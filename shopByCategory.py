from selenium.webdriver.common.by import By


class ShopByCategory:
    def __init__(self, driver):
        self.driver = driver
        self.mobile_computer = (By.XPATH, "//div[text()='Mobiles, Computers']")
        self.allMobilePhones = (By.XPATH, "//a[text()='All Mobile Phones']")

    def click_mobile_computer(self):
        self.driver.find_element(*self.mobile_computer).click()
    # return AllTabs(self.driver)

    def click_AllMobile_phones(self):
        self.driver.find_element(*self.allMobilePhones).click()


