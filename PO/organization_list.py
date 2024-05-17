from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class AddNewNode:
  def init(self, driver):
    self.driver = driver
    
  def add_new_node(self): # 点 击 新 增 按 钮 
       self.driver.find_element(By.ID, "btnAdd").click()
