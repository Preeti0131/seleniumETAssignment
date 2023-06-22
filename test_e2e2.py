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
class Test_Flipkart1(BaseClass):
    # define first test case and pass setup as an argument to use fixture driver
    def test_case2(self, setup):
        object2 = FlipkartMacBook(self.driver)
        object2.addMacBook1()
        object2.addMacBook2()
        object2.compareMacBook()
        object2.validatePrice()
