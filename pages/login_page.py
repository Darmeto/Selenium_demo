import locators.login_locators


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.myaccountbtn = locators.login_locators.LoginLocators.myAccBtn
        self.username_input = locators.login_locators.LoginLocators.usernameBox
        self.password_input = locators.login_locators.LoginLocators.passwordBox
        self.logInBtn = locators.login_locators.LoginLocators.login_Btn
        self.logout_link = locators.login_locators.LoginLocators.assertLogin
        self.error_msg = locators.login_locators.LoginLocators.errorMsg

    def open_page(self):
        self.driver.get("http://seleniumdemo.com/?page_id=7")

    def log_in(self, username, password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.logInBtn).click()

    def is_logout_link_displayed(self):
        return self.driver.find_element(*self.logout_link).is_displayed()

    def get_error_msg(self):
        return self.driver.find_element(*self.error_msg).is_displayed()
