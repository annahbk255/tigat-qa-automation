from selenium.webdriver.common.by import By
from .base_page import BasePage

class TigatWebPage(BasePage):
    # Define your element locators here
    HEADING_LOCATOR = (By.TAG_NAME, "h1")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://example.com"  # Replace with your target URL if needed

    def open(self):
        self.driver.get(self.url)

    def get_heading_text(self):
        return self.find_element(self.HEADING_LOCATOR).text
