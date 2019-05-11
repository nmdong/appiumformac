*** Settings ***
Documentation    Suite description
Library      ../../Library/functions/github_chrome_use_seleinum.py
Library      github_chrome_use_seleinum.Github_web      10.102.1.102     4444      WITH NAME      chr

Test Teardown   Run Keyword If Test Failed    clean_up

*** Variables ***
${client_ip}        10.102.1.102
${clinet_port}      4622
${user_name}        nmdong.dtvt@gmail.com
${paasword}         Minhdong@043

*** Variables ***
${client_ip}        10.102.1.102
${clinet_port}      4622

*** Test Cases ***
TC02 Chrome use selenium
    [Tags]    DEBUG
    log to console  1. Lauch App
    chr.launch browser use selenium     https://github.com/login

    log to console  2. Login Github
    chr.login github    ${user_name}    ${paasword}

    log to console  3. Logout Gihub
    chr.logout github

    log to console  3. exit app
    chr.exit app

*** Keywords ***
clean_up
#    chr.exit app
    log to console  clean_up successfully