from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import Keys
from base.base_class import Base
from selenium.common.exceptions import StaleElementReferenceException
import time


class Checkout_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    card_type = "//select[@name='order.cardType']"
    card_number = "//input[@name='order.creditCard']"
    expiry_date = "//input[@name='order.expiryDate']"
    button_continue = "//input[@name='newOrder']"


    # Getters

    def get_card_type(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.card_type)))

    def get_card_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.card_number)))

    def get_expiry_date(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.expiry_date)))

    def get_button_continue(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_continue)))

    # Actions

    def click_card_type(self):
        self.get_card_type().click()
        self.get_card_type().send_keys(Keys.ARROW_DOWN + Keys.ENTER)
        print("Choose card type Mastercard")

    def input_card_number(self, cardnumber):
        self.get_card_number().clear()
        self.get_card_number().send_keys(cardnumber)
        print("Input card_number")

    def input_expiry_date(self, expirydate):
        self.get_expiry_date().clear()
        self.get_expiry_date().send_keys(expirydate)
        print("Input expiry date")

    def click_button_continue(self):
        self.get_button_continue().click()
        print("Click Button Continue")


    # Methods

    def input_chekout(self):
        self.get_current_url()
        self.click_card_type()
        self.input_card_number("123 1234 1234 1234")
        self.input_expiry_date("99/99")
        self.click_button_continue()