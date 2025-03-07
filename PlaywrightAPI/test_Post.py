from playwright.sync_api import sync_playwright
#need to use random function to create new email each time to get 201 response
def test_list(playwright: sync_playwright()):
    data = {
        "name":"pmnnvritii",
        "gender":"male",
        "email":"pdftimmm@email.kkk",
        "status":"active"
    }

    context = playwright.request.new_context(base_url="https://gorest.co.in/")
    response = context.post(url = "public/v2/users",data=data,headers={"Authorization":"Bearer af5f99755b7300518fad5852a6b18429dbfb69eae3867303570965c2ee6fbaff"})
    print(response)
    assert response.status == 201
    assert response.status_text == 'Created'