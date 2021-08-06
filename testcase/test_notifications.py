import allure
from api.app_api.notifications import Notifications
from common.logs import Logger


@allure.feature('通知相关接口')
class TestTtp:

    @classmethod
    def setup_class(cls):
        cls.nc = Notifications()
        cls.nc.log = Logger('notifications')

    @allure.story('获取所有通知')
    def test_notifications(self):
        res = self.nc.notifications()
        self.nc.my_assert(res, 'assert res.status_code == 200')

    @allure.story('标记通知为已读')
    def test_notification_mark(self):
        try:
            notification_id = self.nc.notifications().json()['list'][0]['id']
            res = self.nc.notificationid_mark(notification_id)
            self.nc.my_assert(res, 'assert res.status_code == 200')
        except:
            self.nc.log.logger.info('没有新通知')

    @allure.story('查询是否有新通知')
    def test_notification_has_new(self):
        res = self.nc.notificationid_has_new()
        self.nc.my_assert(res, "assert 'hasNewNotification' in res.json()")
