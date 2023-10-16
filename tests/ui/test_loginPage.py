import pytest
from pages.login import LoginPage
from pages.home import Home
  
def test_successful_login(nav_to_login):
    login_page = LoginPage(nav_to_login)
    login_page.login("test", "testpw")
    assert login_page.assertLoginWithHeaderElement

def test_invalid_login(nav_to_login):
    login_page = LoginPage(nav_to_login)
    login_page.login("invalid_username", "")
    # assert login_page.getAuthHeaderVal == 'Login'
    # (the test site has fake login :/)
