import unittest

import self
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class register_user(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def automationTest(self):
        self.driver.get("http://automationexercise.com")
        buttonHome = self.driver.find_element(By.CLASS_NAME, "fa fa-home")
        assert buttonHome == "Home"
        self.driver.find_element(By.CLASS_NAME, "fa fa-home").click()
        New_user_button = self.driver.find_element(By.TAG_NAME, "h2")
        if New_user_button == "New User Signup!":
            print("Valid !")
        else:
            print("Try again !")
        self.driver.find_element(By.XPATH, "/html/body/section/div/div/div[3]/div/form/input[2]").send_keys("Cristina")
        self.driver.find_element(By.XPATH, "/html/body/section/div/div/div[3]/div/form/input[3]").send_keys(
            "raileanu.cristina91@gmail.com")
        self.driver.find_element(By.CLASS_NAME, "btn btn-default").click()
        self.driver.find_element(By.ID, "id_gender1").click()
        self.driver.find_element(By.ID, "name").send_keys("Cristina")
        self.driver.find_element(By.ID, "password").send_keys("Hecker1233@vjhdighuh546")
        self.driver.find_element(By.ID, "days").click()
        self.driver.find_element(By.CSS_SELECTOR, "#days > option:nth-child(13)")
        self.driver.find_element(By.ID, "months").click()
        self.driver.find_element(By.CSS_SELECTOR, "#months > option:nth-child(6)")
        self.driver.find_element(By.ID, "years").click()
        self.driver.find_element(By.CSS_SELECTOR, "#years > option:nth-child(6)")
        self.driver.find_element(By.ID, "newsletter").click()
        self.driver.find_element(By.ID, "optin").click()
        self.driver.find_element(By.ID, "first_name").send_keys('Cristina')
        self.driver.find_element(By.ID, "last_name").send_keys("DBSBFUYDBYBSAKLJ")
        self.driver.find_element(By.ID, "company").send_keys("dsbfiebaifhbeiahb")
        self.driver.find_element(By.ID, "address1").send_keys("dnsefcnswfcnw")
        self.driver.find_element(By.ID, "address2").send_keys("cjhsbdhvfbsh")
        self.driver.find_element(By.ID, "country").click()
        self.driver.find_element(By.CSS_SELECTOR, "#country > option:nth-child(5)")
        self.driver.find_element(By.ID, "state").send_keys("ndwbfdwbfdb")
        self.driver.find_element(By.ID, "zipcode").send_keys("1564521")
        self.driver.find_element(By.ID, "mobile_number").send_keys("451515701145754210546")
        self.driver.find_element(By.CSS_SELECTOR, "btn btn-default").click()

    def tearDown(self) -> None:
        self.driver.quit()



        
