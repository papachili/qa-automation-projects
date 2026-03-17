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
- Testing alerts, forms, navigation, dynamic content, and more
- Modular, reusable keyword structure
- HTML reports generated automatically after each test run

---

## Test Structure

```plaintext
robot-playwright-python/
├── tests/
│   └── alerts.robot                      # Tests for JavaScript alert dialogs
├── resources/
│   ├── variables/
│   │   └── common_variables.resource     # URLs, browser settings, shared vars
│   └── page_objects/
│       └── alerts_page.resource          # Locators for the alerts page
├── test-results/                         # Auto-generated test reports (git-ignored)
├── requirements.txt                      # Python dependencies
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

### Run by tag (TODO)

```powershell
robot --outputdir test-results --include smoke tests/
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

###### alerts_page.resource

```robotframework
*** Settings ***
Library    Browser

*** Variables ***
${ALERT_BUTTON}      id=alertexamples
${ALERT_RESULT}      id=alertexplanation
${CONFIRM_BUTTON}    id=confirmexample
${CONFIRM_RETURN}    id=confirmreturn
${CONFIRM_RESULT}    id=confirmexplanation
${PROMPT_BUTTON}     id=promptexample
${PROMPT_RETURN}     id=promptreturn
${PROMPT_RESULT}     id=promptexplanation

```

###### alerts.robot

```robotframework
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
