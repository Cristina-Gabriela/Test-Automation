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
        self.driver.get("https://www.google.com/")
        time.sleep(1)
        self.driver.find_element(By.ID, "L2AGLb").click()

        self.driver.find_element(By.CLASS_NAME, "gLFyf").send_keys("google maps")
        self.driver.find_element(By.CLASS_NAME, "gLFyf").send_keys(Keys.ENTER)

        self.driver.find_element(By.CLASS_NAME, "LC20lb").click()
        self.driver.find_element(By.ID, "searchboxinput").send_keys("Croitoria de Cafea")

        self.driver.find_element(By.ID, "searchboxinput").send_keys(Keys.ENTER)
        time.sleep(10)

        potential_buttons = self.driver.find_elements(By.CLASS_NAME, "S9kvJb")

        send_button = None

        for i in potential_buttons:
            if i.text == "Trimite":
                send_button = i

        send_button.click()
        time.sleep(1)

        copy_link = self.driver.find_element(By.CLASS_NAME, "oucrtf")
        copy_link.click()

        message_LINK_DOC = self.driver.find_element(By.CLASS_NAME, "vrsrZe")
        link_value = message_LINK_DOC.get_attribute("value")
        type_attribute = message_LINK_DOC.get_attribute("type")
        print(link_value)
        print(type_attribute)

        with open("LINK_DOC.txt", "w") as filex:
            filex.write(link_value)

        with open("LINK_DOC.txt", "r") as file_to_read_from:
            read_text = file_to_read_from.read()
        print(f"I read {read_text}")

        with open("Download_image", "wb") as file:
            file.write(self.driver.find_element(By.CLASS_NAME, "Jn12ke").screenshot_as_png)

        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

