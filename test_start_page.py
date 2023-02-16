import logging


class TestStartPage:
    """Stores tests for start page base functionality"""
    log = logging.getLogger("[StartPage]")

    def test_log_in_user(self, start_page, user):
        """
            - Pre-conditions:
                - Open start page
            - Steps:
                - Fill login
                - Fill password
                - Click on the button Login
                - Verify login page name
        """
        # Login as a user
        things_page = start_page.log_in(user)

        # Check user to login page
        things_page.verify_name_page()
