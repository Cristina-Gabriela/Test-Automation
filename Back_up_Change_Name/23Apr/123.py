
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

class TestPathFunction(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_go(self):
        self.driver.get("https://www.google.com/maps/place/Croitoria+de+Cafea/@45.6479483,25.5961557,17z/data=!3m1!4b1!4m5!3m4!1s0x40b35b78a52c434d:0x5ef7c2991d2d47c9!8m2!3d45.6479471!4d25.5982908")
        time.sleep(2)
        click = self.driver.find_element(By.CLASS_NAME, "VfPpkd-vQzf8d")
        click.click()
        # click = self.driver.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div[2]/div/div[3]/div/div/div[1]/div[3]/div[1]/img")
        # click.click()
        download_img = self.driver.find_element(By.CLASS_NAME, "Jn12ke")
        download_img.click()


    def tearDown(self):
        self.driver.quit()

