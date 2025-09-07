from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Select_product_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    product_angelfish = "//a[@href='/actions/Catalog.action?viewProduct=&productId=FI-SW-01']"

    # Getters

    def get_product_angelfish(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_angelfish)))

    # Actions

    def click_product_angelfish(self):
        self.get_product_angelfish().click()
        print("Click Select Product")

    # Methods

    def go_to_info_product(self):
        self.get_current_url()
        self.click_product_angelfish()
