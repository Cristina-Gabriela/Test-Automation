
import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Window(unittest.TestCase):

    # x = (By.LINK_TEXT, "Click Here")
    # Message = (By.CSS_SELECTOR, ".example > h3:nth-child(1)")

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("http://the-internet.herokuapp.com/windows")
        # self.window_maximize()

    def test(self):
        self.driver.find_element(By.CSS_SELECTOR, "#content > div > a").click()
        x = self.driver.find_element(By.CSS_SELECTOR, ".example > h3:nth-child(1)").text
        print(x)
        time.sleep(1)
        window_one = self.driver.window_handles[0]
        window_two = self.driver.window_handles[1]
        time.sleep(5)
        i = 0

        while i < 10:
            self.driver.switch_to.window(window_one)
            self.driver.switch_to.window(window_two)
            i += 1
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()




