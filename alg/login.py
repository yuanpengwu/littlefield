import requests
from lxml import html
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from littlefield import Littlefield

class Login:
    def __init__(self,  user, pw, url):
        self._username = user
        self._password = pw
        self._url = url

    def process(self):
        web = webdriver.Chrome()
        web.get((self._url))
        username = web.find_element_by_name('id')
        username.send_keys(self._username)
        password = web.find_element_by_name('password')
        password.send_keys(self._password)
        ok = web.find_element_by_xpath("//input[@value='ok'][@type='submit']")
        ok.click()
        time.sleep(2)
        return web

'''
#url = "http://op.responsive.net/lt/ucsd2"
obj = Littlefield('group6', 'coronado91', session_id='5b6d82fb9e83f269e0acadeb9dff')
obj.process()
'''
