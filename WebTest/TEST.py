# -*- coding: utf-8 -*-

from selenium import webdriver
import time
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from AW import archer

browser = webdriver.Firefox()
archer.login_boss(browser)












