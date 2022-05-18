import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser= webdriver.Chrome()
browser.get("http://www.faarms.in")
browser.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/div[2]/div[6]/div[2]/div[1]/div[2]/button").click()
browser.implicitly_wait(10)
browser.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/div[2]/div[4]/div/div[2]/input").send_keys("7008425202")
browser.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/div[2]/div[4]/div/div[2]/button").click()
browser.find_element(By.CSS_SELECTOR,"svg[data-testid=AccountCircleIcon]").click()
browser.find_element(By.CSS_SELECTOR,"svg[data-testid=EditIcon").click()
browser.find_element(By.CSS_SELECTOR,"input.input-customer").send_keys("Suryakanta")
browser.find_element(By.XPATH,"//*[@id='root']/div/div/div[2]/div[4]/div/form/div/div/div[1]/label[2]/input").send_keys("Dash")
browser.find_element(By.CSS_SELECTOR,"input.input-customer[type=number]").send_keys("32")
browser.find_element(By.ID,"male").click()
browser.find_element(By.ID,"customer_btnSave").click()
time.sleep(3)
browser.find_element(By.LINK_TEXT,"Home").click()

