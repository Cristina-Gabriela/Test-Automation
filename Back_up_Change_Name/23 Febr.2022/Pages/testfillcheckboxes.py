import time
import unittest

from checkboxesMapping import CheckboxesPage
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class TestFillCheckboxes(unittest.TestCase):

    def __init__(self):
        self.driver = None

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def fill_check_boxes(self):
        self.driver.get("http://formy-project.herokuapp.com/checkbox")
        time.sleep(2)
        checkboxes_page_obj = CheckboxesPage(driver=self.driver)
        checkboxes_page_obj.select_checkbox1()

        time.sleep(1)
        checkboxes_page_obj.select_checkbox2()

        time.sleep(1)
        checkboxes_page_obj.select_checkbox3()

        time.sleep(2)

    def quit(self):
        self.driver.quit()


test_fill_checkboxes = TestFillCheckboxes()
test_fill_checkboxes.setUp()
test_fill_checkboxes.fill_check_boxes()
test_fill_checkboxes.quit()


