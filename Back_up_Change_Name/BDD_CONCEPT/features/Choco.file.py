from behave import *


@given(u'The product {name}')
def step_impl(context):
    print('Given The product {name}')


@when(u'In the location {x}')
def step_impl(context):
    print('When In the location {x}')


@when(u'Buy more {products}')
def step_impl(context):
    print('When Buy more {products}')


@then(u'I will enjoy {name}')
def step_impl(context):
    print('Then I will enjoy {name}')



@given(u'The product apple')
def step_impl(context):
    print('Given The product apple')


@when(u'In the location here')
def step_impl(context):
    print('When In the location here')


@when(u'Buy more fruits')
def step_impl(context):
    print('When Buy more fruits')


@then(u'I will enjoy apple')
def step_impl(context):
    print('Then I will enjoy apple')


@given(u'The product juice')
def step_impl(context):
    print('Given The product juice')


@when(u'In the location town')
def step_impl(context):
    print('When In the location town')

@when(u'Buy more this')
 def step_impl(context):
    print('When Buy more this')


@then(u'I will enjoy juice')
def step_impl(context):
     print('Then I will enjoy juice')
     
     
     
