*** Settings ***
Documentation     Test Suite to run Command Line Interface Test cases
Suite Setup       Run keyword    global_variable_settings    # setting variable that can be used across suites
Suite Teardown
Test Setup
Test Teardown     Run Keyword    Close All Connections    # Closes all Terminals Opened
Resource          ../Resources/Config.txt

*** Test Cases ***
CLI Login
    [Documentation]    Demo test for FDD console application
    [Setup]    Run Process    python    ../FDDConsole.py
