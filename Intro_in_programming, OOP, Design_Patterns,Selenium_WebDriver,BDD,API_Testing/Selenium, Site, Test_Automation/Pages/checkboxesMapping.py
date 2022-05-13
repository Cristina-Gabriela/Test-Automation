from basepage import BasePage
from selenium.webdriver.common.by import By


class CheckboxesPage(BasePage):
    CHECKBOX_ONE = By.ID, "checkbox-1"
    CHECKBOX_TWO = By.ID, "checkbox-2"
    CHECKBOX_THREE = By.ID, "checkbox-3"

    def select_checkbox1(self):
        x = self._driver.find_element(*self.CHECKBOX_ONE)
        x.click()

    def select_checkbox2(self):
        self._driver.find_element(*self.CHECKBOX_TWO).click()

    def select_checkbox3(self):
        self._driver.find_element(*self.CHECKBOX_THREE).click()


        