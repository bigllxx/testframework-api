from api.base_api import BaseApi


class Sms(BaseApi):
    """
    短信接口集
    """
    data = BaseApi.yaml_load('/data/api_data/sms.api.yaml')

    def sms_send(self, phone_number):
        self.params = {'phone_number': phone_number}
        res = self.api_send_string(self.data['sms_send'])
        return res

    def sms_verify(self):
        pass

    def registry(self):
        pass


if __name__ == '__main__':
    s = Sms()
    s.sms_send('13103759028')
