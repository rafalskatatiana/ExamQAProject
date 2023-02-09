import logging
from time import sleep

import pytest
from selenium import webdriver

from constsnts.base import BaseConstants
from pages.start_page import StartPage


class TestThingsPage:
    """Stores methods describes things page actions"""
    log = logging.getLogger("[ThingsPage]")

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

    def test_add_to_cart(self, start_page):
        """
            - Steps:
                - Log in as user
                - Click on Add to cart button
                - Verify that button name is changing
        """

        # Log in as a user
        things_page = start_page.log_in("standard_user", "secret_sauce")

        # Click on Add to cart button
        things_page.add_thing_to_box()
        self.log.info("Button was clicked")
        sleep(1)

        # Verify that button name is changing
        things_page.verify_name_of_button()
        self.log.info("Button name was verified")
        sleep(1)
