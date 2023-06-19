import time
import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AddToCart(unittest.TestCase):
    def __init__(self, driver):
        self.driver = driver
        self.addToCartButton = (By.XPATH, "//input[@id='add-to-cart-button']")
        self.cartCount = (By.XPATH, "//span[@id='nav-cart-count']")
        self.cartValue = (By.XPATH, "//span[@class='a-dropdown-prompt']")

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, 1450);")
        time.sleep(4)

    def add_Product_ToCart(self):
        self.driver.find_element(*self.addToCartButton).click()

    def click_Cart(self):
        # self.driver.find_element(*self.cartCount).click()

        self.driver.find_element(*self.cartCount).click()

    def validate_CartCount(self):
        cart_Value = self.driver.find_element(*self.cartValue).text
        print(cart_Value)
    # self.assertEqual(cart_Value, expected_cartValue)
