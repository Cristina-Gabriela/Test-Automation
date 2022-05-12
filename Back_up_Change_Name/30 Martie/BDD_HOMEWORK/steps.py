
from behave import *

@given(u'I have behave installed')
def step_impl(context):
   print('step1')


@when(u'I execute a test')
def step_impl(context):
    print('step2')


@then(u'result should be provided')
def step_impl(context):
    print('step3')

    