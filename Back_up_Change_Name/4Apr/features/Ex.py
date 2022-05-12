from behave import *


@given(u'I go to autocomplete test')
def step_impl(context):
    print("Given I go to autocomplete test")


@when(u'I type an address')
def step_impl(context):
    print("When I type an address")


@then(u'The actual result should be the same as the expected')
def step_impl(context):
    print("Then The actual result should be the same as the expected")