import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://the-internet.herokuapp.com/login")
driver.maximize_window()
time.sleep(2)

USER = (By.ID, "username")
PASS = (By.ID, "password")
Login = (By.CLASS_NAME, "radius")
ERROR = (By.ID, "flash-messages")
LOGOUT = (By.CSS_SELECTOR, "#content > div > a")

USERNAME = (By.CSS_SELECTOR, "#content > div > h4 > em:nth-child(1)")
PASSWORD = (By.CSS_SELECTOR, "#content > div > h4 > em:nth-child(2)")
time.sleep(2)

username = driver.find_element(*USERNAME).text
driver.find_element(*USER).send_keys(username)
time.sleep(2)

password = driver.find_element(*PASSWORD).text
driver.find_element(*PASS).send_keys(password)
time.sleep(2)

driver.find_element(*Login).click()
time.sleep(2)

flash_message = driver.find_element(*ERROR).text

if "logged into" in flash_message:
    print("Test passed")
    print(flash_message)
    driver.find_element(*Login).click()
    flash_message2 = driver.find_element(*ERROR).text
    time.sleep(2)
    if "logged out" in flash_message2:
        print("Test passed *2")
    time.sleep(2)
else:
    print("Test failed")

driver.quit()
