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
from Pages.verify_owner_details import VerifyOwnerPage


class LoginTest3(unittest.TestCase):

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

        verifyownerpage = VerifyOwnerPage(driver)
        verifyownerpage.enter_username("admin@gmail.com")
        verifyownerpage.enter_password("admin@123")
        verifyownerpage.click_login()


    def test_priority2_navigate_dropdown(self):
        driver = self.driver
        verifyoweners = VerifyOwnerPage(driver)
        verifyoweners.navigate_dropdown("//p[contains(text(),'Vehicles')]")



    def test_priority3_vehicle_owner(self):
        driver = self.driver
        verifyoweners = VerifyOwnerPage(driver)
        verifyoweners.vehicle_owner("//p[contains(text(),'Vehicle Owners')]")
        time.sleep(2)


    def test_priority4_verify_vehicle_owner_name(self):
        driver = self.driver
        verifyoweners = VerifyOwnerPage(driver)
        message = driver.find_element_by_xpath("//td[contains(text(),'milhan')]").text
        self.assertEqual(message, "milhan")
        print("owner name is matched")
        time.sleep(2)


    def test_priority5_verify_owner_phone_number(self):
        driver = self.driver
        verifyoweners = VerifyOwnerPage(driver)
        message = driver.find_element_by_xpath("//td[contains(text(),'052845789')]").text
        self.assertEqual(message, "052845789")
        print("owner phone number matched")
        time.sleep(2)


    def test_priority6_verify_owner_nic(self):
        driver = self.driver
        verifyoweners = VerifyOwnerPage(driver)
        message = driver.find_element_by_xpath("//td[contains(text(),'052845789')]").text
        self.assertEqual(message, "052845789")
        print("owner nic number matched")
        time.sleep(2)


    @classmethod
    def tearDownClass(cls):
        # cls.driver.quite()
        print("Test has completed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/fathih/PycharmProjects/Rent_POM/Reports'))





