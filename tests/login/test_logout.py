import pytest
from pages.login_page import LoginPage
from utils.config import settings

@pytest.mark.regression
class TestLogout:
    """Regression tests for logout functionality."""

    def test_logout(self, page):
        """Verify user can log out and is redirected to login page."""
        login_page = LoginPage(page)

        login_page.open_login_page()
        login_page.login(
            username=settings.admin_username,
            password=settings.admin_password
        )

        assert login_page.is_dashboard_visible()

        login_page.logout()

        assert login_page.is_login_page_visible(), "Login page should be visible after logout."
