*** Settings ***
Library     RequestsLibrary
Library     Collections

*** Variables ***
${base_Url}         https://reqres.in/api/users
#authentication with other baseurl is not working
#http://restapi.demoqa.com
#/authentication/CheckForAuthentication
*** Test Cases ***
BasicAuthTest
    Create Session    mysession    ${base_Url}
    ${req_reponse}=    Get Request    mysession    /2
    Log         ${req_reponse.content}