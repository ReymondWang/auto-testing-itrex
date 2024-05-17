from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
  def init(self, driver):
    self.driver = driver 
    self.username_input = self.driver.find_element(By.NAME, 'username')
    self.password_input = self.driver.find_element(By.NAME, 'password')
    self.login_button = self.driver.find_element(By.CLASS_NAME, 'btn-primary')
    self.register_link = self.driver.find_element(By.CLASS_NAME, 'btn-sm.btn-white.btn-block')
    def input_username(self, username):
      self.username_input.send_keys(username)
    def input_password(self, password):
      self.password_input.send_keys(password)
    def click_login_button(self):
      self.login_button.click()
    def click_register_link(self):
      self.register_link.click()
    def is_login_page_loaded(self):
      return self.driver.find_element(By.CLASS_NAME, 'logo-name')
    def is_register_link_present(self):
      return self.register_link.is_displayed()
    def is_login_button_present(self):
      return self.login_button.is_displayed()
    def is_username_input_present(self):
      return self.username_input.is_displayed()
    def is_password_input_present(self):
      return self.password_input.is_displayed()