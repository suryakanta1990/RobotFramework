import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Program Files\lib\chromedriver.exe")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://faarms.in/")
# driver.maximize_window()
# time.sleep(5)
driver.execute_script("window.scrollBy(0,500)")
time.sleep(5)
driver.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/div[3]/div[3]/div/div/div/a[1]/div/div/img").click()
