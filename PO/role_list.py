from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

driver = webdriver.Chrome()
txtRoleName = driver.find_element(By.CSS_SELECTOR, "#txtRoleName")
btnSearch = driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
table = driver.find_element(By.CSS_SELECTOR, "#RoleList")
page_info = driver.find_element(By.CSS_SELECTOR, "#page")
