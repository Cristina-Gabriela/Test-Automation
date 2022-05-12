from behave import *
from nose.tools import eq_, ok_


@given(u'I search for a valid account')
def step_impl(context):
    context.browser.get


def find_elements(browser, id):
    pass


def get_element(browser, id):
    pass


@then(u'I will see the account details')
def step_impl(context):
    elements = find_elements(context.browser, id='no-account')
    eq_(elements, [], 'account not found')
    h = get_element(context.browser, id='account-head')
    ok_(h.text.startswith("Account 61415551234"),
        'Heading %r has wrong text' % h.text)



