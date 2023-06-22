import time
from webbrowser import Chrome

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from distutils import version


# Create fixture to launch the website and name the method as Setup
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
# define setup method and pass request as an argument which is an instance of fixture
def setup(request):
    service_obj = Service("/usr/local/bin/chromedriver")

    # Create a new instance of the Chrome driver
    driver = webdriver.Chrome(service=service_obj)

    # Launch flipkart website and maximize the window
    driver.get("https://www.flipkart.com")
    driver.maximize_window()
    driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2doB4z']").click()
    time.sleep(4)

    # To use the driver into test case file
    request.cls.driver = driver
    # Yield is used to tear down the browser once all the test cases will be executed
    yield

    driver.close()
