from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

driver = webdriver.Chrome()
txtRoleCode = driver.find_element(By.ID, "txtRoleCode")
txtRoleName = driver.find_element(By.NAME, "roleName")
btnSave = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
