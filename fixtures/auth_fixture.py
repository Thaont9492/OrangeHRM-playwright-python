import pytest
from pages.login_page import LoginPage
from utils.config import settings

STORAGE_STATE_PATH = "auth/admin_storage_state.json"

@pytest.fixture(scope="session")
def admin_storage_state(playwright_instance):
    """
    Login once per session and save storage state.
    """

    browser = playwright_instance.chromium.launch(headless=settings.headless)
    context = browser.new_context()
    page = context.new_page()

    login_page = LoginPage(page)
    login_page.open_login_page()
    login_page.login(
        username=settings.admin_username, 
        password=settings.admin_password
    )

    # Ensure login success
    assert login_page.is_dashboard_visible(), "Admin dashboard should be visible after successful login."
    context.storage_state(path=STORAGE_STATE_PATH)
    context.close()
    browser.close()

    return STORAGE_STATE_PATH

@pytest.fixture(scope="function")
def admin_page(browser, admin_storage_state):
    """
    Provide a page with admin user already logged in.
    """

    context = browser.new_context(storage_state=admin_storage_state)
    page = context.new_page()
    page.goto(settings.base_url)

    yield page
    
    context.close()