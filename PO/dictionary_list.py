from selenium import webdriver
from selenium.webdriver.common.by import By 

driver = webdriver.Chrome()
body = driver.find_element(By.TAG_NAME, 'body')
wrapper = driver.find_element(By.ID, 'wrapper')
gray_bg = driver.find_element(By.CLASS_NAME, 'gray-bg')
page_wrapper = driver.find_element(By.ID, 'page-wrapper')
body_inner = driver.find_element(By.ID, 'body')
