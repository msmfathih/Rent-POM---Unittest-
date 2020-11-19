from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import unittest
import pytest
import HtmlTestRunner
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Pages.loginPage import LoginPage
from Pages.homePage import HomePage
from Pages.fill_form_Page import FormPage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.implicitly_wait(10)
        # cls.driver.maximize_window()


    def test_priority1_valid_login(self):
        driver = self.driver
        driver.get("http://rentvehicles.multicompetition.com/login")
        titleOfWebPage=driver.title
        self.assertEqual("Rent Vehicles", titleOfWebPage, "Web Page title is matched")

        login = LoginPage(driver)
        login.enter_username("admin@gmail.com")
        login.enter_password("admin@123")
        login.click_login()


    def test_priority2_homepage(self):
        driver = self.driver
        homepage = HomePage(driver)
        homepage.click_dropdown_menu()
        homepage.select_registerdriver_page()


    def test_priority3_fillform(self):
        driver = self.driver
        formpage = FormPage(driver)
        formpage.enter_drivername("aadil")
        formpage.enter_mobile_number("0528542762")
        formpage.enter_email("aadil@gmail.com")
        formpage.enter_driver_password("123456")
        formpage.enter_nic("920012213v")


    def test_priority4_upload_licenece_copy_file(self):
        driver = self.driver
        formpage = FormPage(driver)
        formpage.upload_licence("C://Users//fathih//PycharmProjects//Rent_POM//Test//images//python.png")
        time.sleep(3)


    def test_priority5_upload_licenece_backcopy_file(self):
        driver = self.driver
        formpage = FormPage(driver)
        formpage.upload_licence_back("C://Users//fathih//PycharmProjects//Rent_POM//Test//images//python.png")


    def test_priority6_enter_vehicle_number(self):
        driver = self.driver
        formpage = FormPage(driver)
        formpage.enter_vehicle_number("EP-HQ-8165")

        # page = driver.find_elements_by_tag_name("html")
        # page.send_keys(Keys.END)
        driver.execute_script("window.scroll(0,700)")
        time.sleep(2)


    def test_priority7_select_vehicle_owner_permission(self):
        driver = self.driver
        formpage = FormPage(driver)
        formpage.select_vehicle_owner_permission("input.is_vehicle_owner:nth-child(4)")
        time.sleep(3)


    def test_priority8_select_vehicle_type(self):
        driver = self.driver
        formpage = FormPage(driver)
        formpage.select_vehicle_type("//select[@name='vehicle_type_id']")
        time.sleep(5)


    def test_priority9_upload_vehicle_picture(self):
        driver = self.driver
        formpage = FormPage(driver)
        formpage.upload_vihicle_picture("C://Users//fathih//PycharmProjects//Rent_POM//Test//images//python.png")
        time.sleep(8)


    # def test_priority10_enter_engine_number(self):
    #     driver = self.driver
    #     formpage = FormPage(driver)
    #     formpage.enter_engine_number("dsf34534534")
    #     time.sleep(3)

    def test_priority10_parking_location(self):
        driver = self.driver
        formpage = FormPage(driver)
        formpage.enter_parking_location("AbuDhabi001")
    #to be couninued.....




    @classmethod
    def tearDownClass(cls):
        cls.driver.quite()
        print("Test has completed")


if __name__ == '__main__':
    unittest.main()



