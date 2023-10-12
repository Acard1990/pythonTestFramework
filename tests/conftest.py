# pytest configuration file -- fixtures etc
import pytest
from tests.api.data import RESTcountries
from clients.API_client import APIClient

@pytest.fixture(scope="session")
def api_client():
    client = APIClient(base_url=RESTcountries.BaseURL)
    return client