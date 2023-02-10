import logging

from constsnts.header import HeaderConsts
from pages.base_page import BasePage


class Header(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.const = HeaderConsts
        self.log = logging.getLogger("[Header]")

    def navigate_to_cart_page(self):
        """Navigate to cart page via header button"""
        self.click(self.const.CART_BUTTON_XPATH)
        from pages.cart_page import CartPage
        return CartPage(self.driver)
