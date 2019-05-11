
#!/usr/bin/python

# ********************************************************************
# This library mainly focused on calculator with help of
# selenium remote webdriver.
# Author Dong Nguyen <nmdong@tma.com.vn>
# Date 30 Dec 2018
# *******************************************************************
from selenium.webdriver.support.expected_conditions import url_to_be, element_located_selection_state_to_be

from Library.pom.utility import utility
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class GithubLogInPage(unittest.TestCase):
    '''
        This class will help to automate calculator for mac OS
    '''

    def __init__(self):
        self.USER_NAME_INPUT    = {By.CSS_SELECTOR, "#login_field"}
        self.PASSWORD_INPUT     = {By.CSS_SELECTOR, "#password"}
        self.SIGN_IN_BTN        = {By.CSS_SELECTOR, "input.btn.btn-primary.btn-block"}
        self.SIGN_IN_TXT        = (By.CSS_SELECTOR, "a.HeaderMenu-link.no-underline.mr-3")

    def wait_for_signin_text(self, driver, time_out):
        '''
        * Function name: wait_for_signin_text
        * Description: This function is used to wait_for_signin_text
        * Parameters:  driver, time_out
        * Author: Dong Nguyen
        * Date: May, 2019
        * Ex: wait_for_signin_text(driver, '10')
        '''
        self.assertTrue(utility.Utility().wait_for_exists(driver, 20, *(self.SIGN_IN_TXT)), 'Not found signIn text')
        return True

    def typing_username(self, driver, user_name):
        '''
        * Function name: typing_username
        * Description: This function is used to typing_username
        * Parameters:  driver, user_name
        * Author: Dong Nguyen
        * Date: May, 2019
        * Ex: typing_password(driver, 'dong')
        '''
        self.assertTrue(utility.Utility().wait_for_exists(driver, 10, *(self.USER_NAME_INPUT)),'not found user name input')
        ele_username = driver.find_element(*self.USER_NAME_INPUT)
        ele_username.click()
        ele_username.clear()
        ele_username.send_keys(user_name)
        # self.assertTrue(utility.Utility().send_keys(driver, user_name), 'Typing use name failed')
        return True

    def typing_password(self, driver, password):
        '''
        * Function name: typing_password
        * Description: This function is used to entering password
        * Parameters:  driver, password
        * Author: Dong Nguyen
        * Date: May, 2019
        * Ex: typing_password(driver, '123456')
        '''
        ele_password = driver.find_element(*self.PASSWORD_INPUT)
        ele_password.click()
        ele_password.clear()
        ele_password.send_keys(password)
        # self.assertTrue(utility.Utility().send_keys(driver, password), 'Typing use name failed')
        return True

    def click_sign_in_btn(self, driver):
        '''
        * Function name: click_sign_in_btn
        * Description: This function is used to click sigin button
        * Parameters:  driver
        * Author: Dong Nguyen
        * Date: May, 2019
        * Ex: click_sign_in_btn(driver)
        '''
        ele_sigin_btn = driver.find_element(*self.SIGN_IN_BTN)
        self.assertTrue(utility.Utility().click_to_element(driver, ele_sigin_btn), 'Click on sigin button failed')
        return  True