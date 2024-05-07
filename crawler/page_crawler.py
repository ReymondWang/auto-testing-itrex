from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

class PageCrawler(object):
  def __init__(self, url: str) -> None:
    self.driver = webdriver.Chrome()
    self.driver.get(url=url)
    self.wait = WebDriverWait(self.driver, 10)

  def get_all_element(self):
    html = self.driver.find_element(By.TAG_NAME, "html")
    # print(html.get_attribute("innerHTML"))
    for sub in html.children:
      print(sub.get_attribute("innerHTML"))


if __name__ == "__main__":
  crawler = PageCrawler(url="http://localhost:8080")
  crawler.get_all_element()