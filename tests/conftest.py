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
def nav_to_login():
    driver = webdriver.Chrome()
    driver.get('https://demo.applitools.com/')
    yield driver
    driver.quit()

@pytest.fixture
def nav_to_home():
    driver = webdriver.Chrome()
    driver.get('https://demo.applitools.com/app.html')
    yield driver
    driver.quit()