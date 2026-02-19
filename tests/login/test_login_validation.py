import pytest
from pages.login_page import LoginPage
from utils.config import settings

@pytest.mark.regression
@pytest.mark.validation
class TestLoginValidation:
    """Regression validation tests for login - negative scenarios."""

    def test_invalid_password(self, page):
        """Verify error message is displayed for invalid password."""
        login_page = LoginPage(page)

        login_page.open_login_page()
        login_page.login(
            username=settings.admin_username,
            password="wrongpassword"
        )

        assert login_page.is_error_visible(), "Error message should be visible for invalid login."
        assert "invalid" in login_page.get_error_message().lower(), "Error message should indicate invalid credentials."

    def test_empty_username(self, page):
        """Verify required field error is displayed for empty username."""
        login_page = LoginPage(page)

        login_page.open_login_page()
        login_page.login(
            username="",
            password=settings.admin_password
        )

        assert login_page.is_required_field_error_visible(), "Required field error should be visible for empty username."
