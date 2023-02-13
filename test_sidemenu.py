import logging
from time import sleep


class TestSideMenu:
    """Stores tests for side menu base functionality"""
    log = logging.getLogger("[CartPage]")
    """
        - Steps:
            - Log in as user
            - Click on Logout
    """

    def test_log_out_by_side_menu(self, start_page):
        # Login as user
        things_page = start_page.log_in("standard_user", "secret_sauce")

        # Navigate to side menu
        things_page.header.navigate_to_side_menu()
        sleep(2)

        # Click on Logout
        things_page.header.side_menu.log_out_by_side_menu()
        self.log.info("Button Logout was clicked")
