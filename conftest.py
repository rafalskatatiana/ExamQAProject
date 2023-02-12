import pytest
from selenium import webdriver

from constsnts.base import BaseConstants
from pages.start_page import StartPage


@pytest.fixture()
def driver():
    """Create selenium driver"""
    driver = webdriver.Chrome(executable_path=BaseConstants.DRIVER_PATH)
    yield driver
    driver.close()


@pytest.fixture()
def start_page(driver):
    """Create start page object"""
    driver.get(BaseConstants.URL)
    return StartPage(driver)