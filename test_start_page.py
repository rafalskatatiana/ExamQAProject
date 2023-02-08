import logging
import random
import string
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

"""Tests related to start page"""


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

    def test_start_page(self):
        """
            - Pre-conditions:
                - Open start page
            - Steps:
                - Fill login
                - Fill password
                - Click on the button Login
                - Verify login page
        """
        #  Open start page
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

        # Check user is routed to login page
        current_url = driver.current_url
        assert current_url == "https://www.saucedemo.com/inventory.html"
        sleep(1)

        driver.close()

    def test_choose_thing(self):
        """
            - Pre-conditions:
                - Open start page
            - Steps:
                - Fill fields login, password
                - Click on the button Login
                - Choose a things
                - Verify the name of the thing
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

        # Choose a thing
        choose_thing = driver.find_element(by=By.XPATH, value=".//a[@id='item_4_title_link']")
        choose_thing.click()
        sleep(1)

        # Verify the name of the thing
        name_of_thing = driver.find_element(by=By.XPATH, value=".//div[@class='inventory_details_name large_size']")
        assert name_of_thing.text == "Sauce Labs Backpack"
        sleep(2)
        driver.close()

    def test_add_thing_to_card(self):
        """
            - Pre-conditions:
                - Open start page
            - Steps:
                - Fill fields login, password
                - Click on the button Login
                - Choose a thing
                - Click on Add to cart button
                - Verify that button name is changing
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

        # Choose a thing
        choose_thing = driver.find_element(by=By.XPATH, value=".//a[@id='item_4_title_link']")
        choose_thing.click()
        sleep(1)

        # Add to cart
        add_cart_button = driver.find_element(by=By.XPATH,
                                              value=".//button[@class='btn btn_primary btn_small btn_inventory']")
        add_cart_button.click()
        sleep(1)

        # Verify that button name is changing
        remove_button = driver.find_element(by=By.XPATH,
                                            value=".//button[@class='btn btn_secondary btn_small btn_inventory'][text()='Remove']")
        assert remove_button.text == "REMOVE"
        sleep(1)
        driver.close()

    def test_add_one_more_thing(self):
        """
            - Pre-conditions:
                - Open start page
            - Steps:
                - Fill fields login, password
                - Click on the button Login
                - Click on the box icon
                - Verify page name
                - Click on the Continue shopping
                - Choose one more thing and clic on add to card
                - Click on the box icon
                - Verify the second name of the thing
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

        # Verify page name
        page_name = driver.find_element(by=By.XPATH, value=".//span[@class='title'][text()='Your Cart']")
        assert page_name.text == "YOUR CART"

        # Click on the Continue shopping
        continue_shopping_button = driver.find_element(by=By.XPATH,
                                                       value=".//button[@class='btn btn_secondary back btn_medium']")
        continue_shopping_button.click()
        sleep(1)

        # Choose one more thing
        choose_second_thing = driver.find_element(by=By.XPATH,
                                                  value=".//div[@class='inventory_item_name'][text("
                                                        ")='Test.allTheThings() T-Shirt (Red)']")
        choose_second_thing.click()
        sleep(1)

        # Add to cart
        add_cart_button = driver.find_element(by=By.XPATH,
                                              value=".//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")
        add_cart_button.click()
        sleep(1)

        # Click on the box icon
        box_icon_button = driver.find_element(by=By.XPATH, value=".//a[@class='shopping_cart_link']")
        box_icon_button.click()
        sleep(2)

        # Verify the second name of the thing
        name_of_second_thing = driver.find_element(by=By.XPATH,
                                                   value=".//div[@class='inventory_item_name'][text("
                                                         ")='Test.allTheThings() T-Shirt (Red)']")
        assert name_of_second_thing.text == "Test.allTheThings() T-Shirt (Red)"
        sleep(2)
        driver.close()

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

        driver.close()
