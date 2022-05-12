from behave import *


@given(u'I find recent order from database')
def step_impl(context):

    print("Finding an order from the database ...")
    context.order_num = "123"

    print("Found an order.Order number: {}".format(context.order_num))



@when(u'I issue a refund for the order')
def step_impl(context):


@then(u'payment should get processed for the user')
def step_impl(context):


@when(u'I issue a refund on the same order')
def step_impl(context):


@then(u'the refund should fail to process')
def step_impl(context):