# Playwright Automation Tests

This project contains automated UI tests using [Playwright](https://playwright.dev/), Python, and pytest. It focuses on verifying various functionalities of "The Internet Herokuapp" site. This project is intended for training purposes to demonstrate automation testing best practices.

---

## Table of Contents

- [Overview](#overview)
- [Test Structure](#test-structure)
- [Setup & Installation](#setup--installation)
- [Running Tests](#running-tests)
- [Page Object Model](#page-object-model)
- [Contributing](#contributing)
- [License](#license)

---

## Overview

These tests showcase how to automate interaction with web pages, including hover actions, navigation, and validation of UI elements.

Key features:

- Use of **Page Object Model (POM)** for maintainability
- Testing hover interactions, captions, links, and URL assertions
- Modular, reusable test code

---

## Test Structure

```plaintext
playwright-python/
├── pages/
│ ├── checkboxes_page.py # Page Object for the checkboxes page
│ ├── hovers_page.py # Page Object for the hovers page
│ └── login_page.py # Page Object for the login page
├── tests/
│ ├── conftest.py # Shared pytest configuration for browser and page fixtures
│ ├── test_checkboxes.py # Test script for checkboxes functionality
│ ├── test_hovers.py # Test script for hover functionality
│ └── test_login.py # Test script for login functionality
├── requirements.txt # Dependencies for the project
├── pytest.ini # Optional pytest configuration
├── .gitignore # Files and directories to ignore in version control
└── README.md # Project overview and documentation
└── LICENSE.txt # Project License
```

---

## Setup & Installation

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Install dependencies from requirements.txt

```
pip install -r requirements.txt
```

### Or manually

```
pip install playwright pytest
playwright install
```

### Download and install browser engines

```
python -m playwright install
```

### Running Tests

#### Run all tests

```
pytest tests/
```

#### Run specific test file

```
pytest tests/test_hovers.py
```

## Page Object Model

The project utilizes the Page Object Model (POM) design pattern to improve the readability and maintainability of test code. This approach involves creating a separate class for each page, encapsulating the locators and actions associated with that page (e.g., pages/hovers_page.py).
By interacting with pages through these abstractions, tests become more concise, flexible, and easier to maintain, reducing the likelihood of brittle test code that's tied to implementation details.

### Example usage:

###### hovers_page.py

```
from playwright.sync_api import Page


class HoversPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://the-internet.herokuapp.com/hovers"
        self.figure_locator = self.page.locator("div.figure")

    def goto(self):
        self.page.goto(self.url)

    # ... additional code ...


```

###### test_hovers.py

```
from pages.hovers_page import HoversPage

def test_hovers(page):
    hover_page = HoversPage(page)
    hover_page.goto()

    # ... additional test steps ...
```

## Contributing

Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request.

## Guidelines

Follow PEP8 style.
Write clear, descriptive commit messages.
Add new tests with proper page objects.

## License

This project is licensed under the MIT License. See the [MIT License](https://github.com/papachili/qa-automation-projects/blob/main/playwright-python/LICENSE.txt) file for details.
