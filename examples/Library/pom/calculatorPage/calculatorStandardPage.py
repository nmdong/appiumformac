
#!/usr/bin/python

# ********************************************************************
# This library mainly focused on calculator with help of
# selenium remote webdriver.
# Author Dong Nguyen <nmdong@tma.com.vn>
# Date 30 Dec 2018
# *******************************************************************
from Library.pom.utility import utility
import unittest

from selenium.webdriver import ActionChains

class CalculatorStandardPage(unittest.TestCase):
    '''
        This class will help to automate calculator for mac OS
    '''

    def __init__(self):
        self.windowPath         = "/AXApplication[@AXTitle='Calculator']/AXWindow[0]"
        self.basicGroupPath     = self.windowPath + "/AXGroup[1]"
        self.resultGroupPath    = self.windowPath + "/AXGroup[0]"
        self.button_clear       = self.basicGroupPath + "/AXButton[@AXDescription='clear']"
        self.button_plus        = self.basicGroupPath + "/AXButton[@AXDescription='add']"
        self.button_equals      = self.basicGroupPath + "/AXButton[@AXDescription='equals']"
        self.text_result        = self.resultGroupPath + "/AXStaticText[@AXDescription='main display']"

    def numToAXPath(self, num=None):
        num = int(num)
        if num == 0:
            return self.basicGroupPath + "/AXButton[@AXDescription='zero']"
        elif num == 1:
            return self.basicGroupPath + "/AXButton[@AXDescription='one']"
        elif num == 2:
            return self.basicGroupPath + "/AXButton[@AXDescription='two']"
        elif num == 3:
            return self.basicGroupPath + "/AXButton[@AXDescription='three']"
        elif num == 4:
            return self.basicGroupPath + "/AXButton[@AXDescription='four']"
        elif num == 5:
            return self.basicGroupPath + "/AXButton[@AXDescription='five']"
        elif num == 6:
            return self.basicGroupPath + "/AXButton[@AXDescription='six']"
        elif num == 7:
            return self.basicGroupPath + "/AXButton[@AXDescription='seven']"
        elif num == 8:
            return self.basicGroupPath + "/AXButton[@AXDescription='eight']"
        elif num == 9:
            return self.basicGroupPath + "/AXButton[@AXDescription='nine']"
        else:
            return ""

    def clearing_the_calculator(self, driver):
        button_clear_ele = driver.find_element_by_xpath(self.button_clear)
        utility.Utility().click_to_element(driver, button_clear_ele)

    def clicking_the_add_button(self, driver):
        button_plus_ele = driver.find_element_by_xpath(self.button_plus)
        utility.Utility().click_to_element(driver, button_plus_ele)

    def clicking_the_equals_button(self, driver):
        button_equals_ele = driver.find_element_by_xpath(self.button_equals)
        utility.Utility().click_to_element(driver, button_equals_ele)

    def get_result_from_screen(self, driver):
        text_result_ele = driver.find_element_by_xpath(self.text_result)
        print 'Reading result from screen'
        ActionChains(driver).move_to_element(text_result_ele).perform()
        return text_result_ele.text