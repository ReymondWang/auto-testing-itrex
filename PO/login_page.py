from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # 页面元素定位器
    _USERNAME_INPUT = (By.NAME, "username")
    _PASSWORD_INPUT = (By.NAME, "password")
    _LOGIN_BUTTON = (By.XPATH, '//button[contains(text(), "登录")]')
    _FORGET_PASSWORD_LINK = (By.XPATH, '//a[contains(text(), "忘记密码？")]')
    _REGISTER_LINK = (By.XPATH, '//a[contains(text(), "注册新用户")]')

    @property
    def username_input(self):
        return self.driver.find_element(*self._USERNAME_INPUT)

    @property
    def password_input(self):
        return self.driver.find_element(*self._PASSWORD_INPUT)

    @property
    def login_button(self):
        return self.driver.find_element(*self._LOGIN_BUTTON)

    @property
    def forget_password_link(self):
        return self.driver.find_element(*self._FORGET_PASSWORD_LINK)

    @property
    def register_link(self):
        return self.driver.find_element(*self._REGISTER_LINK)

    def fill_username(self, username):
        self.username_input.clear()
        self.username_input.send_keys(username)

    def fill_password(self, password):
        self.password_input.clear()
        self.password_input.send_keys(password)

    def click_login(self):
        self.login_button.click()

    def click_forget_password(self):
        self.forget_password_link.click()

    def click_register(self):
        self.register_link.click()

    def wait_until_page_loaded(self):
        self.wait.until(EC.presence_of_element_located(self._LOGIN_BUTTON))

    def is_login_button_present(self):
        try:
            self.wait.until_not(EC.presence_of_element_located(self._LOGIN_BUTTON))
            return False
        except TimeoutException:
            return True

    def login(self, username, password):
        self.fill_username(username)
        self.fill_password(password)
        self.click_login()

    def navigate_to(self):
        self.driver.get("http://localhost:8080")  # 替换为实际登录页面URL
        self.wait_until_page_loaded()

if __name__ == "__main__":
    driver = webdriver.Chrome()  # 或使用其他浏览器驱动
    login_page = LoginPage(driver)
    login_page.navigate_to()

    # 执行登录操作
    login_page.login("admin", "123456")

    # 断言登录成功（此处仅为示例，实际断言需根据页面响应定制）
    assert login_page.is_login_button_present() is False  # 假设登录成功后登录按钮不再显示

    print(driver.current_url)

    driver.quit()