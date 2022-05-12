import time
import unittest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from KeyBoardAndMouseInputPageMapping import Key_board_and_Mouse_InputPage


class KeyboardandMouseInput(unittest.TestCase):
    def __init__(self):
        self.driver = None

    def setup(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def automation(self):
        self.driver.get("http://formy-project.herokuapp.com/keypress")

        obj = Key_board_and_Mouse_InputPage(driver=self.driver)
        time.sleep(1)
        obj.click_on_page()
        time.sleep(1)
        obj.enter_full_name()
        time.sleep(1)
        obj.enter_button()
        time.sleep(1)

    def quit(self):
        self.driver.quit()


w = KeyboardandMouseInput()
w.setup()
w.automation()
w.quit()

