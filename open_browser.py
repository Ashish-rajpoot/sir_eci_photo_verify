from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import os
import time

profile_path = os.path.abspath("chrome_profile_eci")

options = Options()
options.add_argument(f"--user-data-dir={profile_path}")
options.add_argument("--start-maximized")
options.add_experimental_option("detach", True)

url = "https://officials.eci.gov.in/aero"
# LOGIN DETAIL
userIdStr="AEROS24A231N19"
passWdStr="Mahoba@123"

driver = webdriver.Chrome(options=options)
driver.maximize_window()
wait = WebDriverWait(driver,20)
driver.get(url)

time.sleep(5)

print("Current URL:", driver.current_url)

def element_exists(by, value):
    try:
        driver.find_element(by, value)
        return True
    except NoSuchElementException:
        return False

# Example: check login page elements
if element_exists(By.TAG_NAME, "input"):
    page_text = driver.page_source.lower()

    if "otp" in page_text or "request otp" in page_text or "captcha" in page_text:
        print("Session not available. Please login manually.")
        userIdBox = wait.until(EC.visibility_of_element_located((By.NAME,"userId")))
        userIdBox.clear()
        userIdBox.send_keys(userIdStr)
    else:
        print("Maybe logged in, but confirm with dashboard element.")
else:
    print("No input fields found. Possibly already logged in.")

wait.until(
    EC.element_to_be_clickable(
    (By.XPATH,'//*[@id="textContent"]/div[2]/div/a[1]')
    )
).click()
wait.until(
    EC.element_to_be_clickable(
    (By.XPATH,'//*[@id="textContent"]/div[2]/div/div[2]/div/div/div[5]/div[2]/a')
    )
).click()