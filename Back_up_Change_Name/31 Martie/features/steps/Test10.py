
from behave import *


@given(u'The website https://twitter.com')
def step_impl(context):
    print("Given The website https://twitter.com")


@when(u'Click on this site')
def step_impl(context):
    print("When Click on this site")


@when(u'Press Enter')
def step_impl(context):
    print("When Press Enter")


@then(u'Open a new file with the name of this app')
def step_impl(context):
    print("Then Open a new file with the name of this app")


@then(u'Try to login')
def step_impl(context):
    print("Then Try to login")


@then(u'Enter your twitter@user.com')
def step_impl(context):
    print("Then Enter your twitter@user.com")


@then(u'Press click')
def step_impl(context):
    print("Then Press click")


@given(u'The page https://github.com')
def step_impl(context):
    print("Given The page https://github.com")


@when(u'The founder find the search bar')
def step_impl(context):
    print("When The founder find the search bar")


@when(u'Press enter on this')
def step_impl(context):
    print("When Press enter on this")


@then(u'He/she enter Twitter on the search bar')
def step_impl(context):
    print("Then He/she enter Twitter on the search bar")


@then(u'click enter')
def step_impl(context):
    print("Then click enter")