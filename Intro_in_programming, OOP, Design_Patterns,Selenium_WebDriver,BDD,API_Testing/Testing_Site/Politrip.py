import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class test_suite(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.maximize_window()

    def test_automation_site(self):
        self.driver.get("https://politrip.com/account/sign-up")

        self.driver.find_element(By.ID, "first-name").click()
        self.driver.find_element(By.ID, "first-name").send_keys("Cristina")
        time.sleep(1)
        self.driver.find_element(By.ID, "cookiescript_accept").click()
        self.driver.find_element(By.ID, "last-name").click()
        self.driver.find_element(By.ID, "last-name").send_keys("Raileanu")
        time.sleep(1)
        self.driver.find_element(By.ID, "email").click()
        self.driver.find_element(By.ID, "email").send_keys("raileanu.cristina91@gmail.com")
        time.sleep(1)
        self.driver.find_element(By.ID, "sign-up-password-input").click()
        self.driver.find_element(By.ID, "sign-up-password-input").send_keys("Incantatadecunostinta123@")
        time.sleep(2)

        self.driver.find_element(By.ID, "sign-up-confirm-password-input").click()
        self.driver.find_element(By.ID, "sign-up-confirm-password-input").send_keys("Incantatadecunostinta123@")
        time.sleep(20)

        # question = self.driver.find_element(By.ID, "sign-up-heard-input").click()
        # value = question.get_attribute("value")
        # print(value)
        # time.sleep(20)
        # self.driver.find_element(By.CLASS_NAME, "goto-container").click()

        # self.driver.find_element(By.ID, "login-email-input").click()
        # self.driver.find_element(By.ID, "login-email-input").send_keys("raileanu.cristina91@gmail.com")
        # time.sleep(1)
        #
        # self.driver.find_element(By.ID, "login-password-input").click()
        # self.driver.find_element(By.ID, "login-password-input").send_keys("Incantatadecunostinta123@")
        # time.sleep(1)
        # self.driver.find_element(By.CLASS_NAME, "button-label").click()
        # self.driver.back()
        # time.sleep(1)
        # self.driver.find_element(By.CLASS_NAME, "item-container").click()
        # time.sleep(1)
        #
        # self.driver.find_element(By.ID, "qa_radio-Hiking-select").click()
        # time.sleep(2)
        #
        # self.driver.find_element(By.CLASS_NAME, "name").click()
        # time.sleep(2)
        #
        # self.driver.find_element(By.LINK_TEXT, "Mia Hellberg").click()
        # time.sleep(2)
        # self.driver.find_element(By.CLASS_NAME, "Dominique Willer").click()
        # time.sleep(2)
        # self.driver.find_element(By.CLASS_NAME, "Caroline Noer").click()
        # time.sleep(2)
        # self.driver.find_element(By.CLASS_NAME, "Andrew Smith").click()
        # time.sleep(2)
        # self.driver.find_element(By.CLASS_NAME, "Ignacio Aguado").click()
        # time.sleep(2)
        #
        # self.driver.find_element(By.CLASS_NAME, "fas fa-angle-double-right").click()
        # time.sleep(2)
        # self.driver.find_element(By.ID, "qa_modal-neutral").click()
        # time.sleep(2)
        #
        # self.driver.find_element(By.ID, "qa_footer-contact-us").click()
        # time.sleep(2)
        # self.driver.find_element(By.CLASS_NAME, "qa_footer-terms-and-conditions").click()
        #
        # self.driver.find_element(By.ID, "qa_footer-how-it-works").click()
        # self.driver.back()
        #
        # self.driver.find_element(By.ID, "qa_footer-contact-us").click()
        # self.driver.back()
        #
        #
        # self.driver.find_element(By.ID, "qa_footer-terms-and-conditions").click()
        # self.driver.back()
        #
        # self.driver.find_element(By.ID, "qa_footer-faq").click()
        # self.driver.back()

        # time.sleep(5)
        # self.driver.find_element(By.ID, "qa_radio-Hiking-select").click()
        # self.driver.find_element(By.ID, "qa_radio-Camping-select").click()
        # self.driver.find_element(By.ID, "qa_radio-Swimming-select").click()
        # self.driver.find_element(By.ID, "qa_radio-Kayaking-select").click()
        # self.driver.find_element(By.ID, "qa_radio-Cycling-select").click()
        # self.driver.find_element(By.ID, "qa_radio-Rock Climbing-select").click()
        # self.driver.find_element(By.ID, "qa_radio-Skiing-select").click()
        # self.driver.find_element(By.ID, "qa_radio-Skiing-select").click()
        # self.driver.find_element(By.ID, "qa_appointment-date").click()
        # self.driver.find_element(By.ID, "qa_appointment-date").send_keys("02-05-2022").click()

        # self.driver.find_element(By.CLASS_NAME, "institutions-logo").click()
        # self.driver.find_element(By.LINK_TEXT, "ue")

        # self.driver.find_element(By.TAG_NAME, "blank").click()

    def tearDown(self):
        self.driver.quit()

        # self.driver.find_element(By.ID, "qa_radio - Hiking - select").click()
        # time.sleep(1)

        # self.driver.find_element(By.CSS_SELECTOR,"div.col-6:nth-child(1) > app-organizer-card:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1)").click()
        # time.sleep(1)
        #
        # Mia_button = None
        # for i in big_class:
        #     if i.text == "Mia Hellberg":
        #         Mia_button = i
        # Mia_button.click()
        # time.sleep(2)

        # self.driver.find_element(By.XPATH, "/html/body/app-root/app-home/app-page-template/div/app-cards-wrapper[4]/div/div/div[2]/div[1]/app-video-course-card/div/a/div[1]").click()
        #
        # time.sleep(1)