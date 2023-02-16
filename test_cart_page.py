import logging

from pages.cart_page import CartPage


class TestCartPage:
    """Stores tests for cart page base functionality"""
    log = logging.getLogger("[CartPage]")

    def test_verify_cart_name_page(self, start_page, user):
        """
        - Pre-conditions:
                - Open start page
            - Steps:
                - Log in as user
                - Click on cart button
                - Verify cart page name
        """
        # Log in as a user
        things_page = start_page.log_in(user)

        # Click on cart button
        things_page.header.navigate_to_cart_page()

        # Verify cart page name
        cart_page = CartPage(things_page.driver)
        cart_page.verify_cart_name_page()
