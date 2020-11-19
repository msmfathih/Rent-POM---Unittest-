class Locators3():

    # login page objects
    username_textbox_id = "email"
    password_textbox_id = "password"
    loginbtn_id = "btnLogin"


    #navigate into vehicleowner dropdown
    dropdown_vehicle_xpath = "//p[contains(text(),'Vehicles')]"
    vehicle_owner_xpath = "//p[contains(text(),'Vehicle Owners')]"


    #verify user details
    vehicle_owner_name_xpath = "//td[contains(text(),'milhan')]"
    vehicle_owner_phone_number_xpath = "//td[contains(text(),'052845789')]"
    vehicle_owner_nic_xpath = "//td[contains(text(),'052845789')]"


    #logout test cases
    navigate_to_logout_xpath = "//p[contains(text(),'Need to logout ?')]"
    click_logout_xpath = "//p[contains(text(),'Logout')]"