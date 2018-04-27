# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import json

def login_boss(driver):
    r"""login boss+(192.168.0.12) system without input or click
    :param driver: such as webdriver.Firefox()
    """
    host_url = "http://192.168.0.17/employee//authentication/login"
    login_url = "http://192.168.0.12/login.html"
    index_url = "http://192.168.0.12/index.html"
    data = {"login_name": "15527710855", "password": "9709fec10d3cc05914e3756130ece55c"}  #分析web界面发现对登录接口的关键因子是会话存储与本地存储中的数据，模拟登录后抓包分析传递的参数，post将固定参数写入，通过requests获取登录后的localStorage和sessionStorage
    headers = {"Content-Type": "application/json;charset=utf-8"}
    res = requests.post(host_url, headers=headers, data=json.dumps(data))
    result = res.json()
    currentUser = result["result"]["loginResultFormList"]
    authorization = result["result"]["authorizationResult"]
    a = json.dumps(currentUser)
    b = json.dumps(authorization)
    driver.get(login_url)
    time.sleep(2)
    driver.execute_script("sessionStorage.setItem('ngStorage-currentUser',  JSON.stringify(%s));" % a)  #在登录界面写入localStorage和sessionStorage，即可直接进入系统（json跟str互转可避免none报错）
    driver.execute_script("sessionStorage.setItem('ngStorage-authorization', JSON.stringify(%s));" % b)
    driver.execute_script("localStorage.setItem('md_ts', '1524719750850')")
    driver.get(index_url)

def click_login_boss(driver):
    r"""login boss+(192.168.0.12) system
    :param driver: such as webdriver.Firefox()
    """
    login_url = "http://192.168.0.12/index.html"
    driver.get(login_url)
    driver.maximize_window()
    time.sleep(2)
    driver.find_element_by_id("txtname").send_keys("15527710855")
    driver.find_element_by_id("txtpwd").send_keys("601140895@hzy")
    time.sleep(2)
    driver.find_element_by_id("btnlogin").click()
    time.sleep(2)


