import logging

from constsnts.cart_page import CartPageConsts
from pages.base_page import BasePage
from pages.header import Header
from pages.utils import log_wrapper


class CartPage(BasePage):
    """Stores methods describes cart page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = CartPageConsts
        self.header = Header(self.driver)
        self.log = logging.getLogger("[ThingsPage]")

    @log_wrapper
    def verify_cart_name_page(self):
        """Verify that user is routed to login page"""
        assert self.compare_element_text(xpath=self.const.CART_PAGE_NAME_XPATH, text=self.const.CART_PAGE_NAME_TEXT)
        self.log.info("User routed to login page")
