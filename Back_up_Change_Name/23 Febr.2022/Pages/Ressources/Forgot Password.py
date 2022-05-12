import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("http://the-internet.herokuapp.com/")
driver.get("http://the-internet.herokuapp.com/forgot_password")
driver.maximize_window()

E_MAIL = (By.ID, "email")
RetrievePassword = (By.ID, "form_submit")
InternalServerError = (By.CSS_SELECTOR, "body > h1:nth-child(1) > font:nth-child(1)")



time.sleep(2)
driver.find_element(By.ID, "email").send_keys("abc@mail.com")
time.sleep(4)
driver.find_element(By.ID, "form_submit").click()
time.sleep(4)
driver.back()
time.sleep(4)
driver.quit()

