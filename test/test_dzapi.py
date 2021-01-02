from dzapi import API
from nose.tools import assert_equal, assert_in, assert_true, assert_false
from unittest.mock import patch


def test_get_parties_data():
    api = API('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
              '.eyJpc3MiOiJpb3MiLCJpYXQiOjE2MDkyOTQ'
              '2NTAsImV4cCI6MTYwOTg5OTQ1MCwiYXVkIjo'
              'iaHR0cHM6Ly9hcGlzLWZmLnphaWguY24vZmx'
              'hc2gtYXV0aC92MS9vYXV0aC9qd3QiLCJzdWI'
              'iOiJhMWF4Y2pkbXlwIiwic2NvcGVzIjpbIm9'
              'wZW4iLCJyZWdpc3RlciIsImxvZ2luIl19.X_'
              'jNUtwH36iYIYKuwc0Q4rkVrGVy8EhDlAguWjTM27Q')
    result = api.get_parties_data()
    assert_in('111939705298034855936', str(result))


def test_get_self_info():
    api = API('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
              '.eyJpc3MiOiJpb3MiLCJpYXQiOjE2MDkyOTQ'
              '2NTAsImV4cCI6MTYwOTg5OTQ1MCwiYXVkIjo'
              'iaHR0cHM6Ly9hcGlzLWZmLnphaWguY24vZmx'
              'hc2gtYXV0aC92MS9vYXV0aC9qd3QiLCJzdWI'
              'iOiJhMWF4Y2pkbXlwIiwic2NvcGVzIjpbIm9'
              'wZW4iLCJyZWdpc3RlciIsImxvZ2luIl19.X_'
              'jNUtwH36iYIYKuwc0Q4rkVrGVy8EhDlAguWjTM27Q')
    result = api.get_self_info()
    assert_in('哈弟呀', str(result))
    assert_in('佛山', str(result))


def test_get_party_info():
    api = API('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
              '.eyJpc3MiOiJpb3MiLCJpYXQiOjE2MDkyOTQ'
              '2NTAsImV4cCI6MTYwOTg5OTQ1MCwiYXVkIjo'
              'iaHR0cHM6Ly9hcGlzLWZmLnphaWguY24vZmx'
              'hc2gtYXV0aC92MS9vYXV0aC9qd3QiLCJzdWI'
              'iOiJhMWF4Y2pkbXlwIiwic2NvcGVzIjpbIm9'
              'wZW4iLCJyZWdpc3RlciIsImxvZ2luIl19.X_'
              'jNUtwH36iYIYKuwc0Q4rkVrGVy8EhDlAguWjTM27Q')
    party_id = api.get_parties_data()[0]['id']
    result = api.get_party_info(party_id)
    assert_equal('青梧里', result['topic']['name'])


def test_get_friend_list():
    api = API('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
              '.eyJpc3MiOiJpb3MiLCJpYXQiOjE2MDkyOTQ'
              '2NTAsImV4cCI6MTYwOTg5OTQ1MCwiYXVkIjo'
              'iaHR0cHM6Ly9hcGlzLWZmLnphaWguY24vZmx'
              'hc2gtYXV0aC92MS9vYXV0aC9qd3QiLCJzdWI'
              'iOiJhMWF4Y2pkbXlwIiwic2NvcGVzIjpbIm9'
              'wZW4iLCJyZWdpc3RlciIsImxvZ2luIl19.X_'
              'jNUtwH36iYIYKuwc0Q4rkVrGVy8EhDlAguWjTM27Q')
    result = api.get_friends_list()
    assert_in('Nona', str(result))


def test_get_longin():
    result = API.login('12', '12')
    assert_in('message', str(result))


def test_request_verify_code():
    api = API('eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9'
              '.eyJpc3MiOiJpb3MiLCJpYXQiOjE2MDkyOTQ'
              '2NTAsImV4cCI6MTYwOTg5OTQ1MCwiYXVkIjo'
              'iaHR0cHM6Ly9hcGlzLWZmLnphaWguY24vZmx'
              'hc2gtYXV0aC92MS9vYXV0aC9qd3QiLCJzdWI'
              'iOiJhMWF4Y2pkbXlwIiwic2NvcGVzIjpbIm9'
              'wZW4iLCJyZWdpc3RlciIsImxvZ2luIl19.X_'
              'jNUtwH36iYIYKuwc0Q4rkVrGVy8EhDlAguWjTM27Q')
    result = api.request_verify_code('123')
    assert_in('message', str(result))
