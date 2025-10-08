from playwright.sync_api import sync_playwright
import random
def test_get(playwright: sync_playwright):
    context = playwright.request.new_context()
    response = context.get(url = "https://reqres.in/api/users/2")
    assert response.status == 200
    assert response.status_text == 'OK'
    # print(response.json())
    assert response.headers["content-type"] == "application/json; charset=utf-8"

def test_post(playwright:sync_playwright):
    context = playwright.request.new_context()
    # nameRandom =
    body = {
        "name": "bhavika1245",
        "job": "mother11"
    }
    myheaders={"x-api-key":"reqres-free-v1"}
    response = context.post(url = "https://reqres.in/api/users",
                            headers =myheaders,data=body)
    print(response.json()[id])
    assert response.status == 201
    # print( response.headers)
