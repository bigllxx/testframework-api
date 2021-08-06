import allure
from common.logs import Logger
import pytest
from api.app_api.homepage import HomePage


@allure.feature('首页相关接口')
class TestHomepage:

    @classmethod
    def setup_class(cls):
        cls.c = HomePage()
        cls.c.log = Logger('homepage')

    @allure.story('获取首页广告位 轮播图 瓦片区 配置')
    def test_homepage_banners(self):
        res = self.c.homepage()
        self.c.my_assert(res, 'assert res.json()["code"] == 0')

    @allure.story('获取首页当前最热')
    def test_homepage_grid_cells(self):
        res = self.c.homepage_weekly_hottest()
        self.c.my_assert(res, 'assert res.json()["code"] == 0')

    @allure.story('获取推荐页瓦片区')
    def test_recommend_grid_cell(self):
        res = self.c.recommend_grid_cell()
        self.c.my_assert(res, 'assert res.json()["code"] == 0')

    @allure.story('获取推荐页导航栏')
    def test_recommend_grid_cell(self):
        res = self.c.recommend_nav_bar()
        self.c.my_assert(res, 'assert res.json()["code"] == 0')





