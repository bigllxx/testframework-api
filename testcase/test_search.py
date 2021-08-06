import allure
import pytest
from api.base_api import BaseApi
from api.app_api.search import Search
from common.logs import Logger


@allure.feature('search相关接口')
class TestTtp:
    data = BaseApi.yaml_load('/data/case_data/search.data.yaml')

    @classmethod
    def setup_class(cls):
        cls.se = Search()
        cls.se.log = Logger('search')

    @allure.story('搜索资源')
    @pytest.mark.parametrize('keyword, resource_type, content_type', data['search_resource'])
    def test_search_resource(self, keyword, resource_type, content_type):
        res = self.se.search_resource(keyword, resource_type=resource_type, content_type=content_type)
        self.se.my_assert(res, 'assert res.json()["code"] == 0')

    @allure.story('关键字匹配')
    @pytest.mark.parametrize('keyword, resource_type, content_type', data['search_resource'])
    def test_search_suggest(self, keyword, resource_type, content_type):
        res = self.se.search_suggest(keyword, resource_type=resource_type, content_type=content_type)
        self.se.my_assert(res, 'assert res.json()["code"] == 0')
