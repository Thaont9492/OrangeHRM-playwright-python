import pytest
from utils.config import settings
from pages.pim_page import PimPage
from utils.data_generator import DataGenerator


@pytest.mark.regression
@pytest.mark.validation
class TestCreateEmployeeValidation:
    """Regression validation tests for creating employee - negative scenarios."""

    # def test_create_employee_missing_first_name(self, admin_page):
    #     """
    #     Regression test:
    #     Verify that creating an employee without a first name shows an error
    #     """

    #     pim_page = PimPage(admin_page)
    #     pim_page.navigate_to_pim()
    #     pim_page.click_add_employee()

    #     # Attempt to create employee with missing first name
    #     _, middle_name, last_name = DataGenerator.generate_employee_name()
    #     pim_page.create_employee("", middle_name, last_name)
    #     assert pim_page.is_error_message_displayed(), "Error message should be visible for missing field"

    def test_create_duplicate_employee_id(self, admin_page):
        """
        Regression test:
        Verify that creating an employee with a duplicate employee ID shows an error
        """

        pim_page = PimPage(admin_page)
        pim_page.navigate_to_pim()
        pim_page.click_add_employee()

        # Save the employee ID of the first created employee to attempt duplication
        employee_id = pim_page.get_employee_id()

        # Create first employee to get a valid employee ID
        first_name, middle_name, last_name = DataGenerator.generate_employee_name()
        pim_page.create_employee(first_name, middle_name, last_name)

        # Attempt to create another employee with the same ID
        pim_page.navigate_to_pim()
        pim_page.click_add_employee()
        
        
        pim_page.fill(pim_page.EMPLOYEE_ID_INPUT, employee_id)

        assert pim_page.is_duplicate_id_error_displayed(), "Error message should be visible for duplicate employee ID"
