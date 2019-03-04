from config import gogo_caps,gogo_caps2
import threading
import time
from appium import webdriver
class twotwotwo():
    def dog(self):
        desired_caps = gogo_caps
        return webdriver.Remote('http://127.0.0.1:4726/wd/hub', desired_caps)
    def cat(self):
        desired_caps = gogo_caps2
        return webdriver.Remote('http://127.0.0.1:4725/wd/hub', desired_caps)

