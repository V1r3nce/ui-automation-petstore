import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.cart_page import Cart_page
from pages.chekout_page import Checkout_page
from pages.confirm_page import Confirm_page
from pages.detailed_product_information_page import Detailed_info_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.select_product_page import Select_product_page
from pages.total_chek_page import Total_check_page


def test_buy_product():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ['enable-logging'])
    options.add_experimental_option("detach", True)
    options.add_argument("--guest")
    options.add_argument("--disable-extensions")
    service = Service("C:\\Users\\Andrey\\PycharmProjects\\resourse\\chromedriver.exe")
    driver = webdriver.Chrome(options=options, service=service)

    print('Start Test 1')

    mp = Main_page(driver)
    mp.go_to_auth()

    login = Login_page(driver)
    login.Log_In()

    mp.go_to_fish()

    spp = Select_product_page(driver)
    spp.go_to_info_product()

    dpip = Detailed_info_page(driver)
    dpip.add_product_in_cart()

    cartp = Cart_page(driver)
    cartp.proceed_to_chekout()

    checkp = Checkout_page(driver)
    checkp.input_chekout()

    confirmp = Confirm_page(driver)
    confirmp.confirm_check()

    tcp = Total_check_page(driver)
    tcp.finish_check()

    print("Stop Test 1")




