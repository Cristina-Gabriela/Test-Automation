import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class test_suite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

    def test_automation_site(self):
        self.driver.get("https://politrip.com/appointment?therapyCategory=Hiking&language=fr")
        self.driver.find_element(By.TAG_NAME, "Mia Hellberg").click()

    def tearDown(self):
        self.driver.quit()
