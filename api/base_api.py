import datetime
import json
from run import *
from jsonpath import jsonpath
import requests
import yaml
from common.logs import Logger
from common.action import get_config


class BaseApi:
    params = {}
    _data = {}
    _url = get_config('/config.ini', 'api_config')['url']
    _token = get_config('/config.ini', 'api_config')['token']
    log = Logger('base')

    @classmethod
    def yaml_load(cls, path):
        # 封装yaml文件的加载
        dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        with open(dir_path + path, encoding='UTF-8') as f:
            return yaml.safe_load(f)

    @classmethod
    def format(cls, r):
        cls.r = r
        # print(json.dumps(r.json(), indent=2))
        print(json.dumps(json.loads(r.text), indent=2, ensure_ascii=False))

    def jsonpath(self, path, r=None, **kwargs):
        if r is None:
            r = self.r.json()
        return jsonpath(r, path)

    def my_assert(self, res, ass, *args):
        """
        封装断言+日志
        """
        try:
            exec(ass)
            self.log.logger.info(
                '{}: 用例通过，请求时间：{}s'.format(sys._getframe().f_back.f_code.co_name, res.elapsed.total_seconds()))
        except:
            self.log.logger.error(
                '{}: 断言失败 \n 参数：{} \n 返回值: {}'.format(sys._getframe().f_back.f_code.co_name, self.my_params, res.text))
            raise AssertionError('断言失败')

    def api_send(self, req: dict):
        """
        数据驱动的关键，封装了参数替换及请求发送
        参数不替换为字符串，用于url上有参数的接口
        :param req: 加载后的yaml文件，在业务方法中传递，
        :return: request实例对象
        """
        try:
            req['headers']['token'] = self._token  # 给token赋值,token在headers中
            # req['params']['access_token'] = self.token  # 给token赋值,token在url中
        except:
            pass
            # print('该接口不需要token')
        # 模板内容替换  yaml文件中的变量赋值
        raw = yaml.dump(req)  # 转为字符串
        raw = raw.replace(f'${{url}}', self._url)  # 替换url，便于环境切换

        for key, value in self.params.items():  # 替换参数（测试数据）
            if isinstance(value, datetime.date):
                value = value.strftime('%Y-%m-%d')
                raw = raw.replace(f"${{{key}}}", repr(value))  # 如果参数是datetime.date类型的，先转为字符串
            else:
                raw = raw.replace(f"${{{key}}}", value)
        req = yaml.safe_load(raw)  # 转为yaml
        self.my_params = req
        # print('\n参数：', req)

        r = requests.request(
            method=req['method'],
            url=req['url'],
            params=req['params'],
            headers=req['headers'],
            json=req['json'],
            verify=False
        )
        # print('响应：', r.status_code, r.text)
        return r

    def api_send_string(self, req: dict):
        """
        数据驱动的关键，封装了参数替换及请求发送
        参数替换为字符串，用于不接受int的接口
        :param req: 加载后的yaml文件，在业务方法中传递，
        :return: request实例对象
        """
        try:
            req['headers']['token'] = self._token  # 给token赋值,token在headers中
            # req['params']['access_token'] = self.token  # 给token赋值,token在url中
        except:
            pass
            # print('该接口不需要token')
        # 模板内容替换  yaml文件中的变量赋值
        raw = yaml.dump(req)  # 转为字符串
        raw = raw.replace(f'${{url}}', self._url)  # 替换url，便于环境切换

        for key, value in self.params.items():  # 替换参数（测试数据）
            if isinstance(value, datetime.date):
                value = value.strftime('%Y-%m-%d')
                raw = raw.replace(f"${{{key}}}", repr(value))  # 如果参数是datetime.date类型的，先转为字符串
            else:
                raw = raw.replace(f"${{{key}}}", repr(value))
        req = yaml.safe_load(raw)  # 转为yaml
        # print('\n参数：', req)

        r = requests.request(
            method=req['method'],
            url=req['url'],
            params=req['params'],
            headers=req['headers'],
            json=req['json']
        )
        # print('响应：', r.status_code, r.text)
        return r

    def steps_run(self, steps: list):

        for step in steps:
            # print(step)
            # 模板内容替换
            # todo: 使用format
            raw = yaml.dump(step)
            for key, value in self.params.items():
                raw = raw.replace(f"${{{key}}}", repr(value))
                # print("replace")
                # print(raw)
            step = yaml.safe_load(raw)

            if isinstance(step, dict):
                if "method" in step.keys():
                    method = step['method'].split('.')[-1]
                    # todo: 用装饰器精简参数
                    getattr(self, method)(**step)  # 调用实例化对象（谁调的这个方法谁就是self，一般是子类下的方法）下的method方法
                if "extract" in step.keys():
                    self._data[step["extract"]] = getattr(self, 'jsonpath')(**step)
                    print("extract")
                    print(self._data[step["extract"]])

                if "assertion" in step.keys():
                    assertion = step["assertion"]
                    if isinstance(assertion, str):
                        assert eval(assertion)
                    if assertion[1] == "eq":
                        assert assertion[0] == assertion[2]
