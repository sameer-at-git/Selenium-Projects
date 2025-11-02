from selenium import webdriver
from selenium.webdriver.common.by import By
import time,csv

driver=webdriver.Chrome()
driver.get("https://quotes.toscrape.com/scroll")
time.sleep(2)

last_height=driver.execute_script("return document.body.scrollHeight")
while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
    time.sleep(2)
    new_height=driver.execute_script("return document.body.scrollHeight")
    if new_height==last_height:
        break
    last_height=new_height
quotes=driver.find_elements(By.CLASS_NAME,"quote")

data=[]

for q in quotes:
    text=q.find_element(By.CLASS_NAME,"text").text
    author=q.find_element(By.CLASS_NAME,"author").text
    data.append([text,author])

with open("quotes.csv","w",newline="",encoding="utf-8") as f:
    writer=csv.writer(f)
    writer.writerow(["Quote","Author"])
    writer.writerows(data)
    
driver.quit()
