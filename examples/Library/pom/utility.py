
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

from selenium.webdriver import ActionChains

class Utility(unittest.TestCase):
    '''
        This class will help to automate calculator for mac OS
    '''
    def __init__(self):
        print  '----'
    def click_to_element(self, driver=None, element=None, useNativeEvents=0):
        if useNativeEvents > 0:
            # move and click the mouse like a user
            actions = ActionChains(driver)
            actions.click(element)
            actions.perform()
        else:
            # use the traditional accessibility action
            element.click()

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