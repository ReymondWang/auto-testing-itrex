from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 

driver = webdriver.Chrome()
driver.get("http://localhost/admin/index.php?m=user&c=user&a=lists")
