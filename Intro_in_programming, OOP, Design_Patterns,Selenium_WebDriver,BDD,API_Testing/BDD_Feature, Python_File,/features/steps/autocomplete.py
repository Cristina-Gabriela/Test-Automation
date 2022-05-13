from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@given(u'the site formy')
def step_impl(context):
    context.browser = webdriver.Chrome(ChromeDriverManager().install())
    context.browser.get("http://formy-project.herokuapp.com/")


@when(u'the person click on the Autocomplete')
def step_impl(context):
    context.browser.find_element(By.LINK_TEXT, "Autocomplete").click()


@when(u'open a new page')
def step_impl(context):
    context.browser.get("http://formy-project.herokuapp.com/autocomplete")


@then(u'he fill all blank spaces {address},{Street address},{Street address2},{City},{State},{Zip code},{Country}')
def step_impl(context):
    result1 = context.browser.get(By.ID, "autocomplete").send_keys("Str.2600 Pearl Street, Boulder")
    assert "Str.2600 Pearl Street, Boulder" in result1.text

    result2 = context.browser.get(By.ID, "street_number").send_keys("Boulder")
    assert "Boulder" in result2.text

    result3 = context.browser.find_element(By.ID, "route").send_keys("Abc")
    assert "Abc" in result3.text

    result4 = context.browser.find_element(By.ID, "locality").send_keys("Mountain View")
    assert "Mountain View" in result4.text

    result5 = context.browser.find_element(By.ID, "administrative_area_level_1").send_keys("SUA")
    assert "SUA" in result5.text

    result6 = context.browser.find_element(By.ID, "postal_code").send_keys("1600")
    assert "1600" in result6.text

    result7 = context.browser.find_element(By.ID, "country").send_keys("California")
    assert "California" in result7.text


@then(u'he fill all blank spaces 2300 Traverwood, -, MI, -, United States, 48105, California')
def step_impl(context):
    result1 = context.browser.get(By.ID, "autocomplete").send_keys("Str.2600 Pearl Street, Boulder")
    assert "Str.2600 Pearl Street, Boulder" in result1.text

    result2 = context.browser.get(By.ID, "street_number").send_keys("Boulder")
    assert "Boulder" in result2.text

    result3 = context.browser.find_element(By.ID, "route").send_keys("")
    assert "Abc" in result3.text

    result4 = context.browser.find_element(By.ID, "locality").send_keys("")
    assert "Mountain View" in result4.text

    result5 = context.browser.find_element(By.ID, "administrative_area_level_1").send_keys("")
    assert "SUA" in result5.text

    result6 = context.browser.find_element(By.ID, "postal_code").send_keys("")
    assert "1600" in result6.text

    result7 = context.browser.find_element(By.ID, "country").send_keys("")
    assert "California" in result7.text


@then(u'he fill all blank spaces 1 Hacker Way, Menlo Park, MI, -, United States, 94025, California')
def step_impl(context):
    result1 = context.browser.get(By.ID, "autocomplete").send_keys("")
    assert "2300 Traverwood" in result1.text

    result2 = context.browser.get(By.ID, "street_number").send_keys("1 Hacker Way")
    assert "1 Hacker Way" in result2.text
    result3 = context.browser.find_element(By.ID, "route").send_keys("")
    assert "Abc" in result3.text

    result4 = context.browser.find_element(By.ID, "locality").send_keys("aMountain Viewb")
    assert "Mountain View" == result4.text

    result5 = context.browser.find_element(By.ID, "administrative_area_level_1").send_keys("")
    assert "SUA" in result5.text

    result6 = context.browser.find_element(By.ID, "postal_code").send_keys("")
    assert "1600" in result6.text

    result7 = context.browser.find_element(By.ID, "country").send_keys("")
    assert "California" in result7.text
