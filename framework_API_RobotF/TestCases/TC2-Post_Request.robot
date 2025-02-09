*** Settings ***
Library     RequestsLibrary
Library     Collections

*** Variables ***
${baseUrl}          https://reqres.in/api


*** Test Cases ***
Post_request_1
    Create Session    mysession    ${baseUrl}
    ${body}=        Create Dictionary   name=priti      job=QA
    ${header}=      Create Dictionary   Content-Type=application/json
    ${response}=    Post Request    mysession    /users     data=${body}        headers=${header}
    Log    ${response.status_code}
    Log    ${response.content}
    ${response_body}=   convert to string   ${response.content}
    Should Contain    ${response_body}    createdAt