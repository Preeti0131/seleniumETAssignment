import time

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

service_obj = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service_obj)

# Navigate to Makemy trip web site using get() method
driver.get("https://www.makemytrip.com/")

# maximize the browser window
driver.maximize_window()
time.sleep(2)

driver.find_element(By.XPATH, "//body[@class='desktop in']").click()
time.sleep(5)
p= driver.window_handles[0]
#obtain browser tab window
driver.switch_to.window(p)
#close browser tab window


time.sleep(3)





# Select Round trip
driver.find_element(By.XPATH, "(//span[@class='tabsCircle appendRight5'])[2]").click()

# Select Bengaluru as From City

driver.find_element(By.XPATH, "//label[@for='fromCity']").click()

driver.find_element(By.XPATH, "//Input[@placeholder='From']").send_keys("Bengaluru, India")
time.sleep(3)
driver.find_element(By.XPATH, "//p[text()='Bengaluru, India']").click()

# To city and select Pune
driver.find_element(By.XPATH, "//label[@for='toCity']").click()

driver.find_element(By.XPATH, "//label[@for='toCity']").send_keys("pune")

driver.find_element(By.XPATH, "//p[text()='Pune, India']").click()
time.sleep(2)

# select departure as 4th July
driver.find_element(By.XPATH, "(//span[@class='lbl_input appendBottom10'])[1]").click()
driver.find_element(By.XPATH, "//div[@aria-label='Tue Jul 04 2023']").click()
time.sleep(2)
# select return date
driver.find_element(By.XPATH, "(//span[@class='lbl_input appendBottom10'])[2]").click()
driver.find_element(By.XPATH, "//div[@aria-label='Tue Jul 11 2023']").click()
time.sleep(2)

#select travel class
driver.find_element(By.XPATH, "(//span[@class='lbl_input appendBottom5'])").click()
driver.find_element(By.XPATH, "//li[@data-cy='adults-3']").click()
driver.find_element(By.XPATH, "//button[@data-cy='travellerApplyBtn']").click()
time.sleep(3)

# Click on Search
driver.find_element(By.XPATH, "//a[text()='Search']").click()
time.sleep(3)

driver.find_element(By.XPATH, "//div[@class='flightBody']").click()
#driver.find_element(By.XPATH, "//button[@class='button buttonSecondry buttonBig fontSize12 relative']").click()

#select values from Popular filters
# select Non stop
driver.find_element(By.XPATH, "(//div[@class='checkboxContent'])[1]").click()
# Select Late departures
driver.find_element(By.XPATH, "(//div[@class='checkboxContent'])[3]").click()


#select airlines as Indigo
driver.find_element(By.XPATH, "//p[@class='checkboxTitle'] [@xpath=12]").click()


text = driver.find_element(By.XPATH, "//span[@class='boldFont blackText'][text()='IndiGo ']").text
assert 'IndiGo ' in text







print("success")

driver.close()
