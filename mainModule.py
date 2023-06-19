import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service



# Set up the ChromeDriver service
from miniAssignment4.AllMobilePhones import AllMobilePhones
from miniAssignment4.addToCart import AddToCart
from miniAssignment4.homePage import HomePageDetails
from miniAssignment4.selectPhone import SelectPhone
from miniAssignment4.shopByCategory import ShopByCategory

service_obj = Service("/usr/local/bin/chromedriver")

# Create a new instance of the Chrome driver
driver = webdriver.Chrome(service=service_obj)

# Navigate to Amazon.in
driver.get("https://www.amazon.in")
driver.maximize_window()
time.sleep(2)

# Create an instance of the HomePage class
home_page = HomePageDetails(driver)

# Click on the "All" tab
home_page.click_all_tabs()
time.sleep(2)
#all_tabs_page.click_all_tab()
#time.sleep(2)

home_page.scroll_to_all_tab()
time.sleep(5)

shop_by_category = ShopByCategory(driver)
shop_by_category.click_mobile_computer()
time.sleep(3)
shop_by_category.click_AllMobile_phones()
time.sleep(3)
# Close the browser

allMobile_phones = AllMobilePhones(driver)
allMobile_phones.navigate_To_MobileSection()
time.sleep(3)

phoneType = SelectPhone(driver)
phoneType.select_phoneCategory()
time.sleep(2)
phoneType.select_phoneModel()
time.sleep(2)


add_toCart = AddToCart(driver)
add_toCart.scroll_down()
time.sleep(2)

add_toCart.add_Product_ToCart()
time.sleep(2)

add_toCart.click_Cart()
time.sleep(2)

add_toCart.validate_CartCount()
time.sleep(1)












driver.quit()
