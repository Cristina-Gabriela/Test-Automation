import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Test(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def testAutomation(self):
        self.driver.get("https://www.google.ro")

        copy_link = self.driver.find_element(By.CLASS_NAME, "oucrtf")
        copy_link.click()

        text_extraction = self.driver.find_element(By.CLASS_NAME, "vrsrZe")
        value_extraction = text_extraction.get_attribute("value")
        type_extraction = text_extraction.get_attribute("type")
        print(value_extraction)
        print(type_extraction)

        with open("Doc_extraction.txt", "w") as Text_Extraction:
            Text_Extraction.write(value_extraction)


        with open("Doc_extraction.txt", "r") as Text_Extraction_r:
            Read_Extraction_text = Text_Extraction_r.read()
        print(f"This is the extraction of your text : {Read_Extraction_text}")

    def tearDown(self):
        self.driver.quit()

