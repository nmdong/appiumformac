
#!/usr/bin/python

# ********************************************************************
# This library mainly focused on Equinox Client with help of
# selenium remote webdriver.
# Author Dong Nguyen <nmdong@tma.com.vn>
# Date 30 Dec 2018
# *******************************************************************

import unittest
import time
import logging
from selenium import webdriver
from Library.pom.chromePage import githubLoginPage, githubResponsivePage

class Github_web(unittest.TestCase):
    '''
        This class will help to automate chrome for mac OS  use appium driver
    '''

    def __init__(self, client_ip=None, client_port=None):
        logging.info('Start auto browser: chrome')
        self.chrome_driver = None
        self.client_ip = client_ip
        self.client_port = client_port

    def launch_browser_use_selenium(self, url=None):
        '''
            * Function name: lauch_browser
            * Description: This function is used to launch web address
            * Parameters:
                + url: this is address web
            * Author: Dong Nguyen
            * Date: Feb, 2019
            * Ex: lauch_browser  http://appium.io/
            * Modify by:
            * Date
        '''
        profile1 = webdriver.ChromeOptions()
        profile1.accept_untrusted_cert = True
        profile1.add_argument("--lang=en")
        profile1.add_argument("start-maximized")
        self.profile = profile1
        logging.info('Web Address:   %s' % url)
        d = self.profile.to_capabilities()
        d['loggingPrefs'] = {'browser': 'ALL'}
        self.chrome_driver = webdriver.Remote('http://' + self.client_ip + ':' + self.client_port + '/wd/hub', desired_capabilities=d)
        self.chrome_driver.get(url)
        self.chrome_driver.set_page_load_timeout(30)
        self.chrome_driver.switch_to.default_content()
        self.main_window = self.chrome_driver.current_window_handle
        logging.info('%s' % self.main_window)
        time.sleep(5)
        title_current = self.chrome_driver.title
        logging.info('Title: %s' % title_current)
        return self.chrome_driver

    def login_github(self, user_name=None, password=None):
        '''
            * Function name: login_github
            * Description: This function is used to login_github
            * Parameters:
                + user_name: username or web address
                + password: password
            * Author: Dong Nguyen
            * Date: May, 2019
            * Ex: login_github  nmdong@gmail.com    123456
            * Modify by:
            * Date
        '''
        logging.info('Start function login_github with %s' %user_name)
        logging.info('Typing user name')
        self.assertTrue(githubLoginPage.GithubLogInPage().typing_username(self.chrome_driver, user_name), 'Typimg user name Failed')
        logging.info('Typing password')
        self.assertTrue(githubLoginPage.GithubLogInPage().typing_password(self.chrome_driver, password), 'Typimg password Failed')
        logging.info('Click on sign in')
        self.assertTrue(githubLoginPage.GithubLogInPage().click_sign_in_btn(self.chrome_driver), 'Click on signin button')
        logging.info('Verify login_github')
        self.assertTrue(githubResponsivePage.GithubResponsivePage().loading_responsivePage(self.chrome_driver,30), 'Not found ResponsivePage, So retunr failed')
        return True

    def logout_github(self):
        '''
            * Function name: logout_github
            * Description: This function is used to logout_github
            * Parameters: None
            * Author: Dong Nguyen
            * Date: May, 2019
            * Ex: logout_github
            * Modify by:
            * Date
        '''
        logging.info('Click on avatar')
        self.assertTrue(githubResponsivePage.GithubResponsivePage().click_avatar_user(self.chrome_driver),'Click on avatar failed')
        logging.info('Click on sign out button')
        self.assertTrue(githubResponsivePage.GithubResponsivePage().click_signout_btn(self.chrome_driver),'Click on signout button failed')
        logging.info('Verify logout_github')
        self.assertTrue(githubLoginPage.GithubLogInPage().wait_for_signin_text(self.chrome_driver,30), 'Not found signin text after click on signout, So retunr failed')
        return  True

    def exit_app(self):
        print 'Quitting the WebDriver session'
        self.chrome_driver.quit()
