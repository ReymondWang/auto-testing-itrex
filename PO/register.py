class LoginScreen: def init(self, driver): self.driver = driver def get_username_input(self): return self.driver.find_element(By.NAME, "userCode") def get_name_input(self): return self.driver.find_element(By.NAME, "userName") def get_email_input(self): return self.driver.find_element(By.NAME, "email") def get_password_input(self): return self.driver.find_element(By.NAME, "password") def get_register_button(self): return self.driver.find_element(By.CSS_SELECTOR, "button.btn.btn-primary.block.full-width.m-b") def get_login_link(self): return self.driver.find_element(By.CSS_SELECTOR, "a.btn.btn-sm.btn-white.btn-block") def is_login_screen_visible(self): return WebDriverWait(self.driver, 10).until(visibility_of_element_located((By.CSS_SELECTOR, "div.middle-box.text-center"))) def fill_login_form(self, user_code, user_name, email, password): self.get_username_input().send_keys(user_code) self.get_name_input().send_keys(user_name) self.get_email_input().send_keys(email) self.get_password_input().send_keys(password) def click_register_button(self): self.get_register_button().click() def click_login_link(self): self.get_login_link().click()