from selenium.webdriver.common.by import By

class Home:
    
    def __init__(self, driver):
        self.driver = driver
        self.header = (By.CLASS_NAME, "logo-label")

    def navigateToHome(self):
        self.driver.get('https://demo.applitools.com/')

    def getHeaderVal(self):
        self.driver.get(*self.header.text)