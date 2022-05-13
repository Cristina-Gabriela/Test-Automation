from behave import *


@given('I have a new "{item}" in my cart')
def step_impl(context, item):
    print("The item is: {}".format(item))


@when('I click on "{button_to_click}"')
def step_impl(context, button_to_click):
    print("I click on {}".format(button_to_click))


@then('I should see "{text}"')
def step_impl(context, text):
    print("I should see {}".format(text))

    if text not in ['success', 'error']:
        raise Exception("Unexpected text passed in.")

    if text.lower() == "success":
        print("Yes")
    else:
        print("NO")

    print("Checking if I see the '{}'".format(text))
    print("PASS. I see the '{}'".format(text))


@given('I start a call with "{number}" participants')
def step_impl(context, number):
    print("I start a call with {}".format(number))
    print(type(number))
    new_type = int(number)
    print(type(new_type))










