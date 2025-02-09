from playwright.sync_api import sync_playwright

def test_get(playwright: sync_playwright):
    context = playwright.request.new_context()
    response = context.get(url = "https://gorest.co.in/public/v2/users/7682020",headers ={"Authorization":"Bearer af5f99755b7300518fad5852a6b18429dbfb69eae3867303570965c2ee6fbaff"})
    print(response)
    assert response.status == 200
    assert response.status_text == 'OK'
    print(response.json()["name"])
    assert response.json()["name"] == 'Vedanga Varma'
    res = response.json()
    assert res.get("name")=='Vedanga Varma'
    print(response.headers["content-type"])
    assert response.headers["content-type"] == "application/json; charset=utf-8"
