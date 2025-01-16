*** Settings ***
Library     RequestsLibrary
Library    Collections

*** Variables ***
${baseUrl}      https://api.weatherstack.com/
${city}         New Delhi
${ACCESS_KEY}     620815f8dc8a5804ba39214ac34db1b5
${QUERY}         New York

*** Test Cases ***
getCurrentCity
    ${params}    Create Dictionary    access_key=${ACCESS_KEY}    query=${QUERY}
    Create Session    mySession    ${baseUrl}
    ${response}=      Get Request    mySession   current   params=${params}
    Log     ${response.status_code}
    Log     ${response.content}
    Log     ${response.headers}
*** Keywords ***