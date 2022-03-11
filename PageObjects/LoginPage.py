from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self,driver):
        self.driver=driver

    username = (By.CSS_SELECTOR,("#txt-username"))
    password = (By.CSS_SELECTOR,("#txt-password"))
    loginbtn = (By.CSS_SELECTOR,("#btn-login"))

    def getUsername(self):
        return self.driver.find_element(*LoginPage.username)
    def getpasswd(self):
        return self.driver.find_element(*LoginPage.password)
    def getloginbtn(self):
        return self.driver.find_element(*LoginPage.loginbtn)










