*** Settings ***
Library     Browser
Resource    ../resources/keywords/js_validation_keywords.resource
Resource    ../resources/page_objects/js_validation_page.resource
Resource    ../resources/variables/common_variables.resource

Suite Setup     New Browser    ${BROWSER}    headless=False
Suite Teardown  Close Browser

*** Test Cases ***

Both Fields Submit With Empty Show Validation Errors
    Open Validation Page
    Click    ${SUBMIT_BUTTON}
    Verify Validation Errors Shown

First Field Valid Second Field Empty Show Validation Errors
    Open Validation Page
    Fill Text    ${FIELD_1}    1
    Click    ${SUBMIT_BUTTON}
    Get Element States    ${RESULTS}    validate    detached
    Get Element States    ${ERROR_1}    validate    value & hidden
    Get Text    ${ERROR_2}    contains    less than 30

Second Field Valid First Field Empty Show Validation Errors
    Open Validation Page
    Fill Text    ${FIELD_2}    1
    Click    ${SUBMIT_BUTTON}
    Get Element States    ${RESULTS}    validate    detached
    Get Text    ${ERROR_1}    contains    less than 30
    Get Element States    ${ERROR_2}    validate    value & hidden

First Field Invalid Second Field Valid Show Validation Error
    Open Validation Page
    Submit Forms With Values    50    10
    Get Element States    ${RESULTS}    validate    detached
    Get Text    ${ERROR_1}    contains    less than 30
    Get Element States    ${ERROR_2}    validate    value & hidden

First Field Valid Second Field Invalid Show Validation Error
    Open Validation Page
    Submit Forms With Values    15    31
    Get Element States    ${RESULTS}    validate    detached
    Get Text    ${ERROR_2}    contains    less than 30
    Get Element States    ${ERROR_1}    validate    value & hidden

Both Fields Valid Values Show Correct Values And No Errors
    Open Validation Page
    Submit Forms With Values    0    29
    Verify Results Visible With Values    0    29
    Verify No Errors Shown
    
Both Fields Values Equal To 30 Are Accepted Bug
    [Tags]    bug
    Open Validation Page
    Submit Forms With Values    30    30
    Verify Validation Errors Shown

Both Fields Values Greater Than 30 Show Validation Error
    Open Validation Page
    Submit Forms With Values    50    100
    Verify Validation Errors Shown

Both Fields Negative Values Show Correct Values
    Open Validation Page
    Submit Forms With Values    -1   -100
    Verify Results Visible With Values    -1   -100
    Verify No Errors Shown

Both Fields Valid Values Show Correct Values & No Errors Then Clear Results And Repeat
    Open Validation Page
    Submit Forms With Values    15    15
    Verify Results Visible With Values    15    15
    Verify No Errors Shown
    Click    ${CLEAR_BUTTON}
    Submit Forms With Values    15    15
    Verify Results Visible With Values    15    15
    Verify No Errors Shown

Both Fields Very Large Values Show Validation Error
    Open Validation Page
    Submit Forms With Values    999999999999    999999999999
    Verify Validation Errors Shown

Both Fields Non-numerical Show Validation Error
    Open Validation Page
    Set Field Value Via JavaScript    ${FIELD_1}    aaa
    Set Field Value Via JavaScript    ${FIELD_2}    bbb
    Click    ${SUBMIT_BUTTON}
    Verify Validation Errors Shown

First Fields Non-numerical Second Valid Show Validation Error
    Open Validation Page
    Set Field Value Via JavaScript    ${FIELD_1}    TestStringInput
    Fill Text    ${FIELD_2}    11
    Click    ${SUBMIT_BUTTON}
    Get Element States    ${RESULTS}    validate    detached
    Get Text    ${ERROR_1}    contains    less than 30
    Get Element States    ${ERROR_2}    validate    value & hidden  

