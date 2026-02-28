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
│ ├── hovers_page.py # Page Object for the hovers page
│ └── login_page.py # Page Object for the login page
├── tests/
│ ├── conftest.py # Shared pytest configuration that sets up test fixtures for browser and page usage across multiple test scripts
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

The project employs Page Object Model (POM) to enhance readability and maintainability.
f.e
pages/hovers_page.py: Encapsulates locators and actions for the hover page.
Tests interact with the page through this abstraction.

### Example usage:

```
from pages.hovers_page import HoversPage

def test_hovers(page):
    hover_page = HoversPage(page)
    hover_page.goto()
    # ... test steps ...
```

## Contributing

Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request.

## Guidelines

Follow PEP8 style.
Write clear, descriptive commit messages.
Add new tests with proper page objects.

## License

This project is licensed under the MIT License. See the [MIT License](https://github.com/papachili/qa-automation-projects/blob/main/playwright-python/LICENSE.txt) file for details.
