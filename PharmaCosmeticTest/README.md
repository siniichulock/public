Introduction
------------

This repository contains basic example of usage PageObject
pattern with Selenium and Python (PyTest + Selenium).
Files
-----

[conftest.py](conftest.py) contains all the required code to catch failed test cases and make screenshot
of the page in case any test case will fail.

[base/base.py](base/base.py) contains PageObject pattern implementation for Python and contains helper methods to define web elements on web pages

[tests/test_Pharma.py](tests/test_Pharma.py) contains several smoke Web UI tests for Pharmacosmetica (https://www.pharmacosmetica.ru)


How To Run Tests
----------------

1) Install all requirements:

    ```bash
    pip install -r requirements
    ```

2) Download Selenium WebDriver from https://chromedriver.chromium.org/downloads (choose version which is compatible with your browser)

3) Run tests:

     in directory /tests/
      pytest -v test_Pharma.py

Note:
~/chrome in this example is the file of Selenium WebDriver downloaded and unarchived on step #2.
