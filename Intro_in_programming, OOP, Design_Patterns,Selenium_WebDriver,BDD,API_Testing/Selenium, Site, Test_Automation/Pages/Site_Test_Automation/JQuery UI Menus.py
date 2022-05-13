import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
time.sleep(2)

driver.get("http://the-internet.herokuapp.com/")
JQuery_UI_Menus = (By.LINK_TEXT, "JQuery UI Menus")
driver.find_element(*JQuery_UI_Menus).click()

time.sleep(2)

Link_Button_JQuery_UI_Menus = (By.LINK_TEXT, "JQuery UI Menus")
driver.find_element(*Link_Button_JQuery_UI_Menus).click()
driver.back()

time.sleep(2)

Enabled = (By.CSS_SELECTOR, "ui-corner-all")
driver.find_element(*Enabled).click()

time.sleep(2)
Downloads = (By.ID, "ui-id-4")
driver.find_element(*Downloads).click()
time.sleep(2)

PDF = (By.ID, "ui-id-6")
CSV = (By.ID, "ui-id-7")
EXCEL = (By.ID, "ui-id-2")
Back_to_JQuery_UI = (By.ID, "ui-id-5")
driver.find_element(*Back_to_JQuery_UI).click()
Menu = (By.LINK_TEXT, "Menu")
driver.find_element(*Menu).click()
driver.quit()

