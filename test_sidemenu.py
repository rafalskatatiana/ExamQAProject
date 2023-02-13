import logging


class TestSideMenu:
    """Stores tests for side menu base functionality"""
    log = logging.getLogger("[SideMenu]")

    def test_log_out_by_side_menu(self, start_page):
        """
            - Pre-conditions:
                - Open start page
            - Steps:
                - Login as a user
                - Click on the icon side menu
                -  Click on Logout
         """

        # Login as user
        things_page = start_page.log_in("standard_user", "secret_sauce")
        self.log.info("User was logged")

        # Navigate to side menu
        things_page.header.navigate_to_side_menu()

        # Click on Logout
        things_page.header.side_menu.log_out_by_side_menu()
        self.log.info("Button Logout was clicked")
