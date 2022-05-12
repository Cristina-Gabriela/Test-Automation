from behave import *


@given(u'a sample text loaded into the frobulator')
def step_impl(context):
    assert True is not False


@when(u'we activate the frobulator')
def step_impl(context):
    print("Hello")


@then(u'we will find it similar to English')
def step_impl(context):
    assert context.failed is False