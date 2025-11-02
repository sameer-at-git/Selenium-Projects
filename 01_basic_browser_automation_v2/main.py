from selenium import webdriver
from selenium.webdriver import By 
browser = webdriver.Chrome()
browser.get("http://aiub.edu/")
#browser.quit()
browser.maximize_window()
title = browser.title
print(title)

#assert "AIUb" in title #assertion error

assert "AIUB" in title