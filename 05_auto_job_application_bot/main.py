from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import time

driver=webdriver.Chrome()
driver.get("https://realpython.github.io/fake-jobs/")
time.sleep(2)
data=[]
job_count=len(driver.find_elements(By.CLASS_NAME,"card-content"))
for i in range(job_count):
    jobs=driver.find_elements(By.CLASS_NAME,"card-content")
    j=jobs[i]
    title=j.find_element(By.XPATH,".//h2").text
    company=j.find_element(By.XPATH,".//h3[@class='subtitle is-6 company']").text
    location=j.find_element(By.XPATH,".//p[@class='location']").text
    date=j.find_element(By.TAG_NAME,"time").get_attribute("datetime")
    link=j.find_element(By.LINK_TEXT,"Apply").get_attribute("href")
    data.append([title,company,location,date,link])
with open("jobs.csv","w",newline="",encoding="utf-8") as f:
    writer=csv.writer(f)
    writer.writerow(["Job Title","Company","Location","Date","Apply Link"])
    writer.writerows(data)
for i in range(len(data)):
    driver.get("https://realpython.github.io/fake-jobs/")
    time.sleep(2)
    jobs=driver.find_elements(By.CLASS_NAME,"card-content")
    j=jobs[i]
    j.find_element(By.LINK_TEXT,"Apply").click()
    print(f"Applied Job Number {i+1}")
    time.sleep(2)
    driver.back()
    time.sleep(1)

driver.quit()