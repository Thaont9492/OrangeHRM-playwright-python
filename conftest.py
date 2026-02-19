import pytest
from playwright.sync_api import sync_playwright
from utils.config import settings
from fixtures.auth_fixture import admin_page, admin_storage_state

@pytest.fixture(scope="session")
def playwright_instance():
    """Initialize Playwright instance for the test session."""
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="function")
def browser(playwright_instance):
    """Launch a new browser instance for each test function."""
    browser = playwright_instance.chromium.launch(headless=settings.headless)
    yield browser
    browser.close()

@pytest.fixture(scope="function")
def context(browser):
    """Create a new browser context for each test function."""
    context = browser.new_context()
    yield context
    context.close()

@pytest.fixture(scope="function")
def page(context):
    """Create a new page for each test function."""
    page = context.new_page()
    yield page
    page.close()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Hook to capture test results and take screenshots on failure."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")
        if page:
            screenshot_path = f"screenshots/{item.name}.png"
            page.screenshot(path=screenshot_path)
            print(f"Screenshot saved to {screenshot_path}")