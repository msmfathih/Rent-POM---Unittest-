from selenium import webdriver
from selenium.webdriver.common.by import By
from Locators.verify_vehicle_owner_locators import Locators3


class VerifyOwnerPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = Locators3.username_textbox_id
        self.password_textbox_id = Locators3.password_textbox_id
        self.loginbtn_id = Locators3.loginbtn_id

        self.navigate_dropdown_vehicle_xpath = Locators3.dropdown_vehicle_xpath
        self.vehicle_owner_xpath = Locators3.vehicle_owner_xpath

        self.vehicle_owner_name_xpath = Locators3.vehicle_owner_name_xpath
        self.vehicle_owner_phone_number_xpath = Locators3.vehicle_owner_phone_number_xpath
        self.vehicle_owner_nic_xpath = Locators3.vehicle_owner_nic_xpath

        self.navigate_logout_xpath = Locators3.navigate_to_logout_xpath
        self.click_logout_xpath = Locators3.click_logout_xpath



    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username_textbox_id).clear()
        self.driver.find_element(By.ID, self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_textbox_id).clear()
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.loginbtn_id).click()



    def navigate_dropdown(self, dropdownmenu):
        self.driver.find_element(By.XPATH, self.navigate_dropdown_vehicle_xpath).click()

    def vehicle_owner(self, vehicle_owner):
        self.driver.find_element(By.XPATH, self.vehicle_owner_xpath).click()



    def verify_vehicle_owner_name(self, owner_name):
        self.driver.find_element(By.XPATH, self.vehicle_owner_name_xpath).text()

    def verify_vehicle_owner_phone_number(self, phone_number):
        self.driver.find_element(By.XPATH, self.vehicle_owner_phone_number_xpath).text()

    def verify_owner_nic(self, owner_nic):
        self.driver.find_element(By.XPATH, self.vehicle_owner_nic_xpath).text()















