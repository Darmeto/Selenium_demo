import locators.update_billing_locators
from selenium.webdriver.support.ui import Select


class BillingPage:
    def __init__(self, driver):
        self.driver = driver
        self.firstname = locators.update_billing_locators.BillingLocators.first_name
        self.lastname = locators.update_billing_locators.BillingLocators.last_name
        self.company = locators.update_billing_locators.BillingLocators.company
        self.address = locators.update_billing_locators.BillingLocators.address
        self.addressBtn = locators.update_billing_locators.BillingLocators.addressesBtn
        self.postcode = locators.update_billing_locators.BillingLocators.postcode
        self.city = locators.update_billing_locators.BillingLocators.city
        self.saveBtn = locators.update_billing_locators.BillingLocators.saveBtn
        self.country = locators.update_billing_locators.BillingLocators.country
        self.phone = locators.update_billing_locators.BillingLocators.phone
        self.edit = locators.update_billing_locators.BillingLocators.editBtn

    def open_billing_page(self):
        self.driver.find_element(*self.addressBtn).click()
        self.driver.find_element(*self.edit).click()

    def billing_page_personal_info(self, firstname, lastname):
        self.driver.find_element(*self.firstname).send_keys(firstname)
        self.driver.find_element(*self.lastname).send_keys(lastname)

    def billing_page_company_info(self, company):
        self.driver.find_element(*self.company).send_keys(company)

    def billing_page_address_info(self, address):
        self.driver.find_element(*self.address).send_keys(address)

    def select_country(self, country):
        select = Select(self.driver.find_element(*self.country))
        select.select_by_visible_text(country)

    def billing_page_postcode_info(self, postcode):
        self.driver.find_element(*self.postcode).send_keys(postcode)

    def billing_page_city_info(self, city):
        self.driver.find_element(*self.city).send_keys(city)

    def billing_page_phone_info(self, phone_number):
        self.driver.find_element(*self.phone).send_keys(phone_number)

    def save_billing_page_elements(self):
        self.driver.find_element(*self.saveBtn).click()
