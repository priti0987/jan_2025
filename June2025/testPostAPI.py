import requests
import json
import pytest

payload= {
    "name": "testName",
    "job": "testJob"
}

endpoints = "https://reqres.in/api/users"
def test_PostAPI():
    response = requests.post(endpoints,json=payload)
    assert response.status_code == 201
