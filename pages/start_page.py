import logging
from time import sleep

from constsnts.start_page import StartPageConst
from pages.base_page import BasePage


class StartPage(BasePage):
    """Stores methods describes start page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = StartPageConst
        self.log = logging.getLogger("[StartPage]")

    def log_in(self, username, password):
        """Log in using provided value"""

        # Fill login
        self.fill_field(xpath=self.const.LOG_IN_USERNAME_FIELD_XPATH, value=username)
        self.log.debug("Username field was filled")

        # Fill password
        self.fill_field(xpath=self.const.LOG_IN_PASSWORD_FIELD_XPATH, value=password)
        self.log.debug("Password field was filled")
        sleep(1)

        # Click on the button Login
        self.click(xpath=self.const.LOG_IN_BUTTON_XPATH)
        self.log.debug("Button was clicked")
        sleep(1)

        from pages.things_page import ThingsPage
        return ThingsPage(self.driver)
