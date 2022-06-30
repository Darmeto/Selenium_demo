from faker import Faker

from pages.billing_page import BillingPage
from pages.register_page import RegisterPage
import pytest


@pytest.mark.usefixtures("setup")
class TestBillingPage:

    def test_update_billing_page(self, setup):
        register_page = RegisterPage(self.driver)
        billing_page = BillingPage(self.driver)
        fake = Faker()
        register_page.open_page()
        register_page.register_page_elements(fake.email(), 'Test123456!@')
        billing_page.open_billing_page()
        billing_page.billing_page_personal_info(fake.first_name(), fake.last_name())
        billing_page.billing_page_company_info(fake.company())
        billing_page.billing_page_address_info(fake.address())
        billing_page.select_country("Poland")
        billing_page.billing_page_city_info(fake.city())
        billing_page.billing_page_postcode_info('57-300')
        billing_page.billing_page_phone_info('609609609')
        billing_page.save_billing_page_elements()
