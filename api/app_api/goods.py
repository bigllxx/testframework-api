from api.base_api import BaseApi


class Goods(BaseApi):
    """
    商品接口集
    """
    data = BaseApi.yaml_load('/data/api_data/goods.api.yaml')

    def goods(self, parseStatus, goods_url):
        """
        新增商品
        :param parseStatus:
        :param url:
        :return:
        """
        self.params = {'parseStatus': parseStatus, 'goods_url': goods_url}
        res = self.api_send(self.data['goods'])
        return res

    def goods_parse(self, link):
        """
        解析链接
        :param link:
        :return:
        """
        self.params = {'link': link}
        res = self.api_send(self.data['goods_parse'])
        return res
