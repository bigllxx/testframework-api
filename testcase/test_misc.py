import allure
import pytest
from api.app_api.misc import Misc
from common.logs import Logger


@allure.feature('各种单独接口')
class TestMisc:

    @classmethod
    def setup_class(cls):
        cls.misc = Misc()
        cls.misc.log = Logger('misc')

    @allure.story('健康检查')
    def test_health_check(self):
        res = self.misc.health_check()
        self.misc.my_assert(res, "assert res.json()['status'] == 'OK'")

    def test_splash_screen(self):
        res = self.misc.splash_screen()
        self.misc.my_assert(res, 'assert res.json()["code"] == 0')
