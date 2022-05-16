import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Facebook_Automation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

    def AutomationTest(self):
        self.driver.get("https://www.facebook.com/cristina.raileanu.3/")
        self.driver.find_element(By.CSS_SELECTOR,
                                 "a.qu0x051f:nth-child(3) > div:nth-child(1) > span:nth-child(1)").click()

        self.driver.find_element(By.CSS_SELECTOR,
                                 "a.oajrlxb2:nth-child(4) > div:nth-child(1) > span:nth-child(1)").click()

        self.driver.find_element(By.CSS_SELECTOR,
                                 "a.oajrlxb2:nth-child(5) > div:nth-child(1) > span:nth-child(1)").click()

    def tearDown(self):
        self.driver.quit()




