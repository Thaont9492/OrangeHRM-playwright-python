import pytest
from pages.login_page import LoginPage
from utils.config import settings

@pytest.mark.smoke
class TestLoginSmoke:
    """Smoke tests for login module - run on every MR."""

    def test_open_homepage(self, page):
        """Verify that the OrangeHRM homepage loads successfully."""
        page.goto(settings.base_url)
        assert page.title() == "OrangeHRM", "Homepage title does not match expected value."

    def test_admin_login(self, admin_page):
        """Verify admin session is valid and dashboard is visible."""
        assert "dashboard" in admin_page.url.lower()
