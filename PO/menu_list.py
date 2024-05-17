from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 

driver = webdriver.Chrome()
driver.get("http://example.com/")
dict_type_link = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//a[@name='D00001']")))
dict_type_link.click()
