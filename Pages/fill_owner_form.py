from selenium import webdriver
from selenium.webdriver.common.by import By
from Locators.vehicle_owner_locators import Locators2


class OwnerPage():

    def __init__(self, driver):
        self.driver = driver

        self.username_textbox_id = Locators2.username_textbox_id
        self.password_textbox_id = Locators2.password_textbox_id
        self.loginbtn_id = Locators2.loginbtn_id

        self.drivername_xpath = Locators2.dropdown_vehicle_xpath
        self.vihicle_owner_xpath = Locators2.select_vihicle_owner_xpath
        self.add_vihicle_owners_xpath = Locators2.add_vehicle_owners_xpath

        self.owner_name_id = Locators2.owner_name_id
        self.nic_number_name = Locators2.nic_number_name
        self.phone_number_name = Locators2.phone_number_name
        self.submit_form_xpath = Locators2.form_submit_xpath



    def enter_username(self, username):
        self.driver.find_element(By.ID, self.username_textbox_id).clear()
        self.driver.find_element(By.ID, self.username_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.password_textbox_id).clear()
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.loginbtn_id).click()



    def click_driver_dropdown(self, dropdown):
        self.driver.find_element(By.XPATH, self.drivername_xpath).click()

    def select_vihicle_owner(self, vehicle_owner):
        self.driver.find_element(By.XPATH, self.vihicle_owner_xpath).click()

    def add_vihicle_owner(self, addvehicle_owner):
        self.driver.find_element(By.XPATH, self.add_vihicle_owners_xpath).click()


    #owner registration
    def enter_owner_name(self, ownername):
        self.driver.find_element(By.ID, self.owner_name_id).send_keys(ownername)

    def enter_nic_number(self, nic_number):
        self.driver.find_element(By.NAME, self.nic_number_name).send_keys(nic_number)

    def enter_phone_number(self, phone_number):
        self.driver.find_element(By.NAME, self.phone_number_name).send_keys(phone_number)

    def submit_form(self, submit_form):
        self.driver.find_element(By.XPATH, self.submit_form_xpath).send_keys(submit_form)













