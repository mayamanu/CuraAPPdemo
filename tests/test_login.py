
#Homepage
import pytest

from Data.GetData import LoginPageData
from PageObjects.HomePage import HomePage
from PageObjects.LoginPage import LoginPage
from PageObjects.MakeAppoinmentPage import MakeAppoinment
from utilities.BaseClass import BaseClass


class TestLogin(BaseClass):
    def test_login(self,getData):#calling ficture to get data
        log = self.getLogger()
        homepage=HomePage(self.driver)
        loginpage=LoginPage(self.driver)
        bookpage=MakeAppoinment(self.driver)



        self.click1(homepage.menutoggled())
        log.info("clicked on Menu")
        self.click1(homepage.logininto())
        log.info("clicked on Login")
        self.sendKeys(loginpage.getUsername(),getData["Username"])
        log.info("Entered Username")
        self.sendKeys(loginpage.getpasswd(),getData["Password"])
        log.info("Entered Password")
        self.click1(loginpage.getloginbtn())
        log.info("Loggin in")

        assert bookpage.gettitlef().is_displayed()
        log.info("Logged into booking page")

    @pytest.fixture(params=LoginPageData.getTestData("TC1"))
    def getData(self, request):
        return request.param




