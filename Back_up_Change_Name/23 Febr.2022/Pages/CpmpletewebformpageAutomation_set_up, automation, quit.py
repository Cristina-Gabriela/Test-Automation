import time
import unittest

from selenium import webdriver
from Completewebformpage_Mapping_ID_Function import MappingCompleteWebFormPage
from webdriver_manager.chrome import ChromeDriverManager


class AutomationCompleteWebFormPage(unittest.TestCase):
    def __init__(self):
        self.driver = None

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def automation(self):
        self.driver.get("http://formy-project.herokuapp.com/form")
        automation_object = MappingCompleteWebFormPage(driver=self.driver)
        time.sleep(1)
        automation_object.select_first_name()
        time.sleep(1)
        automation_object.select_last_name()
        time.sleep(1)
        automation_object.select_job_title()
        time.sleep(1)
        automation_object.select_high_school()
        time.sleep(1)
        automation_object.select_college()
        time.sleep(1)
        automation_object.select_grad_school()
        time.sleep(1)
        automation_object.select_male()
        time.sleep(1)
        automation_object.select_female()
        time.sleep(1)
        automation_object.select_prefer_not_to_say()
        time.sleep(1)
        automation_object.select_years_of_experience()
        time.sleep(1)
        automation_object.select_data()
        time.sleep(1)
        automation_object.select_submit()
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()


object = AutomationCompleteWebFormPage()
object.setUp()
object.automation()
object.tearDown()


