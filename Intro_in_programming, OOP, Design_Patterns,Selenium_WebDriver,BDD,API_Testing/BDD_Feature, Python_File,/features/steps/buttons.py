from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@given(u'the site http://formy-project.herokuapp.com/')
def step_impl(context):
    context.browser.get("http://formy-project.herokuapp.com/")


@when(u'the person click on the Buttons')
def step_impl(context):
    context.browser.find_element(By.LINK_TEXT, "Buttons")


@when(u'click on each button')
def step_impl(context):
    context.browser.find_element(By.LINK_TEXT, "Primary").click()
    context.browser.find_element(By.LINK_TEXT, "Success").click()
    context.browser.find_element(By.LINK_TEXT, "Info").click()
    context.browser.find_element(By.LINK_TEXT, "Warning").click()
    context.browser.find_element(By.LINK_TEXT, "Link").click()
    context.browser.find_element(By.LINK_TEXT, "Left").click()
    context.browser.find_element(By.LINK_TEXT, "Middle").click()
    context.browser.find_element(By.LINK_TEXT, "1").click()
    context.browser.find_element(By.LINK_TEXT, "2").click()
    context.browser.find_element(By.ID, "btnGroupDrop1").click()


@then(u'go back')
def step_impl(context):
    context.driver.back()







