import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class test_suite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_automation_site(self):
        self.driver.get("https://politrip.com/account/sign-up")

        self.driver.find_element(By.ID, "first-name").click()
        self.driver.find_element(By.ID, "first-name").send_keys("Cristina")
        time.sleep(2)
        self.driver.find_element(By.ID, "cookiescript_accept").click()
        self.driver.find_element(By.ID, "last-name").click()
        self.driver.find_element(By.ID, "last-name").send_keys("Raileanu")
        time.sleep(2)
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("raileanu.cristina91@gmail.com")
        time.sleep(2)
        self.driver.find_element(By.ID, "sign-up-password-input").click()
        self.driver.find_element(By.ID, "sign-up-password-input").send_keys("Incantata de cunostinta")
        time.sleep(2)
        self.driver.find_element(By.ID, "sign-up-confirm-password-input").click()
        self.driver.find_element(By.ID, "sign-up-confirm-password-input").send_keys("Incantata de cunostinta")
        time.sleep(20)

        # question = self.driver.find_element(By.ID, "sign-up-heard-input").click()
        # value = question.get_attribute("value")
        # print(value)
        # time.sleep(20)
        self.driver.find_element(By.CLASS_NAME, "goto-container").click()

        self.driver.find_element(By.ID, "login-email-input").click()
        self.driver.find_element(By.ID, "login-email-input").send_keys("raileanu.cristina91@gmail.com")
        time.sleep(20)

        self.driver.find_element(By.ID, "login-password-input").click()
        self.driver.find_element(By.ID, "login-password-input").send_keys("Incantata de cunostinta")
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, "button-label").click()
        self.driver.back()


    def tearDown(self):
        self.driver.quit()