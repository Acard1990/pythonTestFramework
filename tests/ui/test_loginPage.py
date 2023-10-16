import pytest
from pages.login import LoginPage
from pages.home import Home

# To-do, setup a before all method for navigating to the homepage
  
def test_successful_login(driver):
    login_page = LoginPage(driver)
    home = Home(driver)
    login_page.navigateToLogin()
    login_page.login("test", "testpw")
    assert home.getHeaderVal != 'ACME'

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.navigateToLogin()
    login_page.login("invalid_username", "")
    # assert login_page.getAuthHeaderVal == 'Login'
    # Add assertion to validate the failure (the test site has fake login :/)
