import os
import sys
import time
import requests
from common.action import get_config
import configparser


class Token:
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '/config.ini'

    def get_token(self):
        i = 0
        while True:
            i = i + 1

            res = requests.request(
                method='post',
                url=get_config('/config.ini', 'api_config')['url'] + '/user/mobile/oauth',
                headers={'Content-Type': 'application/json'},
                json={
                    'phone_number': '13103759028',
                    'captcha': '9999'
                },
                verify=False
            )

            if i < 20 and res.status_code == 200:
                token = res.json()['token']
                config = configparser.ConfigParser()
                config.read(self.path)
                config.set('api_config', 'token', token)
                config.write(open(self.path, "r+"))
                break
            elif i >= 20:
                print('共【{}】次获取token失败，程序终止'.format(i))
                sys.exit()
            else:
                print('第【{}】次获取token失败，重新获取'.format(i))
                time.sleep(3)


if __name__ == '__main__':
    Token().get_token()
