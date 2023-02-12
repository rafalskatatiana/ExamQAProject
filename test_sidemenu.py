import logging


class TestSideMenu:
    """Stores tests for side menu base functionality"""
    log = logging.getLogger("[CartPage]")

    def test_log_out_by_side_menu(self, start_page):
        things_page = start_page.log_in("standard_user", "secret_sauce")

        things_page.header.navigate_to_side_menu()

        sidemenu.log_out_by_side_menu()
