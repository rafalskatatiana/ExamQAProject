import logging
from time import sleep

from constsnts.header import HeaderConsts
from pages.base_page import BasePage
from pages.sidemenu import SideMenu


class Header(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.const = HeaderConsts
        self.side_menu = SideMenu(self.driver)
        self.log = logging.getLogger("[Header]")

    def navigate_to_cart_page(self):
        """Navigate to cart page via header button"""
        self.click(self.const.CART_BUTTON_XPATH)
        sleep(1)
        from pages.cart_page import CartPage
        return CartPage(self.driver)

    def navigate_to_side_menu(self):
        """Navigate to side menu via header button"""
        self.click(self.const.SIDE_MENU_BUTTON_XPATH)
        sleep(2)
        from pages.sidemenu import SideMenu
        return SideMenu(self.driver)
