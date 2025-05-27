from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


chrome_driver_path = r"C:\Development\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org")
# search = driver.find_element("name", "q")
# print(search.get_attribute("placeholder"))

event_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul li time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget ul li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
            "time": event_times[n].text,
            "name": event_names[n].text
        }
    # events.append(events[n])

print(events)
driver.quit()