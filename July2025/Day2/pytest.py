from selenium import webdriver
import pytest

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_google_search(driver):
    driver.get("https://google.com")
    assert "Google" in driver.title
