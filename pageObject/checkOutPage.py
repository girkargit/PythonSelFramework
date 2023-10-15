from selenium.webdriver.common.by import By

class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    # driver.find_elements(By.XPATH, "//div[@class='card-body']//h4[@class='card-title']")
    cardTitle = (By.XPATH, "//app-card/div")
    # self.driver.find_elements(By.XPATH, "//div[@class='card-body']//h4[@class='card-title']")
    cardFooter = (By.XPATH, "//button[@class='btn btn-info']")
    cardCheckOut = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    cardChecksuccess = (By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_element(*CheckOutPage.cardFooter)

    def getCardcheckout(self):
        return self.driver.find_element(*CheckOutPage.cardCheckOut)

    def getCardsuccess(self):
        return self.driver.find_element(*CheckOutPage.cardChecksuccess)