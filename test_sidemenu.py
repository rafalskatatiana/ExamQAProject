import logging


class TestSideMenu:
    """Stores tests for side menu base functionality"""
    log = logging.getLogger("[SideMenu]")

    def test_log_out_by_side_menu(self, start_page, user):
        """
            - Pre-conditions:
                - Open start page
            - Steps:
                - Login as a user
                - Click on the icon side menu
                -  Click on Logout
                -Verify login page by login button
         """

        # Login as user
        things_page = start_page.log_in(user)

        # Navigate to side menu
        things_page.header.navigate_to_side_menu()

        # Click on Logout
        things_page.header.side_menu.log_out_by_side_menu()

        # Verify login page by login button
        start_page.verify_sign_in()
