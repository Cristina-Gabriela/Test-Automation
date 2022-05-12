import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager


# print(driver)
# driver.maximize_window()

class Google(unittest.TestCase):
    def setUp(self):  # daca este cu self pot sa il folosesc si in celelalte functii.
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get("https://www.google.com/")
        time.sleep(4)

    def test(self):
        button = (By.ID, 'L2AGLb')
        self.driver.find_element(*button).click()
        # time.sleep(4)

        cautare_google_btn = self.driver.find_element(By.CLASS_NAME, "gNO89b")

        cautare_google_value = cautare_google_btn.get_attribute("value")
        self.assertEqual(cautare_google_value, "Căutare Google", "Error")
        self.assertIn(cautare_google_value, ['abc', 'CD', 'Căutare Google'], "ERROR ")

        ma_simt_norocos_btn = self.driver.find_element(By.CLASS_NAME, "RNmpXc")
        # y = abc.get_attribute("Mă simt norocos")
        ma_simt_norocos_value = ma_simt_norocos_btn.get_attribute("value")
        # print(y)
        self.assertEqual(ma_simt_norocos_value, "Mă simt norocos", "ERROR")

        cautare_google_aria_label_value = cautare_google_btn.get_attribute("aria-label")
        cautare_google_name_value = cautare_google_btn.get_attribute("name")
        cautare_google_role_value = cautare_google_btn.get_attribute("role")
        cautare_google_tabindex_value = cautare_google_btn.get_attribute("tabindex")
        cautare_google_type_value = cautare_google_btn.get_attribute("type")
        cautare_google_data_ved_value = cautare_google_btn.get_attribute("data-ved")
        dict = {
            "aria-label": cautare_google_aria_label_value,
            "name": cautare_google_name_value,
            "role": cautare_google_role_value,
            "tabindex": cautare_google_tabindex_value,
            "type": cautare_google_type_value,
            "data-ved": cautare_google_data_ved_value
        }
        print(dict)

        # class ="gNO89b" value="Căutare Google"
        # aria-label="Căutare Google"
        #
        # name = "btnK"
        # role = "button"
        # tabindex = "0"
        # type = "submit"
        # data - ved = "0ahUKEwjU8Nq98OX2AhVS6qQKHe2bBawQ4dUDCAs" >

        Enter_information_box = self.driver.find_element(By.CLASS_NAME, "gLFyf")
        Enter_information_box.send_keys("ujct6ywujse kjsjhu")

        # time.sleep(3)
        # Enter_information_box.clear()

        # time.sleep(3)

        # self.driver.find_element(By.CLASS_NAME, "gLFyf").clear()
        # print(Enter_information_box)

        self.driver.get("http://formy-project.herokuapp.com/checkbox")
        checkbox_one = self.driver.find_element(By.ID, "checkbox-1")
        checkbox_one.click()
        time.sleep(2)

        is_selected = checkbox_one.is_selected()
        self.assertEqual(is_selected, True, "Error alabalac")

        def tearDown(self):
            self.driver.quit()




