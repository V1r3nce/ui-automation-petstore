from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Cart_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    button_proceed_to_chekout = "//a[@href='/actions/Order.action?newOrderForm=']"

    # Getters

    def get_button_proceed_to_chekout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_proceed_to_chekout)))

    # Actions

    def click_button_proceed_to_chekout(self):
        self.get_button_proceed_to_chekout().click()
        print("Go to Proceed to chekout")

    # Methods

    def proceed_to_chekout(self):
        self.get_current_url()
        self.click_button_proceed_to_chekout()