import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestNewProject123():
    def setup_method(self, method):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_newProject123(self):
        self.driver.get("https://politrip.com/account/sign-up")
        self.driver.set_window_size(1440, 900)
        self.driver.find_element(By.ID, "email").send_keys("raileanu.cristina91@gmail.com")
        self.driver.find_element(By.ID, "sign-up-password-input").send_keys("Incantatadecunostinta123@")
        self.driver.find_element(By.ID, "qa_footer-how-it-works").click()
        self.driver.find_element(By.ID, "qa_footer-contact-us").click()
        self.driver.find_element(By.ID, "contactFirstNameInput").click()
        self.driver.find_element(By.ID, "contactLastNameInput").click()
        self.driver.find_element(By.ID, "contact-email-input").click()
        self.driver.find_element(By.ID, "type").click()
        self.driver.find_element(By.CSS_SELECTOR, "option").click()
        self.driver.find_element(By.ID, "contact-message-input").click()
        self.driver.find_element(By.ID, "contact-message-input").send_keys("Ok")
        self.driver.find_element(By.ID, "qa_modal-neutral").click()
        self.driver.find_element(By.ID, "qa_footer-terms-and-conditions").click()
        self.driver.find_element(By.CSS_SELECTOR, ".menu-item:nth-child(2)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".menu-item:nth-child(3)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".menu-item:nth-child(4)").click()
        self.driver.find_element(By.CSS_SELECTOR, ".footer-list").click()
        self.driver.find_element(By.ID, "qa_footer-faq").click()
        self.driver.find_element(By.ID, "qa_modal-neutral").click()