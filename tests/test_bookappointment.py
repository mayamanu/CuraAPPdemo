
#Homepage
import pytest

from Data.GetData import LoginPageData
from PageObjects.ConfirmationPage import ConfPage
from PageObjects.HomePage import HomePage
from PageObjects.LoginPage import LoginPage
from PageObjects.MakeAppoinmentPage import MakeAppoinment
from utilities.BaseClass import BaseClass


class TestBookAppointment(BaseClass):
    def test_appoinment(self,getData):#calling ficture to get data
        log = self.getLogger()
        homepage=HomePage(self.driver)
        loginpage=LoginPage(self.driver)
        bookpage=MakeAppoinment(self.driver)
        confpage=ConfPage(self.driver)



        self.click1(homepage.menutoggled())
        log.info("Clicked on Menu")
        self.click1(homepage.logininto())
        log.info("Clicked on Login")
        self.sendKeys(loginpage.getUsername(),getData["Username"])
        log.info("Entered Username")
        self.sendKeys(loginpage.getpasswd(),getData["Password"])
        log.info("Entered Password")
        self.click1(loginpage.getloginbtn())
        log.info("logging in")
        self.selectFromDD(bookpage.dropdownf(),getData["Facility"])
        log.info("selecting facility")
        self.click1(bookpage.checkboxf())
        log.info("Apply for hospital readmission")
        radiobuttons=bookpage.radiobuttonsf()
        self.click1(radiobuttons[2])
        log.info("choosing none")
        self.sendKeys(bookpage.visitdataf(),getData["Visit Date"])
        log.info("specifying visit date")
        self.sendKeys(bookpage.txtcommentf(),getData["Comment"])
        log.info("Entering comment as follwup")
        self.click1(bookpage.bookbtnf())
        log.info("Booking button clicked")

        assert confpage.getTitle().is_displayed()
        log.info("confirmation page ")

    @pytest.fixture(params=LoginPageData.getTestData("TC2"))
    def getData(self, request):
        return request.param

