from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

driver = webdriver.Chrome()
txtUserName = driver.find_element(By.ID, "txtUserName")
txtPhone = driver.find_element(By.ID, "txtPhone")
btnSearch = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
form = driver.find_element(By.ID, "fromCondition")
