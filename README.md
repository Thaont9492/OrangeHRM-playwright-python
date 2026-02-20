# OrangeHRM Test Automation

Playwright + Pytest automation framework for [OrangeHRM](https://opensource-demo.orangehrmlive.com/) using the Page Object Model pattern.

## Project Structure

```text
├── tests/                              # Test suites grouped by module
│   ├── login/
│   │   ├── test_login_smoke.py         # Login smoke tests
│   │   ├── test_login_validation.py    # Login validation scenarios
│   │   └── test_logout.py              # Logout tests
│   └── pim/
│       ├── test_create_employee_smoke.py       # Employee creation smoke tests
│       └── test_create_employee_regression.py  # Employee creation regression tests
├── pages/                              # Page Object classes
│   ├── base_page.py                    # Base page with shared methods
│   ├── login_page.py                   # Login page actions and locators
│   └── pim_page.py                     # PIM page actions and locators
├── fixtures/                           # Reusable pytest fixtures
│   └── auth_fixture.py                 # Authentication fixtures
├── utils/                              # Helpers and config
│   ├── config.py                       # Environment-based settings
│   └── data_generator.py              # Test data generation
├── docs/                               # Strategy and architecture docs
├── conftest.py                         # Root fixtures, hooks, screenshot-on-failure
└── pytest.ini                          # Pytest configuration and markers
```

## Setup

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium
```

## Configuration

Settings are loaded from environment variables with defaults for the public demo site:

| Variable         | Default                                        |
|------------------|------------------------------------------------|
| `BASE_URL`       | `https://opensource-demo.orangehrmlive.com/`   |
| `ADMIN_USERNAME` | `Admin`                                        |
| `ADMIN_PASSWORD` | `admin123`                                     |
| `HEADLESS`       | `true`                                         |

## Running Tests

```bash
# Run all tests
pytest

# Run by marker
pytest -m smoke
pytest -m regression

# Run a specific module
pytest tests/login/
pytest tests/pim/

# Run headed (visible browser)
HEADLESS=false pytest
```

## Test Markers

| Marker       | Description                  |
|--------------|------------------------------|
| `smoke`      | Smoke test suite             |
| `regression` | Full regression suite        |
| `business`   | Business flow tests          |
| `validation` | Validation scenarios         |

## Key Features

- **Page Object Model** — clean separation between test logic and page interactions
- **Screenshot on failure** — automatic screenshots saved to `screenshots/` when tests fail
- **Authenticated sessions** — reusable admin auth state via storage state
- **Parallel execution** — supports `pytest-xdist` for parallel test runs
- **Auto-retry** — flaky test retry with `pytest-rerunfailures`
