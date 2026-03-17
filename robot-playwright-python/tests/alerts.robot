*** Settings ***
Library     Browser
Resource    ../resources/page_objects/alerts_page.resource
Resource    ../resources/variables/common_variables.resource

Suite Setup     New Browser    ${BROWSER}    headless=False
Suite Teardown  Close Browser

*** Test Cases ***

Alert Dialog Is Displayed And Accepted
    New Page    ${BASE_URL}/pages/basics/alerts-javascript/
    Handle Future Dialogs    action=accept
    Click    ${ALERT_BUTTON}
    Get Text    ${ALERT_RESULT}    contains    alert dialog

Confirm Dialog Accepted Returns True
    New Page    ${BASE_URL}/pages/basics/alerts-javascript/
    Handle Future Dialogs    action=accept
    Click    ${CONFIRM_BUTTON}
    Get Text    ${CONFIRM_RETURN}    contains    true
    Get Text    ${CONFIRM_RESULT}    contains    returned true

Confirm Dialog Dismissed Returns False
    New Page    ${BASE_URL}/pages/basics/alerts-javascript/
    Handle Future Dialogs    action=dismiss
    Click    ${CONFIRM_BUTTON}
    Get Text    ${CONFIRM_RETURN}    contains    false
    Get Text    ${CONFIRM_RESULT}    contains    returned false

Prompt Dialog With Input Returns Typed Text
    New Page    ${BASE_URL}/pages/basics/alerts-javascript/
    Handle Future Dialogs    action=accept    prompt_input=Hello Robot
    Click    ${PROMPT_BUTTON}
    Get Text    ${PROMPT_RETURN}    contains    Hello Robot
    Get Text    ${PROMPT_RESULT}    contains    returned Hello Robot