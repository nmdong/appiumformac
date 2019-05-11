*** Settings ***
Documentation    Suite description
Library      ../../Library/functions/calculator.py
Library       calculator.Calculator          WITH NAME       cal

Test Teardown   Run Keyword If Test Failed    clean_up

*** Variables ***
${client_ip}        10.102.1.102
${clinet_port}      4622

*** Test Cases ***
TC01_Calculator_Add_With_Click
    [Tags]    DEBUG
    log to console  1. Lauch App
    cal.lauch_app   ${client_ip}     ${clinet_port}
    log to console  2.do some calculations with clicks
    cal.do some calculations with clicks
    log to console  3. exit app
    cal.exit app


TC01_Calculator_Add_Keystrokes
    log to console  1. Lauch App
    cal.lauch_app   ${client_ip}     ${clinet_port}

    log to console  2.do some calculations with keystrokes
    cal.do some calculations with keystrokes
    log to console  3. exit app
    cal.exit app

*** Keywords ***
clean_up
    log to console  clean_up successfully