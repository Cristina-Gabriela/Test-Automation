import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class HandlesSwitch(unittest.TestCase):
    Username = "admin"
    Password = "admin"
    USERNAME = "tomsmith"
    PASSWORD = "SuperSecretPassword!"
    Login = (By.CLASS_NAME, "radius")
    Error = (By.CLASS_NAME, "flash error")
    Logout = (By.CLASS_NAME, "button secondary radius")

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://the-internet.herokuapp.com/login")
        self.driver.maximize_window()
        time.sleep(2)

    def test(self):
        web_element_username_input = self.driver.find_element(By.ID, 'username')
        web_element_username_input.send_keys(self.USERNAME)
        web_element_password_input = self.driver.find_element(By.ID, "password")
        web_element_password_input.send_keys(self.PASSWORD)
        web_element_login = self.driver.find_element(By.CLASS_NAME, "radius")
        web_element_login.click()
        time.sleep(2)
        web_element_logout = self.driver.find_element(By.LINK_TEXT, "Logout")
        web_element_logout.click()
        time.sleep(2)

        i = 1
        while i < 4:
            web_element_username_input = self.driver.find_element(By.ID, 'username')
            web_element_username_input.send_keys(self.USERNAME)
            web_element_password_input = self.driver.find_element(By.ID, "password")
            web_element_password_input.send_keys(self.PASSWORD)
            web_element_login = self.driver.find_element(By.CLASS_NAME, "radius")
            web_element_login.click()
            time.sleep(2)
            web_element_logout = self.driver.find_element(By.LINK_TEXT, "Logout")
            web_element_logout.click()
            time.sleep(2)
            i = i + 1

        for i in range(3):
            web_element_username_input = self.driver.find_element(By.ID, 'username')
            web_element_username_input.send_keys(self.USERNAME)
            web_element_password_input = self.driver.find_element(By.ID, "password")
            web_element_password_input.send_keys(self.PASSWORD)
            web_element_login = self.driver.find_element(By.CLASS_NAME, "radius")
            web_element_login.click()
            time.sleep(2)
            web_element_logout = self.driver.find_element(By.LINK_TEXT, "Logout")
            web_element_logout.click()
            time.sleep(2)

    def tearDown(self):
        self.driver.quit()


