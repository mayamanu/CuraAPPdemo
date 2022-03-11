from selenium.webdriver.common.by import By


class MakeAppoinment():
    def __init__(self,driver):
        self.driver=driver

    dropdown=(By.CSS_SELECTOR,("#combo_facility"))
    checkbox=(By.CSS_SELECTOR,(".checkbox-inline"))
    radiobuttons=(By.XPATH,('//input[@type="radio"]'))
    visitdata=(By.XPATH,("//input[@id='txt_visit_date']"))
    txtcomment=(By.CSS_SELECTOR,("#txt_comment"))
    bookbtn=(By.XPATH,("//button[@id='btn-book-appointment']"))
    title=(By.CSS_SELECTOR,("h2"))


    def dropdownf(self):
        return self.driver.find_element(*MakeAppoinment.dropdown)
    def checkboxf(self):
        return self.driver.find_element(*MakeAppoinment.checkbox)
    def radiobuttonsf(self):
        return self.driver.find_elements(*MakeAppoinment.radiobuttons)
    def visitdataf(self):
        return self.driver.find_element(*MakeAppoinment.visitdata)
    def txtcommentf(self):
        return self.driver.find_element(*MakeAppoinment.txtcomment)
    def bookbtnf(self):
        return self.driver.find_element(*MakeAppoinment.bookbtn)
    def gettitlef(self):
        return self.driver.find_element(*MakeAppoinment.title)


