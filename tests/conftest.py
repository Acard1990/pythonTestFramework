# pytest configuration file -- fixtures etc
import pytest
from selenium import webdriver
from tests.api.data import RESTcountries
from clients.API_client import APIClient

@pytest.fixture(scope="session")
def api_client():
    client = APIClient(base_url=RESTcountries.BaseURL)
    return client

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()