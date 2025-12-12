# API endpoint : "https://todo.pixegami.io/"
#  4 test methods and tests
# 1 create
# 2 update
# 3 get [ list]
# 4 delete

import requests


endpoints = "https://todo.pixegami.io/"
# response = requests.get(endpoints)
# print(response)
# data = response.json()
# print(data)
# print(response.status_code)


def test_call():
    response = requests.get(endpoints)
    assert response.status_code == 200
    print(response.json())

def test_create():
    payload =new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    data = create_task_response.json()
    print(data)

    # to validate response data , we nned to use get call[ request]
    # for that we need to user task id from previous API response data

    task_id = data["task"]["task_id"]
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    print(get_task_data)
    assert get_task_data["content"] == payload["content"]
    assert get_task_data["user_id"] == payload["user_id"]

def test_update_task():
    #create , update and get
    pass

def create_task(payload):
    return  requests.put(endpoints + "create-task",json=payload)
def get_task(task_id):
    return  requests.get(endpoints + f"get-task/{task_id}")
def new_task_payload():
    return {"content":"This is my content",
               "user_id":"test_user4",
               "task_id":"test_task3",
                "is_done":False}
