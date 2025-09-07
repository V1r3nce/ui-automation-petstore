from selenium.common.exceptions import StaleElementReferenceException
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    url = "https://petstore.octoperf.com/actions/Catalog.action"
    # Locators

    button_go_to_auth = "//a[normalize-space()='Sign In' and contains(@href,'signonForm')]"
    button_go_to_fish = "//a[@href='/actions/Catalog.action?viewCategory=&categoryId=FISH']"


    # Getters

    def get_button_go_to_auth(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_go_to_auth)))

    def get_button_go_to_fish(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_go_to_fish)))


    # Actions

    def click_button_go_to_auth(self):
        self.get_button_go_to_auth().click()
        print("Click Button Go To Auth")

    def click_button_go_to_fish(self):
        if "signonForm" in self.driver.current_url:
            self.driver.get(self.url)

        wait = WebDriverWait(self.driver, 10)

        for attempt in range(2):
            try:
                el = wait.until(EC.element_to_be_clickable((By.XPATH, self.button_go_to_fish)))
                el.click()
                break
            except StaleElementReferenceException:
                time.sleep(0.2)
                if attempt == 1:
                    el = wait.until(EC.presence_of_element_located((By.XPATH, self.button_go_to_fish)))
                    self.driver.execute_script("arguments[0].click();", el)

        wait.until(EC.url_contains("categoryId=FISH"))
        print("Click Button Go To Fish")

    # Methods

    def go_to_auth(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.get_current_url()
        self.click_button_go_to_auth()

    def go_to_fish(self):
        self.get_current_url()
        self.click_button_go_to_fish()
