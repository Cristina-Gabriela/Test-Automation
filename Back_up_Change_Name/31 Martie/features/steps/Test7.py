from behave import *


@given(u'A new website to be Automation Testing')
def step_impl(context):
    print("Given A new website to be Automation Testing")


@when(u'The employee is at work')
def step_impl(context):
    print(u'STEP: When The employee is at work')


@when(u'The requirements are very strict')
def step_impl(context):
    print("When The requirements are very strict")


@then(u'The employee does not have the rights to make a single error')
def step_impl(context):
    print("Then The employee does not have the rights to make a single error")


@given(u'A new update of a preceding website already tested')
def step_impl(context):
    print("Given A new update of a preceding website already tested")


@when(u'The application was arrived at the customer')
def step_impl(context):
    print("When The application was arrived at the customer")


@when(u'The client was connected for the first time')
def step_impl(context):
    print("When The client was connected for the first time")


@then(u'The Automation Tester was notified to verify the new update')
def step_impl(context):
    print("Then The Automation Tester was notified to verify the new update")


@given(u'The same application, tested 2 times was detected with a bug')
def step_impl(context):
    print("Given The same application, tested 2 times was detected with a bug")


@when(u'The customer was connected for the first time on the internet')
def step_impl(context):
    print("When The customer was connected for the first time on the internet")


@when(u'He/She called at our customer service department')
def step_impl(context):
    print("When He/She called at our customer service department")


@then(u'The manager was notified')
def step_impl(context):
    print("Then The manager was notified")