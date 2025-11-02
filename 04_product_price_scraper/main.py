from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

driver=webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
time.sleep(2)

driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.ID,"password").send_keys("secret_sauce")
driver.find_element(By.ID,"login-button").click()
time.sleep(2)

products=driver.find_elements(By.CLASS_NAME,"inventory_item")
data=[]

for p in products:
    name=p.find_element(By.CLASS_NAME,"inventory_item_name").text
    price=p.find_element(By.CLASS_NAME,"inventory_item_price").text
    data.append([name,price])

with open("prices.csv","w",newline="",encoding="utf-8") as f:
    writer=csv.writer(f)
    writer.writerow(["Product","Price"])
    writer.writerows(data)
    
driver.quit()
