from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

class LoginPage:
  def init(self, driver):
    self.driver = driver 
    self.login_form = self.driver.find_element(By.ID, "formRegister")
    self.user_code_input = self.driver.find_element(By.NAME, "userCode")
    self.user_name_input = self.driver.find_element(By.NAME, "userName")
    self.email_input = self.driver.find_element(By.NAME, "email")
    self.password_input = self.driver.find_element(By.NAME, "password")
    self.register_button = self.driver.find_element(By.CLASS_NAME, "btn-primary")
    self.login_button = self.driver.find_element(By.CLASS_NAME, "btn-sm")

  def register(self, user_code, user_name, email, password):
    self.user_code_input.send_keys(user_code)
    self.user_name_input.send_keys(user_name)
    self.email_input.send_keys(email)
    self.password_input.send_keys(password)
    self.register_button.click()

  def login(self, user_code, password):
    self.user_code_input.send_keys(user_code)
    self.password_input.send_keys(password)
    self.login_button.click()

  def goto_register_page(self):
    self.login_form.find_element(By.TAG_NAME, "a").click()

  def goto_login_page(self):
    self.login_form.find_element(By.TAG_NAME, "a").click()