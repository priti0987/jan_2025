import json
import requests
import pytest


endpoints = "https://reqres.in/api/users?page=2"

def testGet_API():
    response = requests.get(endpoints)
    print(response.text)
    print(response.status_code)
    assert response.status_code == 200