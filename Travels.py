import time

from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FlipkartTravels:
    def __init__(self, driver):
        # first item details
        self.driver = driver
        self.travels = (By.XPATH, "(//img[@class='_396cs4'])[7]")
        self.roundTrip = (By.XPATH, "(//div[@class='_1XFPmK'])[2]")
        self.fromLocation = (By.XPATH, "(//div[@class='_3qBKP_ _1Jqgld'])[1]")
        self.toLocation = (By.XPATH, "(//div[@class='_3qBKP_ _1Jqgld'])[2]")
        self.departOn = (By.XPATH, "(//input[@class='_1w3ZZo _2gKfhi _2mFmU7'])[1]")
       # self.returnOn = (By.XPATH, "(//input[@class='_1w3ZZo _2gKfhi _2mFmU7'])[2]")
        self.returnDay = (By.XPATH, "//label[text()='Return On']")

        self.fromDate = (By.XPATH, "(//button[@class='jkj0H4'])[32]")
        self.toDate = (By.XPATH, "(//button[@class='jkj0H4'])[34]")
        self.done = (By.XPATH, "//button[@class='aC49_F _14Me7y']")
        self.search = (By.XPATH, "//button[@class='_2KpZ6l _1QYQF8 _3dESVI']")
        self.selectFlight = (By.XPATH, "(//div[@class='_3Z56kU'])[1]")
        self.fromFlightPrice = (By.XPATH, "(//div[@class='_1AhVAh'])[1]")
        self.toFlightPrice = (By.XPATH, "(//div[@class='_1AhVAh'])[102]")
        self.totalPrice = (By.XPATH, "//span[@class='_1YryzD']")

    def bookFlightTicket(self):
        try:
            # Switch to the alert dialog
            alert = self.driver.switch_to.alert

            # Get the text of the alert
            alert_text = alert.text

            # Perform the desired action (e.g., accepting the alert)
            alert.accept()

            # Handle the alert as per your test case requirements

        except Exception as e:
            # Handle any other exceptions or error handling logic
            print(f"An exception occurred: {e}")
        time.sleep(2)
        self.driver.find_element(*self.travels).click()
        time.sleep(2)
        self.driver.find_element(*self.roundTrip).click()
        time.sleep(3)
        # fromLocation = self.driver.find_element(*self.fromLocation)
        wait = WebDriverWait(self.driver, 20)
        element1 = wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='_3qBKP_ _1Jqgld'])[1]")))
        actions = ActionChains(self.driver)

        # Move to the target element and press the down arrow key
        actions.move_to_element(element1).send_keys(Keys.ARROW_DOWN).perform()

        element1.click()
        # press enter
        # self.driver.execute_script("arguments[0].scrollIntoView();", element1)
        #  element1.send_keys(Keys.ENTER)
        # fromLocation.send_keys("Bangalore")

        # select To location
        # toLocation = self.driver.find_element(*self.toLocation)
        wait = WebDriverWait(self.driver, 20)
        element2 = wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='_3qBKP_ _1Jqgld'])[2]")))
        actions = ActionChains(self.driver)

        # Move to the target element and press the down arrow key
        actions.move_to_element(element2).send_keys(Keys.ARROW_DOWN).perform()
        actions.move_to_element(element2).send_keys(Keys.ARROW_DOWN).perform()
        element2.click()

        # Simulate pressing the Enter key

        time.sleep(2)

        # select departure and return date
        self.driver.find_element(*self.departOn).click()
        time.sleep(2)
        self.driver.find_element(*self.fromDate).click()
        time.sleep(4)
        # wait = WebDriverWait(self.driver, 20)
        #   self.driver.find_element(*self.returnDay).click()
        # element = wait.until(EC.element_to_be_clickable(returnOn))
        self.driver.find_element(*self.returnDay).click()
        # element.click()

        self.driver.find_element(*self.toDate).click()
        time.sleep(2)

        # Click Done
        #   self.driver.find_element(*self.done).click()
        time.sleep(2)

        # click search
        searchButton = self.driver.find_element(*self.search)
        element3 = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//button[@class='_2KpZ6l _1QYQF8 _3dESVI']")))

        element3.click()

        time.sleep(5)

        # Select flight
        self.driver.find_element(*self.selectFlight).click()

        # need to validate price details now
