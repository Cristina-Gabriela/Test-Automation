from basepage import BasePage
from selenium.webdriver.common.by import By


class HomePage(BasePage):
    AUTOCOMPLETE = (By.LINK_TEXT, "Autocomplete")
    BUTTONS = (By.LINK_TEXT, "Buttons")
    CHECKBOX = (By.LINK_TEXT, "Checkbox")
    DATEPICKER = (By.LINK_TEXT, "Date picker")
    DRAG_AND_DROP = (By.LINK_TEXT, "Drag and Drop")
    DROPDOWN = (By.LINK_TEXT, "Dropdown")
    ENABLE_AND_DISABLED_ELEMENTS = (By.LINK_TEXT, "Enable and Disabled Elements")
    FILE_UPLOAD = (By.LINK_TEXT, "File Upload")
    FILE_DOWNLOAD = (By.LINK_TEXT, "File download")
    KEY_AND_MOUSE_PRESS = (By.LINK_TEXT, "Key and Mouse Press")
    MODAL = (By.LINK_TEXT, "Modal")
    PAGE_SCROLL = (By.LINK_TEXT, "Page Scroll")
    RADIO_BUTTON = (By.LINK_TEXT, "Radio Button")
    SWITCH_WINDOW = (By.LINK_TEXT, "Switch window")
    COMPLETE_WEB_FORM = (By.LINK_TEXT, "Complete Web Form")

    def click_on_autocomplete(self):
        print("We'll go to page autocomplete.")
        self._driver.find_element(*self.AUTOCOMPLETE).click()

        