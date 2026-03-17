# Robot Framework Playwright Tests

This project contains automated UI tests using [Robot Framework](https://robotframework.org/) and [Playwright](https://playwright.dev/) (via the [Browser library](https://robotframework-browser.org/)), written in Python. It focuses on verifying various functionalities of [EvilTester Test Pages](https://testpages.eviltester.com/) (dedicated practice site for test automation). This project is intended for training purposes to demonstrate automation testing best practices.

---

## Table of Contents

- [Overview](#overview)
- [Test Structure](#test-structure)
- [Setup & Installation](#setup--installation)
- [Running Tests](#running-tests)
- [Viewing Reports](#viewing-reports)
- [Page Object Model](#page-object-model)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

These tests showcase how to automate interaction with web pages using a keyword-driven approach with Robot Framework and Playwright as the browser engine.

Key features:

- Use of **Page Object Model (POM)** for maintainability
- **Keyword-driven** test design using `.resource` files
- Testing alerts, form validation, and boundary value analysis
- Bug identification and documentation using `[Tags]    bug`
- JavaScript injection for testing restricted input fields
- Modular, reusable keyword structure
- HTML reports generated automatically after each test run

---

## Test Structure

```plaintext
robot-playwright-python/
├── tests/
│   ├── alerts.robot                          # Tests for JavaScript alert dialogs
│   └── js_validation.robot                   # Tests for JavaScript form validation
├── resources/
│   ├── keywords/
│   │   ├── alerts_keywords.resource          # Keywords specific to alerts page
│   │   └── js_validation_keywords.resource   # Keywords specific to JS validation page
│   ├── variables/
│   │   └── common_variables.resource         # URLs, browser settings, shared vars
│   └── page_objects/
│       ├── alerts_page.resource              # Locators for the alerts page
│       └── js_validation_page.resource       # Locators for the JS validation page
├── test-results/                             # Auto-generated test reports (git-ignored)
├── requirements.txt                          # Python dependencies
├── .gitignore
└── README.md
```

---

## Setup & Installation

### Prerequisites

- Python 3.8+
- pip (Python package installer)

### Create and activate virtual environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Install dependencies

```powershell
pip install -r requirements.txt
```

### Initialize Playwright browsers

```powershell
rfbrowser init
```

This downloads Chromium, Firefox, and WebKit browser engines used by the Browser library.

---

## Running Tests

### Run all tests

```powershell
robot --outputdir test-results tests/
```

### Run a specific test file

```powershell
robot --outputdir test-results tests/alerts.robot
```

### Run a specific test case

```powershell
robot --outputdir test-results -t "Test Name Here" tests/
```

### Run by tag

```powershell
robot --outputdir test-results --include bug tests/
```

### Run in headless mode

Set `headless=True` in your suite setup, or pass it as a variable:

```powershell
robot --outputdir test-results -v HEADLESS:True tests/
```

---

## Viewing Reports

Robot Framework automatically generates HTML reports after every run inside the `test-results/` folder.

After running tests, open the report in your browser:

```powershell
start test-results/report.html
```

The report includes:

- Pass/fail status per test case
- Step-by-step keyword execution log
- Screenshots on failure (if configured)
- Full execution timeline

---

## Page Object Model

This project uses the **Page Object Model (POM)** pattern adapted for Robot Framework using `.resource` files. Each page has a dedicated resource file in `resources/page_objects/` that holds its locators, keeping them separate from test logic.

Keywords that interact with a page are stored in `resources/keywords/`, making tests clean and readable.

### Example usage:

###### js_validation_page.resource

```robotframework
*** Settings ***
Library    Browser

*** Variables ***
${FIELD_1}          id=lteq30a
${FIELD_2}          id=lteq30b
${ERROR_1}          id=lteq30aerror
${ERROR_2}          id=lteq30berror
${SUBMIT_BUTTON}    css=[name="submitbutton"]
${CLEAR_BUTTON}     css=[name="clearbutton"]
${RESULTS}          id=rendered-form-results
${VALUE_1}          id=_valuevalue1
${VALUE_2}          id=_valuevalue2
```

###### js_validation_keywords.resource

```robotframework
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

Set Field Value Via JavaScript
    [Arguments]    ${locator}    ${value}
    Evaluate JavaScript    ${locator}    (el) => el.value = '${value}'

Verify Validation Errors Shown
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
```

###### js_validation.robot

```robotframework
*** Settings ***
Library     Browser
Resource    ../resources/keywords/js_validation_keywords.resource
Resource    ../resources/page_objects/js_validation_page.resource
Resource    ../resources/variables/common_variables.resource

Suite Setup     New Browser    ${BROWSER}    headless=False
Suite Teardown  Close Browser

*** Test Cases ***

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
```

---

## Contributing

Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request.

## Guidelines

- Follow [Robot Framework style guide](https://docs.robotframework.org/docs/style_guide) conventions.
- Write clear, descriptive commit messages.
- Add new tests with proper page object resource files.
- Keep locators in `page_objects/`, keywords in `keywords/`, tests in `tests/`.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
