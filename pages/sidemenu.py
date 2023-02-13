import logging
from time import sleep

from constsnts.sidemenu import SideMenuConsts
from pages.base_page import BasePage
from pages.header import Header
from pages.start_page import StartPage


class SideMenu(BasePage):
    """Stores methods describes side menu actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = StartPage
        self.const = SideMenuConsts
        self.header = Header(self.driver)
        self.log = logging.getLogger("[Side menu]")

    def log_out_by_side_menu(self):
        """Click on the button Log out from side menu"""
        self.click(self.const.LOG_OUT_XPATH)
        sleep(2)
        from pages import start_page
        return start_page
