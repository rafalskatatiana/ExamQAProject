import logging


class TestThingsPage:
    """Stores methods describes things page actions"""
    log = logging.getLogger("[ThingsPage]")

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

        # Verify that button name is changing
        things_page.verify_name_of_button()
        self.log.info("Button name was verified")

    def test_open_cart_page(self, start_page):
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
        self.log.info("Cart button was clicked")
