from selenium.webdriver.common.by import By


class HomePage():
    def __init__(self,driver):
        self.driver=driver

    menutoggle=(By.CSS_SELECTOR,("#menu-toggle"))
    login=(By.LINK_TEXT,("Login"))

    def menutoggled(self):
        return self.driver.find_element(*HomePage.menutoggle)
    def logininto(self):
        return self.driver.find_element(*HomePage.login)



