import time
import unittest

import self
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class Test_Google(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def testAutomation(self):
        self.driver.get("https://www.google.com/")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "L2AGLb > div").click()
        time.sleep(2)

        self.driver.find_element(By.CLASS_NAME, "gLFyf").click()
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, "gLFyf").send_keys("google maps")
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, "gLFyf").send_keys(Keys.ENTER)
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, "LC20lb").click()
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, "nhb85d").send_keys("Croitoria de cafea")
        time.sleep(2)
        self.driver.find_element(By.CLASS_NAME, "nhb85d").send_keys(Keys.ENTER)
        time.sleep(2)
        class_button = self.driver.find_element(By.CLASS_NAME, "S9kvJb")

        send_button = None
        for element in class_button:
            if element.text == 'Trimite':
                send_button = element

        class_buttons = self.driver.find_elements(By.CLASS_NAME, "m6QErb")

        cell_button = None

        for element in class_buttons:
            if element.text == "Trimite pe telefon":
                cell_button = element

        the_big_class = self.driver.find_elements(By.CLASS_NAME, "S9kvJb")

        label = None

        for circle in the_big_class:
            if circle.text == "Trimite pe telefon":
                label = circle

        self.driver.find_element(By.CLASS_NAME, "oucrtf").click()

        download_image = self.driver.find_element(By.CLASS_NAME, "Jn12ke")
        link_value = download_image.get_attribute("src")
        print(link_value)

        with open("Doc_image.txt", "w") as Monaco:
            Monaco.write(link_value)

        with open("Doc_image.txt", "r") as Photo:
            Photo_link = Photo.read()

        print(f" This is the link: {Photo_link}")

        time.sleep(2)

    def tearDown(self):
        self.driver.quit()



