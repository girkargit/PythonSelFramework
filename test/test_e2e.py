import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pageObject.checkOutPage import CheckOutPage
from pageObject.homePage import HomePage
from utilities.baseclass import BaseClass # In the base class fixture is mentioned.

class TestOne(BaseClass):

    def test_e2e(self):
        hompage = HomePage(self.driver)
        # self.driver.find_element(By.XPATH, "//a[text()='Shop']").click()
        # hompage.shopeItem().click() # Becuase optimizing object so click is removed
        CheckOutPage = hompage.shopeItem()
        # cards = self.driver.find_elements(By.XPATH, "//div[@class='card-body']//h4[@class='card-title']")
        # checkoutpage = CheckOutPage(self.driver) # Becuase optimizing object.
        cards = CheckOutPage.getCardTitles()
        for k in cards:
            if "Blackberry" in k.text:
        #         # self.driver.find_element(By.XPATH, "//button[@class='btn btn-info']").click()
                CheckOutPage.getCardFooter().click()
        CheckOutPage.getCardcheckout().click()
        CheckOutPage.getCardsuccess().click()
        self.driver.find_element(By.XPATH, "//input[@id='country']").send_keys("ind")
        self.verify_link_presense("//a[text()='India']") # Create custom utilities.
        self.driver.find_element(By.XPATH, "//a[text()='India']").click()
        self.driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
        self.driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
        txt = self.driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
        print(txt)