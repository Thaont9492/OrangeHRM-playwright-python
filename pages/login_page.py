from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from utils.config import settings

class LoginPage(BasePage):

    # Locators
    USERNAME_INPUT = "input[name='username']"
    PASSWORD_INPUT = "input[name='password']"
    LOGIN_BUTTON = "button[type='submit']"
    DASHBOARD_HEADER = "h6:has-text('Dashboard')"
    ERROR_MESSAGE = "div[role='alert']"
    REQUIRED_FIELD_ERROR = "span:has-text('Required')"
    USER_DROPDOWN = "p.oxd-userdropdown-name"
    LOGOUT_BUTTON = "a:has-text('Logout')"


    def __init__(self, page):
        super().__init__(page)

    def open_login_page(self):
        self.open(settings.base_url)

    def login(self, username: str, password: str):
        self.fill(self.USERNAME_INPUT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        self.page.wait_for_load_state("networkidle")

    def is_dashboard_visible(self) -> bool:
        try:
            expect(self.page.locator(self.DASHBOARD_HEADER)).to_be_visible()
            return True
        except AssertionError:
            return False

    def is_error_visible(self) -> bool:
        try:
            expect(self.page.locator(self.ERROR_MESSAGE)).to_be_visible()
            return True
        except AssertionError:
            return False

    def get_error_message(self) -> str:
        if self.page.locator(self.ERROR_MESSAGE).is_visible():
            return self.get_text(self.ERROR_MESSAGE)
        return ""

    def is_required_field_error_visible(self) -> bool:
        try:
            expect(self.page.locator(self.REQUIRED_FIELD_ERROR)).to_be_visible()
            return True
        except AssertionError:
            return False

    def logout(self):
        self.click(self.USER_DROPDOWN)
        self.click(self.LOGOUT_BUTTON)

    def is_login_page_visible(self) -> bool:
        try:
            expect(self.page.locator(self.LOGIN_BUTTON)).to_be_visible()
            return True
        except AssertionError:
            return False
