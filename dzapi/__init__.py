import requests
from typing import Union
import datetime
import re

AUTH_JWT = ''
AUTH_BASIC = 'aW9zOmtvcWVyMjFvaGFmZG8xNDA5YXNkZmU='
VERSION = '1.9.4'


def login(mobile: str, code: str) -> str:
    url = 'https://apis-ff.zaih.com/flash-auth/v2/oauth/jwt'
    payload = {
        'username': mobile,
        'password': code,
        'auth_approach': 'mobile',
        'grant_type': 'password'
    }
    headers = {
        'User-Agent': f'ios dizhuaApp {VERSION}',
        'Host': 'apis-ff.zaih.com',
        'Authorization': f'Basic {AUTH_BASIC}',
        'Content-Type': 'application/json'
    }
    response = requests.request('POST', url, headers=headers, json=payload)
    return response.json().get('access_token', None)


def verification(mobile: str):
    url = 'https://apis-ff.zaih.com/flash-auth/v2/mobile/verification'
    payload = {
        'mobile': mobile
    }
    headers = {
        'User-Agent': f'ios dizhuaApp {VERSION}',
        'Host': 'apis-ff.zaih.com',
        'Authorization': f'Basic {AUTH_BASIC}',
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, json=payload)


def get_partiesInfo(before_date: Union[str, datetime.datetime] = None) -> list:
    url = 'https://apis-ff.zaih.com/flash-whisper/v2/' \
          'applications?filter=all&page=1&per_page=100'
    payload = {}
    headers = {
        'Authorization': f'JWT {AUTH_JWT}',
        'Host': 'apis-ff.zaih.com',
        'User-Agent': f'ios dizhuaApp {VERSION}'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    if not before_date:
        return response.json()
    else:
        pass  # 日期问题暂时pass


def get_userInfo(userId: str, login_status: bool = False):
    url = f'https://dz.zaih.com/activity/whisper_api/v2/' \
          f'square/accounts/{userId}'
    payload = {}
    headers = {
        'Host': 'dz.zaih.com',
        'User-Agent': f'ios dizhuaApp {VERSION}'
    }
    if login_status:
        headers['Authorization'] = AUTH_JWT
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()


def get_partyDetail(partyId: str):
    url = f'https://apis-ff.zaih.com/flash-whisper/v2/' \
          f'application/{partyId}/room_detail'
    payload = {}
    headers = {
        'Authorization': AUTH_JWT,
        'Host': 'apis-ff.zaih.com',
        'User-Agent': f'ios dizhuaApp {VERSION}'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()


def get_version():
    url = 'https://apps.apple.com/cn/app/' \
          '%E9%80%92%E7%88%AA-%E5%A4%9A%E4%BA%BA' \
          '%E5%8C%B9%E9%85%8D%E8%AF%AD%E9%9F%B3%E4' \
          '%BA%A4%E5%8F%8B%E8%BD%AF%E4%BB%B6/id1474925039'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/81.0.4044.138 Safari/537.36 '
    }
    response = requests.request('GET', url, headers=headers)
    raw = response.text
    return re.search(r'版本 \d\.\d\.\d', raw).group()[3:]


def get_friendsList():
    url = 'https://apis-ff.zaih.com/flash-whisper/v3/relationships/all'
    headers = {
        'Authorization': f'JWT {AUTH_JWT}',
        'Host': 'apis-ff.zaih.com',
        'User-Agent': f'ios dizhuaApp {VERSION}'
    }
    response = requests.request('GET', url, headers=headers)
    return response.json()
