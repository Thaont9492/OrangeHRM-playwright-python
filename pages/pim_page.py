from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class PimPage(BasePage):

    # Navigation locators
    PIM_MENU = "a:has-text('PIM')"
    EMPLOYEE_ADD_BUTTON = "button:has-text(' Add ')"

    # Add Employee form locators
    FIRST_NAME_INPUT = "input[name='firstName']"
    MIDDLE_NAME_INPUT = "input[name='middleName']"
    LAST_NAME_INPUT = "input[name='lastName']"
    EMPLOYEE_ID_INPUT = "//div[@class='oxd-grid-2 orangehrm-full-width-grid']//input"

    # Login details form locators
    CREATE_LOGIN_DETAILS_TOGGLE = "span[class='oxd-switch-input']"

    # Validation error locators
    REQUIRED_ERROR = "//span[normalize-space()='Required']"

    # Validation duplicate employee ID error locator
    DUPLICATE_ID_ERROR = "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']"

    # Action button locators
    SAVE_BUTTON = "button[type='submit']"
    CANCEL_BUTTON = "button[type='button']"

    def __init__(self, page: Page):
        super().__init__(page)

    def navigate_to_pim(self):
        self.click(self.PIM_MENU)

    def click_add_employee(self):
        self.click(self.EMPLOYEE_ADD_BUTTON)

    def fill_employee_form(self, first_name: str, middle_name: str, last_name: str):
        self.fill(self.FIRST_NAME_INPUT, first_name)
        self.fill(self.MIDDLE_NAME_INPUT, middle_name)
        self.fill(self.LAST_NAME_INPUT, last_name)

    def submit_employee_form(self):
        self.click(self.SAVE_BUTTON)

    def create_employee(self, first_name: str, middle_name: str, last_name: str):
        self.fill_employee_form(first_name, middle_name, last_name)
        self.submit_employee_form()

    def get_employee_id(self) -> str:
        return self.page.locator(self.EMPLOYEE_ID_INPUT).input_value()

    def is_error_message_displayed(self) -> bool:
        try:
            expect(self.page.locator(self.REQUIRED_ERROR)).to_be_visible()
            return True
        except AssertionError:
            return False

    def is_duplicate_id_error_displayed(self) -> bool:
        try:
            expect(self.page.locator(self.DUPLICATE_ID_ERROR)).to_be_visible()
            return True
        except AssertionError:
            return False
