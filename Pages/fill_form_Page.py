from selenium import webdriver
from selenium.webdriver.common.by import By
from Locators.locators import Locators
from selenium.webdriver.support.select import Select

class FormPage():

    def __init__(self, driver):
        self.driver = driver

        self.drivername_xpath = Locators.drivername_xpath
        self.mobile_number_xpath = Locators.mobile_number_xpath
        self.email_xpath = Locators.email_xpath
        self.password_xpath = Locators.password_xpath
        self.nic_xpath = Locators.nic_xpath

        self.licenece_copy_file_name_id = Locators.licenece_copy_file_id
        self.licenece_backcopy_file_xpath = Locators.licenece_backcopy_file_xpath
        self.vehicle_number_xpath = Locators.vehicle_number_xpath

        self.select_vehicle_owner_css_selector = Locators.select_vehicle_owner_css_selector
        self.select_vehicle_owner_permission_xpath = Locators.select_vehicle_owner_permission_xpath
        self.select_vehicle_type_xpath = Locators.select_vehicle_type_xpath

        self.upload_vihicle_picture_xpath = Locators.picture_vehicle_xpath
        self.enter_engine_number_xpath = Locators.engine_number_xpath
        self.enter_chassis_number_xpath = Locators.chassis_number_xpath

        self.enter_parking_location_xpath = Locators.parking_location_xpath



    def enter_drivername(self, drivername):
        self.driver.find_element(By.XPATH, self.drivername_xpath).send_keys(drivername)

    def enter_mobile_number(self, mobilenumber):
        self.driver.find_element(By.XPATH, self.mobile_number_xpath).send_keys(mobilenumber)

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, self.email_xpath).send_keys(email)

    def enter_driver_password(self, driverpassword):
        self.driver.find_element(By.XPATH, self.password_xpath).send_keys(driverpassword)



    def enter_nic(self, drivernic):
        self.driver.find_element(By.XPATH, self.nic_xpath).send_keys(drivernic)

    def upload_licence(self, driver_licence):
        self.driver.find_element(By.ID, self.licenece_copy_file_name_id).send_keys(driver_licence)

    def upload_licence_back(self, driver_backlicence):
        self.driver.find_element(By.XPATH, self.licenece_backcopy_file_xpath).send_keys(driver_backlicence)



    def enter_vehicle_number(self, vehicle_number):
        self.driver.find_element(By.XPATH, self.vehicle_number_xpath).send_keys(vehicle_number)

    def select_vehicle_owner_permission(self, owner_permission):
        self.driver.find_element(By.CSS_SELECTOR, self.select_vehicle_owner_css_selector).click()

    def select_vehicle_type(self, vehicle_type):
        element1 = self.driver.find_element(By.XPATH, self.select_vehicle_type_xpath)
        sel2 = Select(element1)
        sel2.select_by_index(2)


    def upload_vihicle_picture(self, vehicle_picture):
        self.driver.find_element(By.XPATH, self.upload_vihicle_picture_xpath).send_keys(vehicle_picture)


    def enter_parking_location(self, parking_location):
        self.driver.find_element(By.XPATH, self.enter_parking_location_xpath).send_keys(parking_location)

    # def enter_engine_number(self, engine_number):
    #     self.driver.find_element(By.XPATH, self.vehicle_number_xpath).send_keys(engine_number)




    #
    # def enter_chassis_number(self, chassis_number):
    #     self.driver.find_element(By.XPATH, self.enter_chassis_number_xpath).send_keys(chassis_number)



















