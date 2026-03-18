*** Settings ***
Library             Browser
Resource            ../resources/page_objects/login_page.resource
Resource            ../resources/keywords/login_keywords.resource
Resource            ../resources/variables/common_variables.resource

Suite Setup         New Browser    ${BROWSER}    headless=False
Suite Teardown      Close Browser


*** Test Cases ***
Admin Valid Login Redirects To Admin View
    Open Login Page
    Login As    Admin    AdminPass
    Verify Redirected To Admin View

Super Admin Valid Login Redirects To Super Admin View
    Open Login Page
    Login As    SuperAdmin    AdminPass
    Verify Redirected To Super Admin View

Empty Credentials Show Error
    Open Login Page
    Login As    ${EMPTY}    ${EMPTY}
    Verify On Login Page

Invalid Credentials Show Error
    Open Login Page
    Login As    wronguser    wrongpass
    Verify On Login Page

Admin Logout Returns To Login Page
    Open Login Page
    Login As    Admin    AdminPass
    Verify Redirected To Admin View
    Logout
    Verify On Login Page

Super Admin Logout Redirects To Login Page
    Open Login Page
    Login As    SuperAdmin    AdminPass
    Verify Redirected To Super Admin View
    Logout
    Verify On Login Page

Already Logged In Admin Redirects Away From Login Page
    Open Login Page
    Login As    Admin    AdminPass
    Verify Redirected To Admin View
    Click    ${GO_LOGIN_BUTTON}
    Verify Redirected To Admin View

Already Logged In Super Admin Redirects Away From Login Page
    Open Login Page
    Login As    SuperAdmin    AdminPass
    Verify Redirected To Super Admin View
    Click    ${GO_LOGIN_BUTTON}
    Verify Redirected To Super Admin View

Test Navbar as Admin
    Open Login Page
    Login As    Admin    AdminPass
    Verify Redirected To Admin View
    Click    ${ADMIN_LOGIN_NAV}
    Verify Redirected To Admin View
    Click    ${ADMIN_VIEW_NAV}
    Verify Redirected To Admin View
    Click    ${SUPER_ADMIN_VIEW_NAV}
    Verify Redirected To Admin View
    Click    ${ADMIN_LOGOUT_NAV}
    Verify On Login Page

Test Navbar as Super Admin
    Open Login Page
    Login As    SuperAdmin    AdminPass
    Click    ${ADMIN_LOGIN_NAV}
    Verify Redirected To Super Admin View
    Click    ${ADMIN_VIEW_NAV}
    Verify Redirected To Admin View
    Click    ${SUPER_ADMIN_VIEW_NAV}
    Verify Redirected To Super Admin View
    Click    ${ADMIN_LOGOUT_NAV}
    Verify On Login Page

Access Admin View Without Login Redirects To Login Page
    New Page    ${ADMIN_VIEW_URL}
    Verify On Login Page

Access Super Admin View Without Login Redirects To Login Page
    New Page    ${SUPER_ADMIN_URL}
    Verify On Login Page

Cookie Injection Bypasses Login
    New Page    ${LOGIN_PAGE_URL}
    Add Cookie    loggedin    Admin    url=${BASE_URL}
    Go To    ${ADMIN_VIEW_URL}
    Verify Redirected To Admin View

Super Admin Cookie Injection Bypasses Login
    New Page    ${LOGIN_PAGE_URL}
    Add Cookie    loggedin    SuperAdmin    url=${BASE_URL}
    Go To    ${SUPER_ADMIN_URL}
    Verify Redirected To Super Admin View

Tampered Cookie Value Redirects To Login Page
    [Tags]    bug    security
    New Page    ${LOGIN_PAGE_URL}
    Add Cookie    loggedin    FakeUser    url=${BASE_URL}
    Go To    ${ADMIN_VIEW_URL}
    Verify On Login Page

Remember Me Checkbox Has No Effect
    [Documentation]    Remember me checkbox can be toggled but has no visible
    ...               effect on cookie expiry or session persistence
    [Tags]    bug
    Open Login Page
    Click    ${REMEMBER_ME_CHECKBOX}
    Click    ${REMEMBER_ME_CHECKBOX}
    Login As    Admin    AdminPass
    Verify Redirected To Admin View
    Click    ${ADMIN_LOGOUT_NAV}
    Verify On Login Page
