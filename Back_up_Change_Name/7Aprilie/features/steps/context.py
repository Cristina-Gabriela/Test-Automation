from behave import *


@given(u'I have a new "{item}" in my cart')
def step_impl(context, item):
    print("I have a new {}".format(item))


@when(u'I click on "{text}"')
def step_impl(context, text):
    print("I click on {}".format(text))


@then(u'I should see "{txt}"')
def step_impl(context, txt):
    print("I should see".format(txt))