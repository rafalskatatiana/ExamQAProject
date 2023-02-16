import logging

from constsnts.start_page import StartPageConst
from pages.base_page import BasePage
from pages.utils import log_wrapper


class StartPage(BasePage):
    """Stores methods describes start page actions"""

    def __init__(self, driver):
        super().__init__(driver)
        self.const = StartPageConst
        self.log = logging.getLogger("[StartPage]")

    @log_wrapper
    def log_in(self, user):
        """Log in using provided value"""

        # Fill login
        self.fill_field(xpath=self.const.LOG_IN_USERNAME_FIELD_XPATH, value=user.username)
        self.log.debug("Username field was filled")

        # Fill password
        self.fill_field(xpath=self.const.LOG_IN_PASSWORD_FIELD_XPATH, value=user.password)
        self.log.debug("Password field was filled")

        # Click on the button Login
        self.click(xpath=self.const.LOG_IN_BUTTON_XPATH)
        self.log.debug("Button was clicked")

        from pages.things_page import ThingsPage
        return ThingsPage(self.driver)

    @log_wrapper
    def verify_sign_in(self):
        """Verify login button in start page"""
        assert self.is_element_exists(xpath=self.const.LOG_IN_BUTTON_XPATH)
