# coding=utf-8
import os
import sys
import time
import pytest
from common.action import del_file
import configparser
from common.send_email import SendEmail
from api.get_token import Token


def choice_env():
    config = configparser.ConfigParser()
    config.read('./config.ini')
    if len(sys.argv) == 1 or sys.argv[1] == 'qa':
        config.set('api_config', 'url', 'xxx')
        print('environment：xxx')
    elif sys.argv[1] == 'test':
        config.set('api_config', 'url', 'xxx')
        print('environment：xxx')
    else:
        print('Please specify the environment: test or qa')
    config.write(open('./config.ini', "r+"))


if __name__ == '__main__':
    choice_env()  # 环境选择，写入配置文件
    Token().get_token()  # 获取token，写入配置文件

    # 清除allure目录下所有文件
    try:
        del_file('result/report/allure')
    except:
        pass
    # allure测试报告路径
    allure_path = 'result/report/allure'
    # html报告路径
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    html_path = 'result/report/html/{}.html'.format(now)

    # 执行测试并生成allure报告 & html测试报告
    try:
        pytest.main(
            ['-s', '-n', '3', '--alluredir', allure_path, 'testcase', '--html={}'.format(html_path),
             '--self-contained-html'])
    except:
        pass

    # 运行allure服务
    try:
        os.system('allure serve result/report/allure')
    except:
        pass

    # html报告邮件发送
    html_dir = SendEmail().acquire_report_address('result/report/html')
    SendEmail().send_email(html_dir)
