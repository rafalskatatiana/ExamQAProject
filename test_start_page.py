import logging
import random
import string
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from constsnts.base import BaseConstants
from pages.start_page import StartPage


class TestStartPage:
    """Stores tests for start page base functionality"""
    log = logging.getLogger("[StartPage]")

    @staticmethod
    def random_num():
        """Generate random number"""
        return str(random.randint(11111, 99999))

    @staticmethod
    def random_str(length=5):
        """Generate randomstring"""
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))

    @pytest.fixture()
    def driver(self):
        """Create selenium driver"""
        driver = webdriver.Chrome(executable_path=BaseConstants.DRIVER_PATH)
        yield driver
        driver.close()

    @pytest.fixture()
    def start_page(self, driver):
        """Create start page object"""
        driver.get("https://www.saucedemo.com/")
        return StartPage(driver)

    def test_log_in_user(self, start_page):
        """
            - Pre-conditions:
                - Open start page
            - Steps:
                - Fill login
                - Fill password
                - Click on the button Login
                - Verify login page
        """
        # Login as a user
        things_page = start_page.log_in("standard_user", "secret_sauce")
        self.log.info("User is logged")

        # Check user is routed to login page
        things_page.verify_current_page()

    def test_checkout_your_information(self):
        """
            - Pre-conditions:
                - Open start page
            - Steps:
                - Fill fields login, password
                - Click on the button Login
                - Click on the box icon
                - Click on Check Out
                - Fill fields First name, Last name, zip
                - Click on Continue
                - Verify page name, Payment Information
        """
        # Open start page
        driver = webdriver.Chrome(executable_path="chromedriver.exe ")
        driver.get("https://www.saucedemo.com/")
        sleep(1)
        # Fill login
        login_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Username']")
        login_field.clear()
        login_field.send_keys("standard_user")
        sleep(1)

        # Fill password
        password_field = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Password']")
        password_field.clear()
        password_field.send_keys("secret_sauce")
        sleep(1)

        # Click on the button Login
        login_button = driver.find_element(by=By.XPATH, value=".//input[@class='submit-button btn_action']")
        login_button.click()
        sleep(1)
        # Click on the box icon
        box_icon_button = driver.find_element(by=By.XPATH, value=".//a[@class='shopping_cart_link']")
        box_icon_button.click()
        sleep(2)

        # Click on Check Out
        checkout_button = driver.find_element(by=By.XPATH, value=".//button[@id='checkout']")
        checkout_button.click()
        sleep(2)

        # Fill fields First name, Last name, zip
        firstname_value = f"{self.random_str()}{self.random_num}"
        firstname = driver.find_element(by=By.XPATH, value=".//input[@placeholder='First Name']")
        firstname.clear()
        firstname.send_keys(firstname_value)
        sleep(1)

        lastname_value = f"{self.random_str()}{self.random_num}"
        lastname = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Last Name']")
        lastname.clear()
        lastname.send_keys(lastname_value)
        sleep(1)

        zipcode_value = f"{self.random_num}"
        zipcode = driver.find_element(by=By.XPATH, value=".//input[@placeholder='Zip/Postal Code']")
        zipcode.clear()
        zipcode.send_keys(zipcode_value)
        sleep(1)

        # Click on Continue
        continue_button = driver.find_element(by=By.XPATH,
                                              value=".//input[@class='submit-button btn btn_primary cart_button btn_action']")
        continue_button.click()
        sleep(2)

        # Verify page name
        page_checkout = driver.find_element(by=By.XPATH, value=".//span[@class='title'][text()='Checkout: Overview']")
        assert page_checkout.text == "CHECKOUT: OVERVIEW"
        # Verify Payment Information
        payment_information = driver.find_element(by=By.XPATH,
                                                  value=".//div[@class='summary_value_label'][text()='SauceCard #31337']")
        assert payment_information.text == "SauceCard #31337"
        sleep(2)
