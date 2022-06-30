import pytest
from pages.login_page import LoginPage
from faker import Faker


@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_login_passed(self, setup):
        login_page = LoginPage(self.driver)
        login_page.open_page()
        login_page.log_in('darmetkoqqq@wp.pl', 'Test123456!@')
        assert login_page.is_logout_link_displayed() is True

    def test_login_failed(self, setup):
        fake = Faker()
        login_page = LoginPage(self.driver)
        login_page.open_page()
        login_page.log_in(fake.name(), 'Test123456!@')
        assert login_page.get_error_msg() is True
