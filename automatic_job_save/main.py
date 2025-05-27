from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

MY_EMAIL = "rojendangol1@gmail.com"
PASSWORD = "100daysofpython"

chrome_driver_path = r"C:\Development\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.linkedin.com/jobs/search?keywords=Python%20Developer&location=Kathmandu%2C%20Bāgmatī%2C%20Nepal"
           "&geoId=100665265&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")


# Wait and try to close the modal if it shows up
try:
    wait = WebDriverWait(driver, 10)
    close_button = wait.until(EC.element_to_be_clickable(
        (By.XPATH, '//*[@id="base-contextual-sign-in-modal"]//button')))
    close_button.click()
except:
    print("No modal appeared.")

sign_in_btn = driver.find_element(By.LINK_TEXT,"Sign in")
sign_in_btn.click()

email = driver.find_element(By.ID, "username")
email.send_keys(MY_EMAIL)
password = driver.find_element(By.ID, "password")
password.send_keys(PASSWORD)
password.send_keys(Keys.ENTER)

time.sleep(3)

all_jobs = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")

for job in all_jobs:
    job.click()
    try:
        save_btn = driver.find_element(By.CLASS_NAME, "jobs-save-button")
        save_btn.click()
        time.sleep(5)
    except NoSuchElementException:
        print("No save button. Skipped")
        continue

time.sleep(5)
driver.quit()