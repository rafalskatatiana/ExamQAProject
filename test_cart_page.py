import logging
from time import sleep

from pages import cart_page


class TestCartPage:
    """Stores tests for start cart base functionality"""
    log = logging.getLogger("[CartPage]")

    def test_verify_cart_name_page(self, start_page):
        """
                 - Steps:
                     - Log in as user
                     - Click on cart button
                     - Verify cart page name
             """
        # Log in as a user
        things_page = start_page.log_in("standard_user", "secret_sauce")

        # Click on cart button
        things_page.header.navigate_to_cart_page()
        sleep(2)

        # Verify cart page name
        cart_page.verify_cart_name_page()
