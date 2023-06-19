from selenium.webdriver.common.by import By


class AllTabs:
    def __init__(self, driver):
        self.driver = driver
        self.all_tab_link = (By.XPATH, "(//span[text()='All'])[2]")

    def click_all_tab(self):
        self.driver.find_element(*self.all_tab_link).click()

