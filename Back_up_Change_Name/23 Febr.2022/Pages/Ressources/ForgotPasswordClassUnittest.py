import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class ForgotPasswordAutomation(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://the-internet.herokuapp.com/")
        time.sleep(1)
        self.driver.get("http://the-internet.herokuapp.com/forgot_password")
        self.driver.maximize_window()

    def testAutomation(self):
        time.sleep(1)
        self.driver.find_element(By.ID, "email").send_keys("abc@mail.com")
        time.sleep(2)
        self.driver.find_element(By.ID, "form_submit").click()
        time.sleep(1)

        window_one = self.driver.window_handles[0]
        window_two = self.driver.window_handles[1]

        time.sleep(2)
        i = 0
        while i < 10:
            self.driver.switch_to.window(window_one)
            self.driver.switch_to.window(window_two)
            i += 1

            time.sleep(2)


    def tearDown(self):
        self.driver.quit()


# nu inteleg de ce nu imi da TP