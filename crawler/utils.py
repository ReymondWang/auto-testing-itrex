from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, JavascriptException
from bs4 import BeautifulSoup, NavigableString

import time
import yaml
import lxml.html
import os
import re

def get_crawler_config(file_path: str):
    with open(file_path, 'r') as file:
        try:
            data = yaml.safe_load(file)
            return data
        except yaml.YAMLError as exc:
            print(f"Error parsing YAML file {file_path}: {exc}")
            return None


def find_all_a_elements(driver: WebDriver, element: WebElement=None) -> list[WebElement]:
    """
    递归查找页面上所有<a>元素。

    Args:
        driver (webdriver.Chrome|webdriver.Firefox): Selenium WebDriver实例。
        element (WebElement, optional): 当前递归层次的父元素，默认为None，表示从根节点开始。

    Returns:
        List[WebElement]: 页面上所有<a>元素的列表。
        List[str]: 页面所有<a>元素的href。
    """
    if element is None:
        # 如果element未指定，从文档根节点开始
        element = driver.find_element(By.TAG_NAME, "html")

    # 获取当前元素的所有子节点
    child_elements = element.find_elements(By.XPATH, "./*")

    a_elements = []
    a_href = []
    cnt = 0
    while cnt < 3:
        try:
            for child in child_elements:
                # 检查当前子节点是否为<a>元素
                if child.tag_name.lower() == 'a':
                    a_elements.append(child)
                    a_href.append(child.get_attribute("href"))

                # 对非叶子节点进行递归查找
                if len(child.find_elements(By.XPATH, "./*")) > 0:
                    sub_ele, sub_href = find_all_a_elements(driver, child)
                    a_elements.extend(sub_ele)
                    a_href.extend(sub_href)
            
            break
        except (StaleElementReferenceException, JavascriptException):
            time.sleep(1) # 页面元素刷新了等待1s后，再次获取。
            cnt += 1
            child_elements = element.find_elements(By.XPATH, "./*")
            a_elements = []
            a_href = []

    return a_elements, a_href


def prun_html(page_source, attrs_to_remove=None, tags_to_remove=None, keep_one_child=None, class_remove=None) -> str:
    """
    对HTML源代码进行剪枝和简化操作。

    Args:
        page_source (str): 要处理的HTML源代码。
        attrs_to_remove (list): 要清除的属性名称列表。
        tags_to_remove (list): 要清除的标签名称列表。
        keep_one_child (list): 只保留一个子元素的标签列表。

    Returns:
        str: 剪枝和简化以后的HTML源代码。
    """
    soup = BeautifulSoup(page_source, 'html.parser')

    if attrs_to_remove is None:
        attrs_to_remove = []
    if tags_to_remove is None:
        tags_to_remove = []
    if keep_one_child is None:
        keep_one_child = []
    if class_remove is None:
        class_remove = []

    to_decompose = []
    for tag in soup.find_all():
        class_name = ""
        class_arr = tag.get("class")
        if class_arr:
            for cls in class_arr:
                if class_name:
                    class_name += " "
                class_name += cls

        for attr in attrs_to_remove:
            if attr in tag.attrs:
                del tag[attr]
        if tag.name in tags_to_remove or class_name in class_remove:
            to_decompose.append(tag)
        if tag.name in keep_one_child:
            children = list(tag.children)
            non_empty_children = [child for child in children if child != '\n' and not isinstance(child, str) or child.strip()]
            if len(non_empty_children) > 0:
                first_child = non_empty_children[0]
                tag.clear()
                tag.append(first_child)
        if isinstance(tag, NavigableString):  # 检查是否为文本节点
            new_string = ' '.join(tag.strip().split())  # 去除多余空格，保留单词间单个空格
            tag.replace_with(NavigableString(new_string))  # 用处理后的字符串替换原字符串

    for tag in to_decompose:
        tag.extract()

    pruned_html = soup.prettify()
    single_line_html = pruned_html.replace('\n', '')
    pattern = re.compile(r'(\S)\s+(\S)')
    single_line_html = pattern.sub(r'\1 \2', single_line_html) # 将匹配到的多个空格替换为一个半角空格
    single_line_html = re.sub(r">( *)<", '><', single_line_html)  # 移除标签之间的空格

    return single_line_html


def save_dom_file(dom_source: str, file_name: str, path: str="../dom") -> None:
    cur_path = os.path.abspath(__file__)
    cur_path = cur_path.replace("utils.py", "")
    path = os.path.join(cur_path, path)
    file_path = os.path.join(path, file_name)

    with open(file_path, 'w') as file:
        file.write(dom_source)


def login_by_user(driver: WebDriver, user_login_id: str, password: str, title: str=None):
    if title and title != driver.title:
        raise Exception("URL:" + driver.current_url + "不是登录页面")
    
    ele_username = driver.find_element(By.XPATH, "/html/body/div/div/form/div[1]/input")
    ele_password = driver.find_element(By.XPATH, "/html/body/div/div/form/div[2]/input")
    btn_login = driver.find_element(By.XPATH, '/html/body/div/div/form/button')

    ele_username.send_keys(user_login_id)
    ele_password.send_keys(password)
    btn_login.click()


def is_valid_file_name_part(s):
    return not bool(re.search(r'\d', s)) \
        and "null" != s \
        and "system" != s