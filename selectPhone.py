from selenium.webdriver.common.by import By


class SelectPhone:
    def __init__(self, driver):
        self.driver = driver
        self.phoneCategory = (By.XPATH, "//li[@id='sobe_d_b_8_3'] //img[@alt='Shop now']")
        self.phoneModel = (By.XPATH, "//span[text()='Xiaomi 13 Pro (Ceramic White, 12…']")

    def select_phoneCategory(self):
        self.driver.find_element(*self.phoneCategory).click()

    def select_phoneModel(self):
        self.driver.find_element(*self.phoneModel).click()
