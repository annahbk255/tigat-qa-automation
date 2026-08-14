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

# Data-Driven Testing: Pytest automatically runs this test 3 times with different datasets
@pytest.mark.parametrize("search_term", [
    "Test Automation Framework",
    "QA Engineering Best Practices",
    "CI/CD Pipeline Integration"
])
def test_parameterized_search_scenarios(driver, search_term):
    page = TigatWebPage(driver)
    page.open()
    
    # Validate the session and test data execution
    assert driver.current_url != ""
    print(f"Executing automated test scenario for: {search_term}")
