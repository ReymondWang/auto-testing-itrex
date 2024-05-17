from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

driver = webdriver.Chrome()
txtParentCode = driver.find_element(By.CSS_SELECTOR, "#txtParentCode")
txtFunctionCode = driver.find_element(By.CSS_SELECTOR, "#txtFunctionCode")
txtFunctionName = driver.find_element(By.CSS_SELECTOR, "#txtFunctionName")
txtRequestPath = driver.find_element(By.CSS_SELECTOR, "#txtRequestPath")
btnSave = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
