import allure
import pytest
from api.app_api.goods import Goods
from api.base_api import BaseApi
from common.logs import Logger


@allure.feature('商品接口')
class TestGoods:
    data = BaseApi.yaml_load('/data/case_data/goods.data.yaml')

    @classmethod
    def setup_class(cls):
        cls.goods = Goods()
        cls.goods.log = Logger('goods')

    @allure.story('解析商品链接')
    @pytest.mark.parametrize('link, expect', data['test_goods_parse'])
    def test_goods_parse(self, link, expect):
        res = self.goods.goods_parse(link)
        self.goods.my_assert(res, 'assert res.json()["status"] == "success"')

    @allure.story('新增商品')
    @pytest.mark.skip(reason='不执行该用例')
    def test_goods(self):
        try:
            if len(self.status) > 0:
                res = self.goods.goods(self.status[0], self.goods_url[0])
                try:
                    assert 'goodsId' in res.json()
                    self.log.logger.info('test_goods_parse：用例通过，请求时间：{}s'.format(res.elapsed.total_seconds()))
                except:
                    self.log.logger.error('test_goods_parse: 断言失败 \n 返回值: {}'.format(res.json()))
                    raise AssertionError('断言失败')
            else:
                self.log.logger.error('test_goods_parse: 没有解析成功的商品')
            res = self.goods.goods('success',
                                   'http://gw.alicdn.com/bao/uploaded/i1/2200811252547/O1CN01d91ZqX1UgZLcVQ8g1_!!0-item_pic.jpg')
            self.goods.my_assert(res, 'assert "goodsId" in res.json()')
        except:
            self.log.logger.error('test_goods_parse: 新增商品失败')
