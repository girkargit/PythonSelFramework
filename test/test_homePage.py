import pytest
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from pageObject.homePage import HomePage
from testData.home_pageData import HomePageData
from utilities.baseclass import BaseClass


class TestHomePage(BaseClass):

    def test_formsubmission(self, gets_data):
        log = self.getlogger()
        home_page = HomePage(self.driver)
        log.info("First name is %s" % gets_data["firstname"])
        # home_page.get_name().send_keys(gets_data[0])
        home_page.get_name().send_keys(gets_data["firstname"])
        log.info("Firstname")
        # home_page.get_email().send_keys(gets_data[1])
        home_page.get_email().send_keys(gets_data["email"])
        log.info("Email address")
        home_page.get_checkbox().click()
        # self.static_dropdown(home_page.get_gender(), gets_data[2])
        self.static_dropdown(home_page.get_gender(), gets_data["gender"])
        home_page.get_submit().click()
        txt = home_page.get_text().text
        log.info(txt)
        assert ("Success!" in txt)
        self.driver.refresh()

    # @pytest.fixture(params=[('abhi', 'test@test.com', 'Male'), ('suraj', 'test@test.com', 'Male')])
    @pytest.fixture(params= HomePageData.get_testData())
    def gets_data(self, request):
        return request.param





