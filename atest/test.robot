*** Settings ***
Library         REST    http://localhost:48080/
Documentation   Acceptance test for REST API in Flask
...             build using RESTinstance library


*** Test Cases ***
GET existing items
    GET         /items
    Output      response body
    [Teardown]  Output schema

GET existing items
    GET         /users
    Integer     response status           404
    Output      response body
