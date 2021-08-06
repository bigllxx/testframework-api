from api.base_api import BaseApi


class Notifications(BaseApi):
    """
    消息中心接口集
    """
    data = BaseApi.yaml_load('/data/api_data/notifications.api.yaml')

    def notifications(self):
        """
        获取所有通知
        :return:
        """
        res = self.api_send(self.data['notifications'])
        return res

    def notificationid_mark(self, notificationId):
        """
        标记指定id为已读状态
        :param notificationId:
        :return:
        """
        self.params = {'notificationId': notificationId}
        res = self.api_send(self.data['notificationid_mark'])
        return res

    def notificationid_has_new(self):
        """
        查询是否有新的消息
        :return:
        """
        res = self.api_send(self.data['notificationid_has_new'])
        return res
