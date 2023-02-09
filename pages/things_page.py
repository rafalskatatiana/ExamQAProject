import logging
from time import sleep

from constsnts.things_page import ThingsPageConst
from pages.base_page import BasePage
from pages.start_page import StartPage


class ThingsPage(BasePage):
    """Stores methods describes hello page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = StartPage
        self.const = ThingsPageConst

        self.log = logging.getLogger("[ThingsPage]")

    def verify_current_page(self, current_url):
        """Verify that user is routed to login page"""
        self.verify_current_page(current_url=self.const.THINGS_PAGE_URL)
        assert current_url

    def add_thing_to_box(self):
        """Click on the button Add to cart"""
        self.click(self.const.ADD_TO_CART_XPATH)

    def verify_name_of_button(self):
        """Verify that button changed name"""
        assert self.compare_element_text(xpath=self.const.VERIFY_CHANGE_NAME_BUTTON_XPATH,
                                         text=self.const.VERIFY_CHANGE_NAME_BUTTON_TEXT)
        sleep(2)
