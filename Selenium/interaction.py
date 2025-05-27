from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


chrome_driver_path = r"C:\Development\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://secure-retreat-92358.herokuapp.com/")
fname = driver.find_element(By.NAME, 'fName')
lname = driver.find_element(By.NAME, 'lName')
email = driver.find_element(By.NAME, 'email')
sign_up = driver.find_element(By.CLASS_NAME, "btn")

fname.send_keys("Rojen")
lname.send_keys("Dangol")
email.send_keys("rojen@gmail.com")
sign_up.send_keys(Keys.ENTER)

time.sleep(5)
driver.quit()