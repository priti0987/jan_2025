*** Settings ***
Library     RequestsLibrary
Library    Collections

*** Variables ***
${baseUrl}      https://api.weatherstack.com/
${ACCESS_KEY}     620815f8dc8a5804ba39214ac34db1b5
${city}         New York

*** Test Cases ***
getCurrentCity
    ${params}    Create Dictionary    access_key=${ACCESS_KEY}    query=${city}
    Create Session    mySession    ${baseUrl}
    ${response}=      Get Request    mySession   current   params=${params}
    ${statusCode}=     convert to string        ${response.status_code}
    Should Be Equal    ${statusCode}    200

    ${body}=    convert to string   ${response.content}
    Should Contain      ${body}      ${city}
    ${contentTypeValue}=    Get From Dictionary    ${response.headers}    content-Type
    Should Be Equal    ${contentTypeValue}  application/json; Charset=UTF-8
*** Keywords ***
