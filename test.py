from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("C:\chrome_driver\chromedriver")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.XPATH, "//a[text()='Shop']").click()
card = driver.find_elements(By.XPATH, "//app-card/div")
for k in card:
    # info = k.text
    if "Blackberry" in k.text:
        driver.find_element(By.XPATH, "//button[@class='btn btn-info']").click()
driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
driver.find_element(By.XPATH, "//button[normalize-space()='Checkout']").click()
driver.find_element(By.XPATH, "//input[@id='country']").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[text()='India']")))
driver.find_element(By.XPATH, "//a[text()='India']").click()
driver.find_element(By.XPATH, "//label[@for='checkbox2']").click()
driver.find_element(By.XPATH, "//input[@value='Purchase']").click()
txt = driver.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").text
print(txt)

