import unittest
from appium import webdriver
import time
import threading
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class onetwo():

    def caps(self):
        desired_caps2 = {
            'platformName': 'Android',
            'deviceName': 'FAHUNRAEHISS9HLV',  # 华为
            'platformVersion': '6.0',
            'appPackage': 'com.sz.gcyh.KSHongBao',
            'appActivity': 'com.sz.gcyh.KSHongBao.view.WelcomeAcitivity',
            # 'noReset': 'true',
            'resetKeyboard': 'true',
            'unicodeKeyboard': 'true'
        }
        return desired_caps2

    def task(self):
        dd = self.caps()
        self.driver = webdriver.Remote('http://127.0.0.1:4726/wd/hub',dd)
        time.sleep(10)
        print('华为启动')
        self.driver.quit()

    def always_allow(self):
        number = 3
        for i in range(number):
            loc = ("xpath", "//*[@text='允许']")
            try:
                e = WebDriverWait(10, 0.5).until(EC.presence_of_element_located(loc))
                e.click()
            except:
                print('未找到')

    def dog(self):
        task = self.task
        always_allow = self.always_allow
        threads = []
        t1 = threading.Thread(target=task)
        threads.append(t1)
        t2 = threading.Thread(target=always_allow())
        threads.append(t2)


