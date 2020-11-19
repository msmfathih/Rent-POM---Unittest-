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
import timeout_decorator
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Pages.fill_owner_form import OwnerPage


class LoginTest2(unittest.TestCase):

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

        ownerpage = OwnerPage(driver)
        ownerpage.enter_username("admin@gmail.com")
        ownerpage.enter_password("admin@123")
        ownerpage.click_login()

    # @timeout_decorator.timeout(20)
    def test_priority2_click_dropdown(self):
        driver = self.driver
        ownerpage = OwnerPage(driver)
        ownerpage.click_driver_dropdown("//p[contains(text(),'Vehicles')]")


    def test_priority3_select_vehicle_owner(self):
        driver = self.driver
        ownerpage = OwnerPage(driver)
        ownerpage.select_vihicle_owner("//p[contains(text(),'Vehicle Owners')]")


    def test_priority4_add_vehicle_owner(self):
        driver = self.driver
        ownerpage = OwnerPage(driver)
        ownerpage.add_vihicle_owneselect_vehicle_typer("//a[@class='btn btn-success']")


    def test_priority5_enter_owner_name(self):
        driver = self.driver
        ownerpage = OwnerPage(driver)
        ownerpage.enter_owner_name("aadil")


    def test_priority6_enter_nic_number(self):
        driver = self.driver
        ownerpage = OwnerPage(driver)
        ownerpage.enter_nic_number("20012213v")


    def test_priority7_enter_phone_number(self):
        driver = self.driver
        ownerpage = OwnerPage(driver)
        ownerpage.enter_phone_number("052854262")


    @unittest.skip("demostrating skipping")
    def test_priority8_submit_form(self):
        driver = self.driver
        ownerpage = OwnerPage(driver)
        ownerpage.submit_form("//button[@class='btn btn-primary btn-submit']")



    @classmethod
    def tearDownClass(cls):
        # cls.driver.quite()
        print("Test has completed")

if __name__ == '__main__':
    unittest.main()





