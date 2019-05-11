
#!/usr/bin/python

# ********************************************************************
# This library mainly focused on calculator with help of
# selenium remote webdriver.
# Author Dong Nguyen <nmdong@tma.com.vn>
# Date 30 Dec 2018
# *******************************************************************

from Library.pom.utility import utility
import unittest, time, logging
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

class GithubResponsivePage(unittest.TestCase):
    '''
        This class will help to automate calculator for mac OS
    '''

    def __init__(self):
        self.AVATAR_USER        = {By.CSS_SELECTOR, "summary[aria-label='View profile and more']"}
        self.SIGN_OUT_BTN        = {By.CSS_SELECTOR, "button.dropdown-item.dropdown-signout"}

    def loading_responsivePage(self, driver, time_out):
        '''
        * Function name: loading_responsivePage
        * Description: This function is used to loading_responsivePage
        * Parameters:  driver, time_out
        * Author: Dong Nguyen
        * Date: May, 2019
        * Ex: loading_responsivePage(driver, '10')
        '''
        self.assertTrue(utility.Utility().wait_for_exists(driver, 20, *(self.AVATAR_USER)), 'Not found avatar user')
        return True


    def click_avatar_user(self, driver):
        '''
        * Function name: click_sign_in_btn
        * Description: This function is used to click avatar
        * Parameters:  driver
        * Author: Dong Nguyen
        * Date: May, 2019
        * Ex: click_avatar_user(driver)
        '''
        ele_avatar = driver.find_element(*self.AVATAR_USER)
        self.assertTrue(utility.Utility().click_to_element(driver, ele_avatar),'Not found avatar user')
        return True

    def click_signout_btn(self, driver):
        '''
        * Function name: click_avatar_user
        * Description: This function is used to click sigmout button
        * Parameters:  driver
        * Author: Dong Nguyen
        * Date: May, 2019
        * Ex: click_avatar_user(driver)
        '''
        ele_signout = driver.find_element(*self.SIGN_OUT_BTN)
        self.assertTrue(utility.Utility().click_to_element(driver, ele_signout))
        return True