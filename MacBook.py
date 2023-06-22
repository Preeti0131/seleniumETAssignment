import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utilities.BaseClass import BaseClass


class FlipkartMacBook(BaseClass):
    def __init__(self, driver):
        # first item details
        self.driver = driver
        # first macbook details
        self.searchProduct = (By.XPATH, "//input[@class='_3704LK']")
        self.productName1 = (By.XPATH, "(//div[@class='_4rR01T'])[1]")
        self.productPrice1 = (By.XPATH, "(//div[@class='_30jeq3 _1_WHN1'])[1]")

        # second macbook details
        self.productName2 = (By.XPATH, "(//div[@class='_4rR01T'])[2]")
        self.productPrice2 = (By.XPATH, "(//div[@class='_30jeq3 _1_WHN1'])[1]")
        self.addToCart = (By.XPATH, "//button[@class='_2KpZ6l _2U9uOA _3v1-ww']")

        # Compare mac book buttons
        self.addToCompare1 = (By.XPATH, "(//label[@class='_6Up2sF'])[1]")
        self.addToCompare2 = (By.XPATH, "(//label[@class='_6Up2sF'])[2]")
        self.compare = (By.XPATH, "//span[@class='_3hShhO']")

        # product price details on Compare screen
        self.price1 = (By.XPATH, "(//div[@class='_30jeq3'])[1]")
        self.price2 = (By.XPATH, "(//div[@class='_30jeq3'])[2]")

    def addMacBook1(self):
        log = self.get_logger()
        macBook = self.driver.find_element(*self.searchProduct)
        macBook.clear()
        macBook.send_keys("Mac book pro 2023")
        macBook.send_keys(Keys.ENTER)
        time.sleep(5)
        itemValue = macBook.text
        log.info(itemValue)
        time.sleep(5)

        # macbook1 details
        product1_name = self.driver.find_element(*self.productName1).text
        product1_price = self.driver.find_element(*self.productPrice1).text
        log.info(product1_name)
        log.info(product1_price)

        # add first item to cart
        current_window = self.driver.current_window_handle
        self.driver.find_element(*self.productName1).click()

        for window_handle in self.driver.window_handles:
            if window_handle != current_window:
                self.driver.switch_to.window(window_handle)
                break
        self.driver.find_element(*self.addToCart).click()
        time.sleep(2)

        self.driver.close()

        # switch to previous window
        self.driver.switch_to.window(current_window)
        time.sleep(2)

    def addMacBook2(self):
        time.sleep(5)
        # macbook1 details
        product2_name = self.driver.find_element(*self.productName2).text
        product2_price = self.driver.find_element(*self.productPrice2).text
        print("MacBook product2 name: ", product2_name)
        print("Macbook product2 price: ", product2_price)

        # add first item to cart
        current_window = self.driver.current_window_handle
        self.driver.find_element(*self.productName2).click()

        for window_handle in self.driver.window_handles:
            if window_handle != current_window:
                self.driver.switch_to.window(window_handle)
                break
        self.driver.find_element(*self.addToCart).click()
        time.sleep(2)

        self.driver.close()

        # switch to previous window
        self.driver.switch_to.window(current_window)
        time.sleep(2)

    def compareMacBook(self):
        self.driver.find_element(*self.addToCompare1).click()
        time.sleep(2)
        self.driver.find_element(*self.addToCompare2).click()
        time.sleep(2)
        self.driver.find_element(*self.compare).click()
        time.sleep(3)
        self.driver.execute_script("window.scrollBy(0, 2000);")
        time.sleep(5)

    def validatePrice(self):
        price1 = self.driver.find_element(*self.price1).text
        price2 = self.driver.find_element(*self.price2).text

        if price1 != price2:
            print("The price of both the macbooks are different")
        else:
            print("The price of both the macbooks are same")
