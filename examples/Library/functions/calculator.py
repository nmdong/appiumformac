
#!/usr/bin/python

# ********************************************************************
# This library mainly focused on calculator with help of
# selenium remote webdriver.
# Author Dong Nguyen <nmdong@tma.com.vn>
# Date 30 Dec 2018
# *******************************************************************

import unittest
import time
import logging
import driver
from Library.pom import calculatorPage, utility

from random import randint

class Calculator(unittest.TestCase):
    '''
        This class will help to automate calculator for mac OS
    '''

    def __init__(self):
        logging.info('Start auto Calculator app')
        self.windowPath = "/AXApplication[@AXTitle='Calculator']/AXWindow[0]"
        self.basicGroupPath = self.windowPath + "/AXGroup[1]"
        self.resultGroupPath = self.windowPath + "/AXGroup[0]"
        self.calculator_driver = None
        self.obj_calculator = None

    def lauch_app(self, client_ip=None, client_port=None):
        logging.info('Start function launch app calculator for mac')
        self.obj_calculator = driver.Driver(client_ip=client_ip, client_port=client_port, app_name='Calculator')
        self.calculator_driver = self.obj_calculator.get_driver()
        self.assertTrue(self.calculator_driver, 'Get calculator driver failed')
        logging.info('lauch_app successfully')
        return True

    def exit_app(self):
        print 'Quitting the WebDriver session'
        menubar = ['Calculator', 'Quit Calculator']
        self.obj_calculator.select_menu_item(self.calculator_driver, menubar)
        self.calculator_driver.quit()

    def do_some_calculations_with_clicks(self):
        print 'Clearing the calculator'
        calculatorPage.CalculatorPage().clearing_the_calculator(self.calculator_driver)

        rand1 = randint(0, 1000)
        rand2 = randint(0, 1000)

        print 'Entering the first number'
        for num in str(rand1):
            n = calculatorPage.CalculatorPage().numToAXPath(num)
            print str(num) + ' --> ' + str(n)
            utility.Utility().click_to_element(driver=self.calculator_driver, element=self.calculator_driver.find_element_by_xpath(n))
            time.sleep(1)

        print 'Clicking the "+" button'
        calculatorPage.CalculatorPage().clicking_the_add_button(self.calculator_driver)

        print 'Entering the second number'
        for num in str(rand2):
            n = calculatorPage.CalculatorPage().numToAXPath(num)
            print str(num) + ' --> ' + str(n)
            utility.Utility().click_to_element(self.calculator_driver, self.calculator_driver.find_element_by_xpath(n))
            time.sleep(2)

        print 'Clicking the "=" button'
        calculatorPage.CalculatorPage().clicking_the_equals_button(self.calculator_driver)

        print 'Reading result from screen'
        answer = calculatorPage.CalculatorPage().get_result_from_screen(self.calculator_driver)

        if int(answer) == (rand1 + rand2):
            print 'Correct Result: ' + answer
        else:
            self.fail('Incorect Result: ' + answer)

    def do_some_calculations_with_keystrokes(self):
        print 'Clearing the calculator'
        calculatorPage.CalculatorPage().clearing_the_calculator(self.calculator_driver)

        rand1 = randint(0, 1000)
        rand2 = randint(0, 1000)

        print 'Typing the first number'
        utility.Utility().send_keys(self.calculator_driver, rand1)

        print 'Typing the "+" button'
        utility.Utility().send_keys(self.calculator_driver, '+')

        print 'Typing the second number'
        utility.Utility().send_keys(self.calculator_driver, rand2)

        print 'Typing the "=" button'
        utility.Utility().send_keys(self.calculator_driver, '=')

        print 'Reading result from screen'
        answer = calculatorPage.CalculatorPage().get_result_from_screen(self.calculator_driver)

        if int(answer) == (rand1 + rand2):
            print 'Correct Result: ' + answer
        else:
            self.fail('Incorect Result: ' + answer)