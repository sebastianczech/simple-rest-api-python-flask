*** Settings ***
Library         REST    http://192.168.0.36:48080/
Documentation   Acceptance test for REST API in Flask
...             build using RESTinstance library


*** Test Cases ***
GET items
    GET         /items
    Output      response body
    [Teardown]  Output schema

GET users
    GET         /users
    Integer     response status           404
    Output      response body
