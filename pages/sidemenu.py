import logging

from constsnts.sidemenu import SideMenuConsts
from pages.base_page import BasePage
from pages.utils import log_wrapper


class SideMenu(BasePage):
    """Stores methods describes side menu actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = SideMenuConsts

        self.log = logging.getLogger("[Side menu]")

    @log_wrapper
    def log_out_by_side_menu(self):
        """Click on the button Log out from side menu"""
        self.click(self.const.LOG_OUT_XPATH)

        from pages.start_page import StartPage
        return StartPage(self.driver)
