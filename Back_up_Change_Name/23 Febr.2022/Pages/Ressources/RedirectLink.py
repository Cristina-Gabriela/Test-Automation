import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
time.sleep(5)

driver.get("http://the-internet.herokuapp.com/")
driver.get("http://the-internet.herokuapp.com/redirector")

time.sleep(5)
ClickHere = (By.ID, "redirect")
First_Button = (By.CSS_SELECTOR, ".example > ul:nth-child(3) > li:nth-child(1) > a:nth-child(1)")
time.sleep(5)

here_1 = (By.CSS_SELECTOR, ".example > p:nth-child(2) > a:nth-child(3)")
Second_Button = (By.CSS_SELECTOR, ".example > ul:nth-child(3) > li:nth-child(2) > a:nth-child(1)")
time.sleep(5)

here_2 = (By.CSS_SELECTOR, ".example > p:nth-child(2) > a:nth-child(3)")
Third_Button = (By.CSS_SELECTOR, ".example > ul:nth-child(3) > li:nth-child(3) > a:nth-child(1)")
time.sleep(5)

here_3 = (By.CSS_SELECTOR, ".example > p:nth-child(2) > a:nth-child(3)")
Forth_Button = (By.CSS_SELECTOR, ".example > ul:nth-child(3) > li:nth-child(4) > a:nth-child(1)")
time.sleep(5)

here_4 = (By.CSS_SELECTOR, ".example > p:nth-child(2) > a:nth-child(3)")

driver.find_element(*ClickHere).click()
driver.find_element(*First_Button).click()
driver.find_element(*here_1).click()
driver.find_element(*Second_Button).click()
driver.find_element(*here_2).click()
driver.find_element(*Third_Button).click()
driver.find_element(*here_3).click()
driver.find_element(*Forth_Button).click()
driver.find_element(*here_4).click()

driver.back()
driver.back()

driver.quit()

