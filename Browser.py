from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.proxy import Proxy, ProxyType


chrome_options = webdriver.ChromeOptions()
def add_extensions(path,chrome_options = chrome_options):
    chrome_options.add_extension(path)

def start_browser():
    s = Service(r"chromedriver.exe")
    driver=webdriver.Chrome(service=s,options=chrome_options)
    driver.maximize_window()
    while(True):
        pass


    