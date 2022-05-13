from basepage import BasePage
from selenium.webdriver.common.by import By


class AutocompleteMapping(BasePage):
    ADDRESS = (By.ID, "autocomplete")
    STREET_ADDRESS_1 = (By.ID, "street_number")
    STREET_ADDRESS_2 = (By.ID, "route")
    CITY = (By.ID, "locality")
    STATE = (By.ID, "administrative_area_level_1")
    ZIP_CODE = (By.ID, "postal_code")
    COUNTRY = (By.ID, "country")

    def select_address(self):
        self._driver.find_element(*self.ADDRESS).send_keys("Amphitheatre Parkway")

    def select_street_address_1(self):
        self._driver.find_element(*self.STREET_ADDRESS_1).send_keys("1600")

    def select_street_address_2(self):
        self._driver.find_element(*self.STREET_ADDRESS_2).send_keys("1601")

    def select_city(self):
        self._driver.find_element(*self.CITY).send_keys("California")

    def select_state(self):
        self._driver.find_element(*self.STATE).send_keys("SUA")

    def select_zip_code(self):
        self._driver.find_element(*self.ZIP_CODE).send_keys("94043 ")

    def select_country(self):
        self._driver.find_element(*self.COUNTRY).send_keys("SUA")


        