*** Settings ***
Library     Browser
Resource    ../variables/common_variables.resource


*** Variables ***
${USERNAME_FIELD}           id=username
${PASSWORD_FIELD}           id=password
${LOGIN_BUTTON}             id=login
${REMEMBER_ME_CHECKBOX}     css=[name="remember"]
${GO_LOGIN_BUTTON}          id=gologin
${LOGOUT_LINK}              text=Admin Logout
${LOGIN_PAGE_URL}           ${BASE_URL}/apps/simulated-login/
${ADMIN_VIEW_URL}           ${BASE_URL}/apps/simulated-login/adminview/
${SUPER_ADMIN_URL}          ${BASE_URL}/apps/simulated-login/superadminview/
${ADMIN_LOGIN_NAV}          id=navadminlogin
${ADMIN_VIEW_NAV}           id=navadminview
${SUPER_ADMIN_VIEW_NAV}     id=navadminsuperview
${ADMIN_LOGOUT_NAV}         id=navadminlogout
