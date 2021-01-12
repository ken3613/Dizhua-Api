from dzapi import API
from nose.tools import assert_equal, assert_in, assert_true, assert_false, with_setup
import os
from unittest.mock import patch

auth = ''


def setUp():
    global auth
    auth = os.getenv('AUTH')


def test_get_parties_data():
    global auth
    api = API(auth)
    result = api.get_parties_data()
    assert_in('111939705298034855936', str(result))


def test_get_self_info():
    api = API(auth)
    result = api.get_self_info()
    assert_in('哈弟呀', str(result))
    assert_in('佛山', str(result))


def test_get_party_info():
    api = API(auth)
    party_id = api.get_parties_data()[0]['id']
    result = api.get_party_info(party_id)
    assert_equal('青梧里', result['topic']['name'])


def test_get_friend_list():
    api = API(auth)
    result = api.get_friends_list()
    assert_in('Nona', str(result))


def test_get_longin():
    result = API.login('12', '12')
    assert_in('message', str(result))


def test_request_verify_code():
    api = API(auth)
    from random import randint
    result = api.request_verify_code(str(randint(1, 1000)))
    assert_in('ok', str(result))


def test_get_user_info():
    api = API(auth)
    info = api.get_user_info('a1jfayl4zp')
    assert_equal('Nona', info['user_nickname'])


def test_set_proxies():
    api = API(auth,
              proxies=None)
    return True
