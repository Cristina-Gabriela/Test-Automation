import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Redirect(unittest.TestCase):
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

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()
        time.sleep(5)

        self.driver.get("http://the-internet.herokuapp.com/")
        self.driver.get("http://the-internet.herokuapp.com/redirector")

    def test(self):
        self.driver.find_element(*self.ClickHere).click()
        self.driver.find_element(*self.First_Button).click()
        self.driver.find_element(*self.here_1).click()
        self.driver.find_element(*self.Second_Button).click()
        self.driver.find_element(*self.here_2).click()
        self.driver.find_element(*self.Third_Button).click()
        self.driver.find_element(*self.here_3).click()
        self.driver.find_element(*self.Forth_Button).click()
        self.driver.find_element(*self.here_4).click()

        self.driver.back()
        self.driver.back()

    def tearDown(self):
        self.driver.quit()

        
