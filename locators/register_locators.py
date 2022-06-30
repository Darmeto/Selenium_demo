from selenium.webdriver.common.by import By


class RegisterLocators:
    myAcc_button = (By.XPATH, "//li[@id='menu-item-22']//a")
    emailBox = (By.ID, "reg_email")
    passwordBox = (By.ID, "reg_password")
    registerButton = (By.NAME, "register")
    logoutText = (By.LINK_TEXT, "Logout")
    error_msg = (By.XPATH, "//ul[@class='woocommerce-error']//li")
