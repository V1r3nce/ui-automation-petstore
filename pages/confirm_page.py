from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from base.base_class import Base
from selenium.common.exceptions import StaleElementReferenceException
import time


class Confirm_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    button_confirm = "//a[@href='/actions/Order.action?newOrder=&confirmed=true']"


    # Getters

    def get_button_confirm(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_confirm)))


    # Actions

    def click_button_confirm(self):
        self.get_button_confirm().click()
        print("Click Button Confirm")


    # Methods

    def confirm_check(self):
        self.get_current_url()
        self.click_button_confirm()
