from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from base.base_class import Base
from selenium.common.exceptions import StaleElementReferenceException
import time


class Total_check_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    button_return_menu = "//a[@href='/actions/Catalog.action']"


    # Getters

    def get_button_return_menu(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_return_menu)))


    # Actions

    def click_button_return_menu(self):
        self.get_button_return_menu().click()
        print("Click Button Return To Menu")


    # Methods

    def finish_check(self):
        self.get_current_url()
        self.get_screenshot()
        self.click_button_return_menu()
