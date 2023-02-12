import logging
from time import sleep

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
        from pages import cart_page
        return cart_page

    def navigate_to_side_menu(self):
        """Navigate to side menu via header button"""
        self.click(self.const.SIDE_MENU_BUTTON_XPATH)
        sleep(2)
        from pages import sidemenu
        return sidemenu
