import requests
from typing import Union
import datetime
import json

with open('authrizotion.json', 'r') as fp:
    jwt = json.load(fp)['jwt']


class DZApi:

    # jwt为请求的Authorization

    @staticmethod
    def get_partiesInfo(before_date: Union[str, datetime.datetime] = None) -> list:
        url = 'https://apis-ff.zaih.com/flash-whisper/v2/applications?filter=all&page=1&per_page=100'
        payload = {}
        headers = {
            'Authorization': jwt,
            'Host': 'apis-ff.zaih.com',
            'User-Agent': 'ios dizhuaApp 1.9.2'
        }
        response = requests.request("GET", url, headers=headers, data=payload)
        if not before_date:
            return response.json()
        else:
            pass  # 日期问题暂时pass

    @staticmethod
    def get_userInfo(userId: str, login: bool = False):
        url = f'https://dz.zaih.com/activity/whisper_api/v2/square/accounts/{userId}'
        payload = {}
        headers = {
            'Host': 'dz.zaih.com',
            'User-Agent': 'ios dizhuaApp 1.9.2'
        }
        if login:
            headers['Authorization'] = jwt
        response = requests.request("GET", url, headers=headers, data=payload)
        return response.json()

    @staticmethod
    def get_partyDetail(partyId: str):
        url = f'https://apis-ff.zaih.com/flash-whisper/v2/application/{partyId}/room_detail'

        payload = {}
        headers = {
            'Authorization': jwt,
            'Host': 'apis-ff.zaih.com',
            'User-Agent': 'ios dizhuaApp 1.9.2'
        }

        response = requests.request("GET", url, headers=headers, data=payload)
        return response.json()
