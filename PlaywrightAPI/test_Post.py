from playwright.sync_api import sync_playwright

def test_list(playwright: sync_playwright()):
    data = {
        "name":"pritii",
        "gender":"male",
        "email":"pritimmm@email.kkk",
        "status":"active"
    }

    context = playwright.request.new_context(base_url="https://gorest.co.in/")
    response = context.post(url = "public/v2/users",data=data,headers={"Authorization":"Bearer af5f99755b7300518fad5852a6b18429dbfb69eae3867303570965c2ee6fbaff"})
    print(response)
    assert response.status == 200
    assert response.status_text == 'OK'