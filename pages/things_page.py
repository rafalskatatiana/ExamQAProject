import logging

from constsnts.things_page import ThingsPageConst
from pages.base_page import BasePage
from pages.header import Header
from pages.start_page import StartPage
from pages.utils import log_wrapper, wait_until_ok


class ThingsPage(BasePage):
    """Stores methods describes things page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = StartPage
        self.const = ThingsPageConst
        self.header = Header(self.driver)
        self.log = logging.getLogger("[ThingsPage]")

    @log_wrapper
    def verify_name_page(self):
        """Verify that user is routed to login page"""
        assert self.compare_element_text(xpath=self.const.THINGS_PAGE_XPATH, text=self.const.THINGS_PAGE_TEXT)

    @wait_until_ok(timeout=10, period=1)
    @log_wrapper
    def add_thing_to_box(self):
        """Click on the button Add to cart"""
        self.click(self.const.ADD_TO_CART_XPATH)

    @log_wrapper
    def verify_name_of_button(self):
        """Verify that button changed name"""
        assert self.compare_element_text(xpath=self.const.VERIFY_CHANGE_NAME_BUTTON_XPATH,
                                         text=self.const.VERIFY_CHANGE_NAME_BUTTON_TEXT)
