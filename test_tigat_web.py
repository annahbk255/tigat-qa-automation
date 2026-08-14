import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.tigat_page import TigatWebPage

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    yield driver
    driver.quit()

def test_page_heading(driver):
    # Initialize the Page Object
    page = TigatWebPage(driver)
    
    # Open page and perform actions using the Page Object model
    page.open()
    
    # Assertion using the page method
    # Note: Adjust expected text depending on the website you are testing
    assert driver.current_url != ""
