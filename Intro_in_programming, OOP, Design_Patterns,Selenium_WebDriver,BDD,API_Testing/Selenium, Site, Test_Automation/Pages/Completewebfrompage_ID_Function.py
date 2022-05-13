from basepage import BasePage
from selenium.webdriver.common.by import By


class MappingCompleteWebFormPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    JOB_TITLE = (By.ID, "job-title")
    HIGH_SCHOOL = (By.ID, "radio-button-1")
    COLLEGE = (By.ID, "radio-button-2")
    GRAD_SCHOOL = (By.ID, "radio-button-3")
    MALE = (By.ID, "checkbox-1")
    FEMALE = (By.ID, "checkbox-2")
    PREFER_NOT_TO_SAY = (By.ID, "checkbox-3")
    YEARS_OF_EXPERIENCE = (By.ID, "select-menu")
    ZERO = (By.ID, "select-menu")
    ZERO_TO_ONE = (By.ID, "select-menu")
    TWO_FOUR = (By.ID, "select-menu")
    FIVE_NINE = (By.ID, "select-menu")
    TEN = (By.ID, "select-menu")
    DATA = (By.ID, "datepicker")
    SUBMIT = (By.LINK_TEXT, "http://formy-project.herokuapp.com/thanks")

    def select_first_name(self):
        self._driver.find_element(*self.FIRST_NAME).send_keys("Hyacinth")

    def select_last_name(self):
        self._driver.find_element(*self.LAST_NAME).send_keys("White")

    def select_job_title(self):
        self._driver.find_element(*self.JOB_TITLE).send_keys("A very good job")

    def select_high_school(self):
        self._driver.find_element(*self.HIGH_SCHOOL).click()

    def select_college(self):
        self._driver.find_element(*self.COLLEGE).click()

    def select_grad_school(self):
        self._driver.find_element(*self.GRAD_SCHOOL).click()

    def select_male(self):
        self._driver.find_element(*self.MALE).click()

    def select_female(self):
        self._driver.find_element(*self.FEMALE).click()

    def select_prefer_not_to_say(self):
        self._driver.find_element(*self.PREFER_NOT_TO_SAY).click()

    def select_years_of_experience(self):
        self._driver.find_element(*self.YEARS_OF_EXPERIENCE)
        self._driver.find_element(*self.ZERO).send_keys(0)
        # self._driver.find_element(*self.ZERO_TO_ONE).send_keys(0 - 1)
        self._driver.find_element(*self.TWO_FOUR).send_keys(2 - 4)
        # self._driver.find_element(*self.FIVE_NINE).send_keys(5 - 9)
        # self._driver.find_element(*self.TEN).send_keys(10)

    def select_data(self):
        self._driver.find_element(*self.DATA).click()
        self._driver.find_element(*self.DATA).send_keys("03/07/2022").click()

    def select_submit(self):
        self._driver.find_element(*self.SUBMIT)




