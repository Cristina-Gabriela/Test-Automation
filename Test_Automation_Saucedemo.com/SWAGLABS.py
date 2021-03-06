import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class AutomationTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.saucedemo.com/")

    def test_automation(self):
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").click()
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("standard_user")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#password").click()
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_badge").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "continue-shopping").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "inventory_item_name").click()
        time.sleep(1)
        time.sleep(1)
        self.driver.find_element(By.ID, "back-to-products").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "inventory_item_name").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "inventory_item_name").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "back-to-products").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "product_sort_container").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "header_secondary_container").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "react-burger-cross-btn").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "remove-sauce-labs-bolt-t-shirt").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "remove-sauce-labs-fleece-jacket").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "remove-sauce-labs-onesie").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "remove-test.allthethings()-t-shirt-(red)").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "checkout").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "logout_sidebar_link").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "user-name").click()
        self.driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#password").click()
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()
        time.sleep(1)
        self.driver.back()
        self.driver.find_element(By.ID, "user-name").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "user-name").send_keys("problem_user")
        time.sleep(1)
        self.driver.find_element(By.ID, "password").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#item_4_title_link > div:nth-child(1)").click()
        time.sleep(1)
        self.driver.back()
        self.driver.find_element(By.CSS_SELECTOR, "#item_0_title_link > div:nth-child(1)").click()
        time.sleep(1)
        self.driver.back()
        self.driver.find_element(By.CSS_SELECTOR, "#item_1_title_link > div:nth-child(1)").click()
        time.sleep(1)
        self.driver.back()
        self.driver.find_element(By.CSS_SELECTOR, "#item_5_title_link > div:nth-child(1)").click()
        time.sleep(1)
        self.driver.back()
        self.driver.find_element(By.CSS_SELECTOR, "#item_3_title_link > div:nth-child(1)").click()
        time.sleep(1)
        self.driver.back()
        self.driver.find_element(By.CSS_SELECTOR, "#item_2_title_link > div:nth-child(1)").click()
        time.sleep(1)
        self.driver.back()
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "about_sidebar_link").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "nav-image-link").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#onetrust-accept-btn-handler").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".display-horizontal-on-mobile > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)").click()
        time.sleep(1)
        self.driver.back()
        self.driver.find_element(By.CSS_SELECTOR,
                                 ".display-horizontal-on-mobile > ul:nth-child(1) > li:nth-child(2) > a:nth-child(1)").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "FirstName").click()
        self.driver.find_element(By.ID, "FirstName").send_keys("Cristina")
        time.sleep(1)
        self.driver.find_element(By.ID, "LastName").click()
        self.driver.find_element(By.ID, "LastName").send_keys("Raileanu")
        time.sleep(1)
        self.driver.find_element(By.ID, "Company").click()
        self.driver.find_element(By.ID, "Company").send_keys("SauceLabs")
        time.sleep(1)
        self.driver.find_element(By.ID, "Email").click()
        self.driver.find_element(By.ID, "Email").send_keys("raileanu.cristina91@gmail.com")
        time.sleep(1)
        self.driver.find_element(By.ID, "Country").click()
        self.driver.find_element(By.ID, "Country").send_keys("Romania")
        time.sleep(1)
        self.driver.find_element(By.NAME, "Country").get_attribute("value=Romania")
        time.sleep(1)
        self.driver.find_element(By.ID, "Phone").send_keys("25854165415151")
        time.sleep(1)
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        time.sleep(1)
        self.driver.back()
        time.sleep(1)
        self.driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "logout_sidebar_link").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").click()
        self.driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys("performance_glitch_user")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#password").click()
        self.driver.find_element(By.CSS_SELECTOR, "#password").send_keys("secret_sauce")
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#login-button").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bolt-t-shirt").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-onesie").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-bike-light").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-sauce-labs-fleece-jacket").click()
        time.sleep(1)
        self.driver.find_element(By.CSS_SELECTOR, "#add-to-cart-test\.allthethings\(\)-t-shirt-\(red\)").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "inventory_item_name").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "back-to-products").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "remove-sauce-labs-onesie").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "remove-sauce-labs-bike-light").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "remove-sauce-labs-fleece-jacket").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "remove-test.allthethings()-t-shirt-(red)").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "remove-sauce-labs-backpack").click()
        time.sleep(1)
        self.driver.find_element(By.ID, "remove-sauce-labs-bolt-t-shirt").click()
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()
