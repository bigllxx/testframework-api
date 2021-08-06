from api.base_api import BaseApi
import requests


class Misc(BaseApi):
    """
    各种单独的接口
    """
    data = BaseApi.yaml_load('/data/api_data/misc.api.yaml')

    def health_check(self):
        """
        健康检查
        :return:
        """
        res = self.api_send(self.data['health_check'])
        return res

    def splash_screen(self):
        res = self.api_send(self.data['splash_screen'])
        return res


if __name__ == '__main__':
    m = Misc()
    m.splash_screen()
