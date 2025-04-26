from playwright.sync_api import sync_playwright

def test_list(playwright: sync_playwright()):
    query_params = {
        "page":"1"
    }
    context = playwright.request.new_context(base_url="https://gorest.co.in/")
    response = context.get(url = "public/v2/users",params=query_params,headers={"Authorization":"Bearer af5f99755b7300518fad5852a6b18429dbfb69eae3867303570965c2ee6fbaff"})
    print(response)
    assert response.status == 200
    assert response.status_text == 'OK'
    res = response.json()
    print(res[0].get('name'))
    assert "Kalinda Khan" == res[0].get('name')

    size = len(res)
    print(size)
    for i in range(0,size-1):
        if "Divya Saini" == res[i].get('name'):
            assert "Divya Saini" == res[i].get('name')
            print("====================assert pass")
            break
        print(res[i].get('name'))