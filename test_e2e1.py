import selenium

import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By
from distutils import version

from testCaseBaseFiles.FlipkartAdd3Items import FlipKart
from testCaseBaseFiles.MacBook import FlipkartMacBook

from testCaseBaseFiles.Travels import FlipkartTravels
from utilities.BaseClass import BaseClass


# define child class inheriting the properties of Base class which helps to call fixture
class Test_Flipkart(BaseClass):
    # define first test case and pass setup as an argument to use fixture driver

    def test_case1(self, setup):
        object1 = FlipKart(self.driver)
        object1.select_firstItem()
        object1.select_secondItem()
        object1.select_thirdItem()
        object1.validate_CartItems()














