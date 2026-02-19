# Automation Framework Architecture

Framework: Playwright + Pytest
Design Pattern: Page Object Model
Language: Python

---

## 1. Directory Structure

orangehrm-automation/
│
├── tests/
│   ├── login/
│   │   ├── test_login_smoke.py
│   │   ├── test_login_validation.py
│   │   └── test_logout.py
│   ├── pim/
│   └── leave/
│
├── pages/
│   ├── base_page.py
│   ├── login_page.py
│   ├── pim_page.py
│   ├── leave_page.py
│
├── fixtures/
│   ├── browser_fixture.py
│   ├── auth_fixture.py
│
├── utils/
│   ├── data_generator.py
│   ├── config.py
│
├── docs/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitlab-ci.yml
└── README.md

---

## 2. Design Principles

- Test logic separated from page logic
- No assertion inside page class
- Reusable fixtures
- Config-driven environment
- No hardcoded sleep()
- Module-based test grouping (tests organized by feature, not test level)
- Smoke/regression separation via pytest markers, not folder structure

---

## 3. Page Object Model

Each page:
- Contains locators
- Contains interaction methods
- Returns clear state

---

## 4. Fixtures Strategy

- Browser fixture
- Admin login fixture
- Employee login fixture

---

## 5. Reporting & Debugging

- Screenshot on failure
- Retry support
- Parallel execution ready

---

## 6. CI Integration

- Smoke tests run on MR
- Regression nightly
- Artifact upload
- Merge blocking policy
