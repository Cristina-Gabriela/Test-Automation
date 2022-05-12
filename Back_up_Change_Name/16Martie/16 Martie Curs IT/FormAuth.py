import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestFormAuth(unittest.TestCase):
    USER = (By.ID, "username")
    PASS = (By.ID, "password")
    SUBMIT = (By.CLASS_NAME, "radius")
    ERROR = (By.ID, "flash-messages")
    LOGOUT = (By.CSS_SELECTOR, " #content > div > a ")

    USERNAME = (By.CSS_SELECTOR, ".subheader > em:nth-child(1)")
    PASSWORD = (By.CSS_SELECTOR, ".subheader > em:nth-child(2)")

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://the-internet.herokuapp.com/login")
        self.driver.maximize_window()
        time.sleep(2)

    def test(self):
        username = self.driver.find_element(*self.USERNAME).text
        self.driver.find_element(*self.USER).send_keys(username)
        time.sleep(2)

        password = self.driver.find_element(*self.PASSWORD).text
        self.driver.find_element(*self.PASS).send_keys(password)
        time.sleep(2)

        self.driver.find_element(*self.SUBMIT).click()
        time.sleep(2)

        flash_message_ok = self.driver.find_element(*self.ERROR).text

        if "logged into" in flash_message_ok:
            print("Test passed")
            print(flash_message_ok)

            self.driver.find_element(*self.LOGOUT).click()
            time.sleep(2)
            print(flash_message_ok)
            if "logged out" in flash_message_ok:
                print("Test passed x2")
                time.sleep(2)

        else:
            print("Test failed")

    def tearDown(self):
        self.driver.quit()

