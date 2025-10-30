from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time,os

options=webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)

sites=["https://www.wikipedia.org","https://www.github.com","https://www.python.org"]
os.makedirs("screenshots",exist_ok=True)
for site in sites:
    driver.get(site)
    time.sleep(2)
    filename=site.split("//")[1].replace(".","_")+".png"
    driver.save_screenshot(os.path.join("screenshots",filename))

driver.get("https://www.google.com")
search_box=driver.find_element(By.NAME,"q")
search_box.send_keys("Python Selenium automation")
search_box.send_keys(Keys.RETURN)
time.sleep(3)
driver.save_screenshot(os.path.join("screenshots","google_search.png"))

driver.quit()
print("Automation complete. Screenshots saved in /screenshots folder.")
