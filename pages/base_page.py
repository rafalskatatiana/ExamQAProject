from selenium.webdriver.common.by import By


class BasePage:
    """Describe base methods for the website"""

    def __init__(self, driver):
        self.driver = driver

    def fill_field(self, xpath, value):
        """"Fill fields using value"""
        field = self.driver.find_element(by=By.XPATH, value=xpath)
        field.clear()
        field.send_keys(value)

    def click(self, xpath):
        """Find and click on the button by provided xpath"""
        element = self.driver.find_element(by=By.XPATH, value=xpath)
        element.click()

    def compare_element_text(self, xpath, text):
        """Compare element text"""
        element = self.driver.find_element(by=By.XPATH, value=xpath)
        return element.text == text
