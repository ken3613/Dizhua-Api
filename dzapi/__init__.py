import requests

AUTH_BASIC = 'aW9zOmtvcWVyMjFvaGFmZG8xNDA5YXNkZmU='
APP_VERSION = '1.26.0'


class API:
    __auth = ''
    __proxy = {
        'http': None,
        'https': None
    }
    __use_session = False

    def __init__(self, auth, **kwargs):
        self.__auth = auth
        if 'proxies' in kwargs:
            self.__proxy = kwargs['proxies']
        if 'usr_session' in kwargs:
            self.__use_session = kwargs['use_session']
        self.__session = requests.session()

    @staticmethod
    def request_verify_code(mobile: str) -> bool:
        url = 'https://apis-ff.zaih.com/flash-auth/v2/mobile/verification'
        headers = {
            "Content-Type": "application/json",
            "Host": "apis-ff.zaih.com",
            "User-Agent": f"ios dizhuaApp {APP_VERSION}",
            "Authorization": f"Basic {AUTH_BASIC}"
        }
        data = {
            "mobile": mobile
        }
        response = requests.post(url=url, json=data, headers=headers, proxies={'https': None})
        return response.json()

    @staticmethod
    def login(mobile: str, code: str) -> dict:
        url = 'https://apis-ff.zaih.com/flash-auth/v2/oauth/jwt'
        headers = {
            "Content-Type": "application/json",
            "Host": "apis-ff.zaih.com",
            "User-Agent": f"ios dizhuaApp {APP_VERSION}",
            "Authorization": f"Basic {AUTH_BASIC}"
        }
        data = {
            "username": mobile,
            "password": code,
            "auth_approach": "mobile",
            "grant_type": "password"
        }
        response = requests.post(url=url, json=data, headers=headers, proxies={'https': None})
        return response.json()

    def get_parties_data(self):
        url = 'https://apis-ff.zaih.com/flash-whisper/v2/applications?filter=all'
        headers = {
            'Authorization': f'JWT {self.__auth}',
            'Host': 'apis-ff.zaih.com',
            'User-Agent': f'ios dizhuaApp {APP_VERSION}'
        }
        response = self.__session.get(url, headers=headers, proxies=self.__proxy)
        r_json = response.json()
        return r_json

    def get_party_info(self, party_id) -> dict:
        url = f'https://apis-ff.zaih.com/flash-whisper/v2/application/{party_id}/room_detail'
        headers = {
            'Authorization': f'JWT {self.__auth}',
            'Host': 'apis-ff.zaih.com',
            'User-Agent': f'ios dizhuaApp {APP_VERSION}'
        }
        response = self.__session.get(url, headers=headers, proxies=self.__proxy)
        if response.status_code == 200:
            return response.json()
        else:
            return {}

    def get_self_info(self):
        url = 'https://apis-ff.zaih.com/flash-whisper/v2/accounts'
        headers = {
            'Authorization': f'JWT {self.__auth}',
            'Host': 'apis-ff.zaih.com',
            'User-Agent': f'ios dizhuaApp {APP_VERSION}'
        }
        response = self.__session.get(url, headers=headers, proxies=self.__proxy)
        r_json = response.json()
        return r_json

    def get_friends_list(self):
        url = 'https://apis-ff.zaih.com/flash-whisper/v3/relationships/all'
        headers = {
            'Authorization': f'JWT {self.__auth}',
            'Host': 'apis-ff.zaih.com',
            'User-Agent': f'ios dizhuaApp {APP_VERSION}'
        }
        response = self.__session.get(url, headers=headers, proxies=self.__proxy)
        return response.json()

    def get_user_info(self, uid):
        url = f'https://dz.zaih.com/activity/whisper_api/v2/square/accounts/{uid}'
        headers = {
            'Authorization': f'JWT {self.__auth}',
            'Host': 'dz.zaih.com',
            'User-Agent': f'ios dizhuaApp {APP_VERSION}'
        }
        response = self.__session.get(url, headers=headers, proxies=self.__proxy)
        return response.json()
