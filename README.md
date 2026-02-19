# OrangeHRM Automation

Playwright + Pytest automation framework for OrangeHRM using Page Object Model.

## Project Structure

```text
├── tests/                  # Test logic (module-based grouping)
│   ├── login/              # Login module tests
│   ├── pim/                # PIM module tests
│   └── leave/              # Leave module tests
├── pages/                  # Page Object classes
├── fixtures/               # Reusable pytest fixtures
├── utils/                  # Helpers and config
├── docs/                   # Strategy and architecture docs
├── conftest.py             # Root fixtures and hooks
└── pytest.ini              # Pytest configuration and markers
```

## Running Tests

```bash
# Run all tests
pytest

# Run smoke tests only (MR pipeline)
pytest -m smoke

# Run regression tests (nightly pipeline)
pytest -m regression

# Run a specific module
pytest tests/login/
```

## Test Organization

Tests are grouped by **feature module** (login, pim, leave), not by test level.
Smoke vs regression separation is handled via `@pytest.mark.smoke` and `@pytest.mark.regression` markers.
