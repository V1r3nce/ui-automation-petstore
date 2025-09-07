from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base

class Login_page(Base):


    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    log_in = "//input[@name='username']"
    pass_word = "//input[@name='password']"
    button_auth = "//input[@name='signon']"
    text_register = "//a[@href='/actions/Account.action?newAccountForm=' and normalize-space()='Register Now!']"

    # Getters

    def get_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.log_in)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.pass_word)))

    def get_button_auth(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_auth)))

    def get_text_register(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.text_register)))


    # Actions

    def input_login(self, login):
        self.get_login().clear()
        self.get_login().send_keys(login)
        print("Input Login")

    def input_password(self, password):
        self.get_password().clear()
        self.get_password().send_keys(password)
        print("Input Password")

    def click_button_auth(self):
        self.get_button_auth().click()
        print("Click Button Auth")



    # Methods

    def Log_In(self):
        self.get_current_url()
        self.assert_word(self.get_text_register(), "Register Now!")
        self.input_login("denis.qa")
        self.input_password("Krasnova44")
        self.click_button_auth()

