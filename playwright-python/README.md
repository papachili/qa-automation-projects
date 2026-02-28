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

playwright-python/
├── pages/
│ └── hovers_page.py # Page Object for the hovers page
│ └── login_page.py # Page Object for the login page
├── tests/
│ └── test_hovers.py # Test script for hover functionality
│ └── test_login.py # Test script for login functionality
├── requirements.txt # Dependencies for the project
├── pytest.ini # Optional pytest configuration
├── .gitignore # Files and directories to ignore in version control
└── README.md # Project overview and documentation

---

## Setup & Installation

### Prerequisites

- Python 3.7+
- pip (Python package installer)

### Install dependencies

```bash
pip install playwright pytest
playwright install
      Download and install browser engines
          Copy
          Run
          python -m playwright install

Running Tests
Run all tests
          Copy
          Run
          pytest tests/
      Run specific test file
          Copy
          Run
          pytest tests/test_hovers.py
      Additional options

Run tests with verbose output:

          Copy
          Run
          pytest -v

Page Object Model
The project employs Page Object Model (POM) to enhance readability and maintainability.

pages/hovers_page.py: Encapsulates locators and actions for the hover page.
Tests interact with the page through this abstraction.

Example usage:
          Copy
          Run
          from pages.hovers_page import HoversPage

def test_hovers(page):
    hover_page = HoversPage(page)
    hover_page.goto()
    # ... test steps ...

Contributing
Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request.
Guidelines:

Follow PEP8 style.
Write clear, descriptive commit messages.
Add new tests with proper page objects.


License
This project is licensed under the MIT License. See the LICENSE file for details.
```
