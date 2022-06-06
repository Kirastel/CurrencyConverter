from nose.tools import assert_true
import requests


def test_request_response():
    response = requests.get('https://api.exchangerate-api.com/v4/latest/USD')
    assert_true(response.ok)