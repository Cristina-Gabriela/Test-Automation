from behave import *


@given(u'I put Red Tree Frog in a blender,')
def step_impl(context):
    assert True is not False


@when(u'I switch the blender on')
def step_impl(context):
    assert True is not False


@then(u'it should transform into mush')
def step_impl(context):
    assert context.failed is False


@given(u'I put iPhone in a blender,')
def step_impl(context):
    assert context.failed is False


@then(u'it should transform into toxic waste')
def step_impl(context):
    pass


@given(u'I put Galaxy Nexus in a blender,')
def step_impl(context):
    pass