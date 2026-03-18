*** Settings ***
Library     Browser
Resource    ../page_objects/js_validation_page.resource
Resource    ../variables/common_variables.resource


*** Keywords ***
Open Validation Page
    New Page    ${BASE_URL}/pages/forms/javascript-validation/

Submit Forms With Values
    [Arguments]    ${value1}    ${value2}
    ${value1}=    Convert To String    ${value1}
    ${value2}=    Convert To String    ${value2}
    Fill Text    ${FIELD_1}    ${value1}
    Fill Text    ${FIELD_2}    ${value2}
    Click    ${SUBMIT_BUTTON}

Verify Validation Errors Shown
    Get Element States    ${RESULTS}    validate    detached
    Get Text    ${ERROR_1}    contains    less than 30
    Get Text    ${ERROR_2}    contains    less than 30

Verify Results Visible With Values
    [Arguments]    ${expected_val1}    ${expected_val2}
    ${expected_val1}=    Convert To String    ${expected_val1}
    ${expected_val2}=    Convert To String    ${expected_val2}
    Get Element States    ${RESULTS}    validate    visible
    ${actual1}=    Get Text    ${VALUE_1}
    ${actual2}=    Get Text    ${VALUE_2}
    Should Be Equal    ${actual1}    ${expected_val1}
    Should Be Equal    ${actual2}    ${expected_val2}

Verify No Errors Shown
    Get Element States    ${ERROR_1}    validate    value & hidden
    Get Element States    ${ERROR_2}    validate    value & hidden

Set Field Value Via JavaScript
    [Arguments]    ${locator}    ${value}
    Evaluate JavaScript    ${locator}    (el) => el.value = '${value}'
