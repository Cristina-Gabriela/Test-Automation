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

        window_one = self.driver.window_handles[0]
        window_one_r = self.driver.window_handles[1]
        window_two = self.driver.window_handles[2]
        window_two_r = self.driver.window_handles[3]
        window_three = self.driver.window_handles[4]
        window_three_r = self.driver.window_handles[5]
        window_four = self.driver.window_handles[6]
        window_four_r = self.driver.window_handles[7]
        window_five = self.driver.window_handles[8]
        window_five_r = self.driver.window_handles[9]

        i = 1
        while i < 5:
            self.driver.switch_to.window(window_one)
            self.driver.switch_to.window(window_one_r)
            self.driver.switch_to.window(window_two)
            self.driver.switch_to.window(window_two_r)
            self.driver.switch_to.window(window_three)
            self.driver.switch_to.window(window_three_r)
            self.driver.switch_to.window(window_four)
            self.driver.switch_to.window(window_four_r)
            self.driver.switch_to.window(window_five)
            self.driver.switch_to.window(window_five_r)

            i += 1

        self.driver.back()
        self.driver.back()

    def tearDown(self):
        self.driver.quit()


        