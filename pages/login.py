from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

class LoginPage:
    
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "log-in")
        self.auth_header = (By.CLASS_NAME, "auth-header")

    # def navigateToLogin(self):
    #     self.driver.get('https://demo.applitools.com/')

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()

    def assertLoginWithHeaderElement(self):
        try:
            self.driver.find_element(*self.auth_header.text)
            assert False, "The element should not exist, but it was found"
        except NoSuchElementException:
            assert True, "The element does not exist"



