*** Settings ***
Library     Browser
Resource    ../page_objects/login_page.resource
Resource    ../variables/common_variables.resource


*** Keywords ***
Open Login Page
    New Page    ${LOGIN_PAGE_URL}

Login As
    [Arguments]    ${username}    ${password}
    Fill Text    ${USERNAME_FIELD}    ${username}
    Fill Text    ${PASSWORD_FIELD}    ${password}
    Click    ${LOGIN_BUTTON}

Verify Redirected To Admin View
    Get Url    ==    ${ADMIN_VIEW_URL}

Verify Redirected To Super Admin View
    Get Url    ==    ${SUPER_ADMIN_URL}

Verify On Login Page
    Get Url    ==    ${LOGIN_PAGE_URL}

Logout
    Click    ${LOGOUT_LINK}
