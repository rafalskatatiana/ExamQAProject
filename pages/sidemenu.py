import logging
from time import sleep

from constsnts.sidemenu import SideMenuConsts
from pages.base_page import BasePage


class SideMenu(BasePage):
    """Stores methods describes side menu actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = SideMenuConsts

        self.log = logging.getLogger("[Side menu]")

    def log_out_by_side_menu(self):
        """Click on the button Log out from side menu"""
        self.click(self.const.LOG_OUT_XPATH)
        sleep(2)

        from pages.start_page import StartPage
        return StartPage(self.driver)
