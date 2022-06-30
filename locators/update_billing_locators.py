from selenium.webdriver.common.by import By

class BillingLocators:
    addressesBtn = (By.LINK_TEXT, "Addresses")
    editBtn = (By.LINK_TEXT, "Edit")
    first_name = (By.ID, "billing_first_name")
    last_name = (By.ID, "billing_last_name")
    company = (By.ID, "billing_company")
    country = (By.ID, "billing_country")
    address = (By.ID, "billing_address_1")
    postcode = (By.ID, "billing_postcode")
    city = (By.ID, "billing_city")
    phone = (By.ID, "billing_phone")
    saveBtn = (By.NAME, "save_address")
    successAddressText = (By.XPATH, "//div[@class='woocommerce-message']")



