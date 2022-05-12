from behave import *


@given(u'One computer and the internet')
def step_impl(context):
    print("Given One computer and the internet")


@given(u'The person will start to install pycharm')
def step_impl(context):
    print("Given The person will start to install pycharm")


@when(u'At the beginning of the project')
def step_impl(context):
    print("When At the beginning of the project")


@then(u'He/She try to install some useful python libraries')
def step_impl(context):
    print("Then He/She try to install some useful python libraries")


@then(u'It is the moment to write the code')
def step_impl(context):
    print("Then It is the moment to write the code")


@then(u'The code is run')
def step_impl(context):
    print("Then The code is run")


@then(u'He generate a report')
def step_impl(context):
    print("Then He generate a report")


@then(u'The report is successful')
def step_impl(context):
    print("Then The report is successful")


@given(u'Access at Github Local and Global')
def step_impl(context):
    print("Given Access at Github Local and Global")


@given(u'The Founder publish their code')
def step_impl(context):
    print("Given The Founder publish their code")


@when(u'All the code is uploaded')
def step_impl(context):
    print("When All the code is uploaded")


@then(u'The Open Source Community can verify the code')
def step_impl(context):
    print("Then The Open Source Community can verify the code")


@then(u'They can give the useful advices to the founder')
def step_impl(context):
    print("Then They can give the useful advices to the founder")


@given(u'Publicly the advices with the parts of code')
def step_impl(context):
    print("Given Publicly the advices with the parts of code")


@given(u'The codes will be integrated')
def step_impl(context):
    print("Given The codes will be integrated")


@when(u'The entire code is successfully done')
def step_impl(context):
    print("When The entire code is successfully done")


@then(u'The testers could automatically tested all the lines of code')
def step_impl(context):
    print("Then The testers could automatically tested all the lines of code")


@then(u'The reports will arrived to the founder')
def step_impl(context):
    print("Then The reports will arrived to the founder")