# Practice Software Testing - Playwright & Pytest Automation Framework

A scalable, modular test automation framework built for [Practice Software Testing](https://practicesoftwaretesting.com/) using Python, Playwright, and Pytest, structured around the **Page Object Model (POM)** design pattern.

---

## 🚀 Key Features

* **Page Object Model (POM):** Clean separation of test logic from page structures and locators.
* **Modular Payment Flows:** Distinct, dedicated methods for each payment type (Cash on Delivery, Bank Transfer, Credit Card, BNPL, and Gift Cards) to completely avoid messy conditional logic (`if/else` anti-patterns).
* **Robust Fixtures:** Standardized Pytest fixtures handle automated setup states (login, cart population, address filling) to keep test scripts lightweight (often just 1–2 lines each).
* **CI/CD Integration:** Automated workflow configuration via GitHub Actions.

---

## 📂 Project Structure

```text
├── .github/
│   └── workflows/
│       └── test.yml       # GitHub Actions CI/CD pipeline configuration
├── pages/
│   ├── account_page.py    # Account dashboard elements and locators
│   ├── catalog_page.py    # Product listing and filtering logic
│   └── checkout_page.py   # Cart, address, and multi-flow payment handlers
│   └── login_page.py      # Authentication workflows
├── tests/
│   ├── cart_test.py       # Cart and item selection tests
│   ├── checkout_test.py   # End-to-end payment flow test suite
│   └── login_test.py      # Successful and negative login tests
├── .gitignore             # Excluded local artifacts and environment caches
├── requirements.txt       # Project dependencies
└── README.md