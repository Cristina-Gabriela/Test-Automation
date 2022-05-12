import time

from behave import *
from selenium.webdriver.common.by import By


@given(u'I go to autocomplete test')
def step_impl(context):
    context.browser.get("http://formy-project.herokuapp.com/")
    context.browser.find_element(By.LINK_TEXT, "Autocomplete").click()
    time.sleep(2)

@when(u'I type an address')
def step_impl(context):
    context.browser.find_element(By.ID, "autocomplete").send_keys("Cluj_Napoca")

@then(u'The actual result should be the same as the expected')
def step_impl(context):
    result = context.browser.find_element(By.CSS_SELECTOR, "#autocomplete")
    assert "Cluj_Napoca" in result.text



