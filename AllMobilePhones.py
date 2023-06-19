import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class AllMobilePhones:
    def __init__(self, driver):
        self.driver = driver

    def navigate_To_MobileSection(self):
        self.driver.execute_script("window.scrollTo(0, 1450);")
        time.sleep(4)
      #  self.nextPage = (By.CSS_SELECTOR, "//div[@class='sl-sobe-carousel-scroller'][@style='left: 505.064px;']")

   # def click_Next(self):
       # actions = ActionChains(self.driver)
      #  actions.move_to_element_with_offset(*self.nextPage, 0, 0).perform()
      #  self.driver.execute_script("arguments[0].scrollIntoView();", *self.nextPage)

        # Scroll the element to the right
      #  self.driver.execute_script("arguments[0].scrollLeft += 2000;", *self.nextPage)
       # time.sleep(3)




