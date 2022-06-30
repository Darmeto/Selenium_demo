from selenium.webdriver.common.by import By


class LoginLocators:
    usernameBox = (By.ID, "username")
    passwordBox = (By.ID, "password")
    errorMsg = (By.XPATH, "//ul[@class='woocommerce-error']//li")
    errorText = "ERROR: Incorrect username or password."
    myAccBtn = (By.XPATH, "//li[@id='menu-item-22']//a")
    assertLogin = (By.LINK_TEXT, "Logout")
    login_Btn = (By.NAME, 'login')
