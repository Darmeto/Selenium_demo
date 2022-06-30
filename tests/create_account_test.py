import pytest
from faker import Faker
from pages.register_page import RegisterPage


@pytest.mark.usefixtures("setup")
class TestRegister:

    def test_reg_in_passed(self, setup):
        fake = Faker()
        register_page = RegisterPage(self.driver)
        register_page.open_page()
        register_page.register_page_elements(fake.email(), 'Test123456!@')
        register_page.logout_link_is_displayed()

    def test_reg_in_failed(self, setup):
        register_page = RegisterPage(self.driver)
        register_page.open_page()
        register_page.register_page_elements('darmetkoqqq@wp.pl', 'Test123456!@')
        register_page.already_registered_msg()
