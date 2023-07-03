import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Firefox driver
driver = webdriver.Chrome()

# Navigate to the demoqa.com website
driver.get("https://demoqa.com/")
driver.maximize_window()
time.sleep(2)
wait = WebDriverWait(driver, 10)
# Click on 'Alerts, Frame & Windows' link
alerts_frame_windows_link = wait.until(
    EC.element_to_be_clickable((By.XPATH, "(//div[@class='card mt-4 top-card'])[3]"))
)

alerts_frame_windows_link.click()
time.sleep(4)
driver.execute_script("window.scrollTo(0, 250);")

# Click on 'Alert' link
alert_link = wait.until(EC.element_to_be_clickable((By.XPATH, "(//li[@id='item-1'])[2]")))
alert_link.click()
time.sleep(2)

# Click on 'Click me' button for the first alert
click_me_button_1 = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@id='alertButton']"))
)
click_me_button_1.click()
time.sleep(2)
alert_1 = driver.switch_to.alert
alert_1.accept()

# Click on 'Click me' button for the second alert
click_me_button_2 = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@id='timerAlertButton']"))
)
click_me_button_2.click()
time.sleep(3)
alert_2 = WebDriverWait(driver, 10).until(EC.alert_is_present())
alert_2.accept()
time.sleep(3)

# Click on 'Click me' button for the confirm box
click_me_button_confirm = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@id='confirmButton']"))
)
click_me_button_confirm.click()
alert_confirm = driver.switch_to.alert
alert_confirm.accept()
selected_option = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//span[@id='confirmResult']"))
)
# validating selected option is appearing
print("option:", selected_option.text)

# Click on 'Click me' button for the prompt box
click_me_button_prompt = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@id='promtButton']"))
)
click_me_button_prompt.click()
alert_prompt = driver.switch_to.alert

# validating given name
alert_prompt.send_keys("HashedIn by Deloitte")
alert_prompt.accept()
given_name = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "promptResult"))
)
print("name:", given_name.text)

# Close the browser
driver.quit()
