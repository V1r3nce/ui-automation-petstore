from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Detailed_info_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    button_add_product_cart = "//a[@href='/actions/Cart.action?addItemToCart=&workingItemId=EST-1']"

    # Getters

    def get_button_add_product_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_add_product_cart)))

    # Actions

    def click_button_add_product_cart(self):
        self.get_button_add_product_cart().click()
        print("Add Product in Cart")

    # Methods

    def add_product_in_cart(self):
        self.get_current_url()
        self.click_button_add_product_cart()