*** Settings ***
Documentation    Suite description
Library      ../../Library/functions/github_chrome_use_seleinum.py
Library      github_chrome_use_seleinum.Github_web      10.102.1.102     4444      WITH NAME      chr

Test Teardown   Run Keyword If Test Failed    clean_up

*** Variables ***
${client_ip}        10.102.1.102
${clinet_port}      4622

*** Test Cases ***
TC02 Chrome use selenium
    [Tags]    DEBUG
    log to console  1. Lauch App
    chr.launch browser use selenium     http://appium.io
    log to console  3. exit app
    chr.exit app

*** Keywords ***
clean_up
    log to console  clean_up successfully