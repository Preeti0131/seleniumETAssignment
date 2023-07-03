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

modal_dialogs_link = driver.find_element(By.XPATH, "(//li[@id='item-4'])[2]")
modal_dialogs_link.click()
time.sleep(2)

# Step 4: Click on small modal and validate the content and then click on close
small_modal_btn = driver.find_element(By.XPATH, "//button[text()='Small modal']")
small_modal_btn.click()
time.sleep(2)

# Wait for the modal content to load
wait = WebDriverWait(driver, 10)
modal_content = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='modal-content']")))
smallModalActualText = modal_content.text
print("Small Modal Content:", modal_content.text)

# Validate the small modal text
assert "This is a small modal" in smallModalActualText

close_btn = driver.find_element(By.XPATH, "//button[text()='Close']")
close_btn.click()
time.sleep(2)

# Step 5: Click on Large modal and validate the content and then click on close
large_modal_btn = driver.find_element(By.XPATH, "//button[text()='Large modal']")
large_modal_btn.click()
time.sleep(2)

# Wait for the modal content to load
modal_content = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@class='modal-content']")))
largeModalActualText = modal_content.text
print("Large Modal Content:", modal_content.text)

# # Validate the Large modal text
assert "Lorem Ipsum is simply dummy text of the printing and typesetting industry." in largeModalActualText

close_btn = driver.find_element(By.XPATH, "//button[text()='Close']")
close_btn.click()
time.sleep(2)

driver.quit()
