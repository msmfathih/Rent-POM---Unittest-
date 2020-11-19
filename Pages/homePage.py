from selenium.webdriver.common.by import By

class HomePage():

    def __init__(self, driver):
        self.driver = driver

        self.dropdown_xpath = "/html/body/div[1]/aside[1]/div/div[4]/div/div/nav/ul/li[2]/a"
        self.select_registerdriver_xpath = "//p[contains(text(),'Register Drivers')]"


    def click_dropdown_menu(self):
        self.driver.find_element_by_xpath(self.dropdown_xpath).click()

    def select_registerdriver_page(self):
        self.driver.find_element(By.XPATH, self.select_registerdriver_xpath).click()



