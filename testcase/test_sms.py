import allure
import pytest
from api.app_api.sms import Sms
from common.logs import Logger


@allure.feature('短信相关接口')
class TestSms:

    @classmethod
    def setup_class(cls):
        cls.sms = Sms()
        cls.sms.log = Logger('sms')

    @allure.story('发送短信')
    @pytest.mark.parametrize('phone', ['13072127150', '1310375902', ''])
    def test_sms_send(self, phone):
        res = self.sms.sms_send(phone)
        self.sms.my_assert(res, 'assert res.status_code == 200 or 400')
