Feature: User signup and login


Scenario: Successful signup and login
Given I am a new user with username "behave_user" and password "secret"
When I signup
Then signup should succeed
When I login with the same credentials
Then login should succeed