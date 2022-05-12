from basepage import BasePage
from selenium.webdriver.common.by import By


class Key_board_and_Mouse_InputPage(BasePage):
    Full_name = (By.ID, "name")
    Button = (By.ID, "button")

    def click_on_page(self):
        x = self._driver.find_element(*self.Full_name).click()

    def enter_full_name(self):
        y = self._driver.find_element(By.ID, "name").send_keys("My name")

    def enter_button(self):
        z = self._driver.find_element(By.ID, "button").click()


        