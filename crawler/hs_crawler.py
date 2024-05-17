from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, NoSuchElementException
from utils import find_all_a_elements, login_by_user, prun_html, save_dom_file, save_python_file, get_crawler_config, is_valid_file_name_part, format_py_code

import datetime
import furl
import os
import re

class HsCrawler(object):
  def __init__(self, config: dict) -> None:
    self.config = config

    # 这是一个需要访问的链接队列
    self.need_visit = [self.config["crawler"]["start-url"]]
    self.pure_url = []
    self.visited = []
    self.error_url = []

    self.load_temp_url()

    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
    self.wait = WebDriverWait(self.driver, 100)

    if self.config["gen-code"] == "Y":
      # 保存爬虫的窗口句柄
      self.crawler_window = self.driver.window_handles[-1]

      # 打开一个新的窗口，并用它来执行agent
      self.driver.execute_script("window.open('');")
      self.agent_window = self.driver.window_handles[-1]

      self.driver.switch_to.window(self.agent_window)
      agent_url = self.config["agent"]["url"]
      self.driver.get(agent_url)
    
  def get_html(self) -> None:
    if self.config["gen-code"] == "Y":
      self.driver.switch_to.window(self.crawler_window)

    black_list = self.config["crawler"]["black-list"]
    try:
      while len(self.need_visit) > 0:
        cur_href = self.need_visit.pop()
        if cur_href in black_list:
          print("----do not visit url in black list:" + cur_href + "----")
          continue
        
        self.visited.append(cur_href)
        print("----visit url:" + cur_href + "; remain size:" + str(len(self.need_visit)) + "----")
        self.driver.get(cur_href)

        raw_html = self.driver.page_source
        attrs_remove = self.config["crawler"]["prune"]["attrs"]
        tags_remove = self.config["crawler"]["prune"]["tags"]
        keep_one_child = self.config["crawler"]["prune"]["keep-one"]
        class_remove = self.config["crawler"]["prune"]["class"]
        pruned_html = prun_html(raw_html, attrs_to_remove=attrs_remove, tags_to_remove=tags_remove, keep_one_child=keep_one_child, class_remove=class_remove)
        saved_file_name = self.get_dom_file_name(cur_href)
        print("----" + saved_file_name + "----")
        save_dom_file(dom_source=pruned_html, file_name=saved_file_name)

        if self.is_page_error():
          self.error_url.append(cur_href)
          continue
        else:
          if self.config["gen-code"] == "Y":
            py_file_name = saved_file_name.replace("html", "py")
            self.get_code(pruned_html, file_name=py_file_name)

        if self.config["gen-code"] == "Y":
          self.driver.switch_to.window(self.crawler_window)
          
        self.collect_href()
        
        login_title = self.config["crawler"]["login"]["title"]
        if login_title == self.driver.title:
          username = self.config["crawler"]["login"]["username"]
          password = self.config["crawler"]["login"]["password"]

          login_by_user(self.driver, username, password, login_title)
          self.wait.until_not(EC.visibility_of_element_located((By.CLASS_NAME, "fa fa-refresh fa-spin")))
          self.collect_href()
    except Exception:
      # 如果发生异常，则把已经访问的url存放到临时文件中
      self.save_temp_url()

  def collect_href(self) -> None:
    _, a_list = find_all_a_elements(self.driver)
    for a in a_list:
      if self.url_filter(a):
          print(a)
          self.need_visit.append(a)
          self.pure_url.append(self.purify_url(a))

  def url_filter(self, url: str) -> bool:
    purified_url = self.purify_url(url)
    valid_patten = self.config["crawler"]["valid-patten"]
    return url \
      and url.startswith(valid_patten) \
      and purified_url not in self.pure_url
  
  def purify_url(self, url: str) -> str:
    f = furl.furl(url)
    f.args.clear()
    return str(f)
  
  def get_dom_file_name(self, url: str) -> str:
    f = furl.furl(url)

    if len(f.path.segments) == 0:
      return "login.html"
    elif "#" in url:
      last_path_segment = url.split("#")[1]
      lps_arr = last_path_segment.split("/")
      file_name = ""
      for lps in lps_arr:
        if lps and is_valid_file_name_part(lps):
          if file_name:
            file_name += "_"
          file_name += lps 
      file_name += ".html"
      return file_name
    else:
      last_path_segment = f.path.segments[-1]
      file_name = re.sub(r'(?<!^)(?=[A-Z])', '_', last_path_segment).lower()
      if not file_name.endswith(".html"):
        file_name = file_name + ".html"
      return file_name
  
  def save_visited_url(self) -> None:
    current_datetime = datetime.datetime.now()
    timestamp_str = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
    file_name = f"file_{timestamp_str}.txt"
    with open(file_name, 'w') as file:
      file.write("[visite url]")
      file.write("\n")
      for url in self.visited:
        file.write(url)
        file.write("\n")
      
      file.write("[error url]")
      file.write("\n")
      for url in self.error_url:
        file.write(url)
        file.write("\n")
    
    # 正确保存完结果后，要把中间结果删掉。
    if os.path.exists("temp.txt"):
      os.remove("temp.txt")
    
  def save_temp_url(self) -> None:
    with open("temp.txt", 'w') as file:
      for url in self.visited:
        file.write(url)
        file.write("\n")

  def load_temp_url(self) -> None:
    if os.path.exists("temp.txt"):
      with open("temp.txt", 'r') as file:
        for line in file:
          line = line.rstrip("\n")
          if line != '':
            self.visited.append(line)

  def is_page_error(self) -> bool:
    try:
      err_ele = self.driver.find_element(By.XPATH, "/html/body/div[1]/table/tbody/tr/td/table/tbody/tr[1]/td/div/font/b")
      return err_ele and err_ele.text == ":ERROR MESSAGE:"
    except NoSuchElementException:
      return False

  def get_code(self, html, file_name):
    self.driver.switch_to.window(self.agent_window)

    input_ele_loc = self.config["agent"]["input-ele"]
    response_ele_loc = self.config["agent"]["response-ele"]
    send_ele_loc = self.config["agent"]["send-ele"]
    refresh_ele_loc = self.config["agent"]["refresh-ele"]
    del_ele_loc = self.config["agent"]["del-ele"]

    del_ele = self.driver.find_element(By.XPATH, del_ele_loc)
    if not del_ele.get_attribute("disabled"):
      del_ele.click()
    
    input_ele = self.driver.find_element(By.XPATH, input_ele_loc)
    code_gen_msg = self.code_prompt(html)
    input_ele.send_keys(code_gen_msg)

    print(code_gen_msg)

    send_ele = self.driver.find_element(By.XPATH, send_ele_loc)
    refresh_ele = self.driver.find_element(By.XPATH, refresh_ele_loc)
    send_ele.click()
    self.wait.until(EC.element_to_be_clickable(refresh_ele))

    response_ele = self.driver.find_element(By.XPATH, response_ele_loc)
    formatted_code = format_py_code(response_ele.text)
    save_python_file(formatted_code, file_name=file_name)


  def code_prompt(self, msg):
    # prompt = "Please generate a PO object for automated testing based on the following HTML, and return only Python code in Python code format. "
    prompt = "请根据以下html生成自动化测试的PO对象，对象中要包括元素的定位以及基本操作，并且以Python代码的格式返回。在返回内容中不要添加文字解释，只返回代码即可。 "
    return prompt + msg


  def close(self) -> None:
    self.driver.quit()


if __name__ == "__main__":
  cur_path = os.path.abspath(__file__)
  cur_path = cur_path.replace("hs_crawler.py", "")
  path = os.path.join(cur_path, "../config/crawler.yml")
  config = get_crawler_config(path)
  crawler = HsCrawler(config=config)
  print("----started----")
  crawler.get_html()
  crawler.save_visited_url()
  crawler.close()