import pytest
from pages.pim_page import PimPage
from utils.data_generator import DataGenerator

@pytest.mark.smoke 
@pytest.mark.business 
def test_create_employee_smoke(admin_page):
    """
    Smoke test:
    Admin can create a new employee successfully
    """

    pim_page = PimPage(admin_page)
    pim_page.navigate_to_pim()
    pim_page.click_add_employee()

    first_name, middle_name, last_name = DataGenerator.generate_employee_name()
    pim_page.create_employee(first_name, middle_name, last_name)

    # Verify employee creation - the system redirects to the personal details page
    assert "viewpersonaldetails" in admin_page.url.lower()