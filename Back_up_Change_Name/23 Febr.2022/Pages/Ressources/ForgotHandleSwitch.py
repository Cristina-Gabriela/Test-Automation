import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class ForgotPasswordAutomation(unittest.TestCase):
    E_MAIL = (By.ID, "email")
    RetrievePassword = (By.ID, "form_submit")
    InternalServerError = (By.CSS_SELECTOR, "body > h1:nth-child(1) > font:nth-child(1)")

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://the-internet.herokuapp.com/")
        self.driver.get("http://the-internet.herokuapp.com/forgot_password")
        self.driver.maximize_window()

    def testAutomation(self):
        time.sleep(2)
        self.driver.find_element(By.ID, "email").send_keys("abc@mail.com")
        time.sleep(4)
        self.driver.find_element(By.ID, "form_submit").click()
        time.sleep(4)
        self.driver.back()
        time.sleep(4)

    def tearDown(self):
        self.driver.quit()


        