from behave import given, when, then
import requests


BASE_URL = 'http://127.0.0.1:5005'


@given('I am a new user with username "{username}" and password "{password}"')
def step_given_user(context, username, password):
context.username = username
context.password = password


@when('I signup')
def step_when_signup(context):
resp = requests.post(BASE_URL + '/signup', json={
'username': context.username,
'password': context.password
})
context.signup_resp = resp


@then('signup should succeed')
def step_then_signup(context):
assert context.signup_resp.status_code == 201


@when('I login with the same credentials')
def step_when_login(context):
resp = requests.post(BASE_URL + '/login', json={
'username': context.username,
'password': context.password
})
context.login_resp = resp


@then('login should succeed')
def step_then_login(context):
assert context.login_resp.status_code == 200