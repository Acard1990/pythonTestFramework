from selenium.webdriver.common.by import By

class Home:
    
    def __init__(self, driver):
        self.driver = driver
        self.header = (By.CLASS_NAME, "logo-label")

    def getHeaderVal(self):
        self.driver.get(*self.header.text)