import locators.register_locators
from locators.register_locators import RegisterLocators


class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.email = locators.register_locators.RegisterLocators.emailBox
        self.password = locators.register_locators.RegisterLocators.passwordBox
        self.register_button = locators.register_locators.RegisterLocators.registerButton
        self.logout_text = locators.register_locators.RegisterLocators.logoutText
        self.error = locators.register_locators.RegisterLocators.error_msg

    def open_page(self):
        self.driver.get("http://seleniumdemo.com/?page_id=7")

    def register_page_elements(self, email, password):
        self.driver.find_element(*self.email).send_keys(email)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.register_button).click()

    def logout_link_is_displayed(self):
        return self.driver.find_element(*self.logout_text).is_displayed()

    def already_registered_msg(self):
        return self.driver.find_element(*self.error).is_displayed()

