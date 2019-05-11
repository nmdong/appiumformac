*** Settings ***
Documentation    Suite description
Library      ../../Library/functions/github_chrome_use_appium.py
Library      github_chrome_use_appium.Chrome_web                  WITH NAME      chr

Test Teardown   Run Keyword If Test Failed    clean_up

*** Variables ***
${client_ip}        10.102.1.102
${clinet_port}      4622

*** Test Cases ***
TC02_Chrome_not_use_selenium
    log to console  1. Lauch App
    chr.launch browser       ${client_ip}     ${clinet_port}      appium.io

    log to console  3. exit app
    chr.exit app

*** Keywords ***
clean_up
    log to console  clean_up successfully