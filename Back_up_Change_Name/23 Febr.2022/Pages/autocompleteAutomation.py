import time
import unittest

from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from autocompleteMapping import AutocompleteMapping


class AutocompleteAutomation(unittest.TestCase):
    def __init__ (self):
        self.driver = None

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def automation(self):
        self.driver.get("http://formy-project.herokuapp.com/autocomplete")
        obj = AutocompleteMapping(driver=self.driver)
        time.sleep(1)
        obj.select_address()
        time.sleep(1)
        obj.select_street_address_1()
        time.sleep(1)
        obj.select_street_address_2()
        time.sleep(1)
        obj.select_city()
        time.sleep(1)
        obj.select_state()
        time.sleep(1)
        obj.select_zip_code()
        time.sleep(1)
        obj.select_country()
        time.sleep(1)

    def quit(self):
        self.driver.quit()


obj_final = AutocompleteAutomation()
obj_final.setUp()
obj_final.automation()
obj_final.quit()