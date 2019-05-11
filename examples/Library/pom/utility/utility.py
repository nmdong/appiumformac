
#!/usr/bin/python

# ********************************************************************
# This library mainly focused on Equinox Client with help of
# selenium remote webdriver.
# Author Dong Nguyen <nmdong@tma.com.vn>
# Date 30 Dec 2018
# *******************************************************************

# Python default packages used in this lib.

import unittest
import time,datetime,inspect
import logging
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException

class Utility(unittest.TestCase):
    '''
        This class will help to automate calculator for mac OS
    '''
    def __init__(self):
        print  'Utility'
    def click_to_element(self, driver=None, element=None, useNativeEvents=0):
        if useNativeEvents > 0:
            # move and click the mouse like a user
            actions = ActionChains(driver)
            actions.click(element)
            actions.perform()
        else:
            # use the traditional accessibility action
            element.click()
        return True

    def send_keys(self, driver, message):
        message = str(message)
        if ":" in message:
            for i in message:
                logging.info('-------: %s' % i)
                if i == ":":
                    ActionChains(driver).key_down(Keys.SHIFT).send_keys(';').key_up(Keys.SHIFT).perform()
                    time.sleep(3)
                else:
                    ActionChains(driver).send_keys(i).perform()
        else:
            ActionChains(driver).send_keys(message).perform()
        return True

    def check_exists(self, driver, locator=None, element=None):
        '''
            * Convenience method to check existence immediately without using implicit timeout
            * returns: True iffound element else return False
            * Author: Dong Nguyen
            * Ex: check_exists(driver, By.NAME, "Hello")
        '''
        # logger.info('Start function check_exists_by_name')
        elements = driver.find_elements(locator, element)
        if len(elements) > 0:
            logging.info('Found element ' +(element))
            return True
        logging.info('Not found element %s' + (element))
        return False

    def wait_for_exists(self, driver, implicitTimeout_sec1=10, locator=None, element=None):
        '''
            * Convenience method to check existence immediately without using implicit timeout.
            * returns: True iffound element else return False
            * Author: Dong Nguyen
            * Ex: wait_for_exists(driver, By.NAME, "Hello")
        '''
        try:
            logging.info('Checking element...')
            wait = WebDriverWait(driver, implicitTimeout_sec1)
            wait.until(EC.visibility_of_element_located((locator, element)))
            logging.info('Found element ' + element)
            return True
        except WebDriverException as Ex:
            logging.error('Exception ' + str(Ex))
            return False