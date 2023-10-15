from selenium.webdriver.common.by import By
from pageObject.checkOutPage import CheckOutPage

class HomePage:
    def __init__(self, driver):
        self.driver = driver
    shop = (By.XPATH, "//a[text()='Shop']") # class variable
    name = (By.XPATH, "(//input[@name='name'])[1]")
    email = (By.XPATH, "//input[@name='email']")
    checkbox = (By.XPATH, "//input[@id='exampleCheck1']")
    gender = (By.XPATH, "//select[@id='exampleFormControlSelect1']")
    submit = (By.XPATH, "//input[@value='Submit']")
    alert_text = (By.XPATH, "//div[@class='alert alert-success alert-dismissible']")

    def shopeItem(self):
        # return self.driver.find_element(*HomePage.shop) # driver.find_element(By.XPATH, "//a[text()='Shop']").click()

        # Smart way of optimizing page object
        self.driver.find_element(*HomePage.shop).click()
        check_out = CheckOutPage(self.driver)
        return check_out

    def get_name(self):
        return self.driver.find_element(*HomePage.name)

    def get_email(self):
        return self.driver.find_element(*HomePage.email)

    def get_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox)

    def get_gender(self):
        return self.driver.find_element(*HomePage.gender)

    def get_submit(self):
        return self.driver.find_element(*HomePage.submit)

    def get_text(self):
        return self.driver.find_element(*HomePage.alert_text)

