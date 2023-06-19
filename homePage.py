from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from miniAssignment4.AllTabs import AllTabs


class HomePageDetails:
    def __init__(self, driver):
        self.driver = driver
        self.all_tabs_link = (By.XPATH, "//a[@id='nav-hamburger-menu']")

    def click_all_tabs(self):
        self.driver.find_element(*self.all_tabs_link).click()
       # return AllTabs(self.driver)

    def scroll_to_all_tab(self):
        all_tab_element = self.driver.find_element(*self.all_tabs_link)
        ActionChains(self.driver).move_to_element(all_tab_element).perform()
        ActionChains(self.driver).key_down(Keys.ARROW_DOWN).perform()
