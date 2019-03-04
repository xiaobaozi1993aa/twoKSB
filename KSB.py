from appium import webdriver
import threading
from selenium.webdriver.support.ui import WebDriverWait

def devices_message():
    desired_caps = {
                    'platformName': 'Android',
                    'deviceName': 'YGKBBBE642918622',   #华为
                    'platformVersion': '5.1',
                    'appPackage': 'com.sz.gcyh.KSHongBao',
                    'appActivity': 'com.sz.gcyh.KSHongBao.view.WelcomeAcitivity',
                    #'noReset': 'true',
                    'resetKeyboard': 'true',
                    'unicodeKeyboard': 'true'
                    }
    return desired_caps

def android_driver():
    driver = webdriver.Remote('http://127.0.0.1:4726/wd/hub', devices_message())
    return driver


def all_allow():
    def always_allow(self):
        number = 3
        for i in range(number):
            loc = ("xpath", "//*[@text='允许']")
            try:
                e = WebDriverWait(10, 0.5).until(EC.presence_of_element_located(loc))
                e.click()
            except:
                print('未找到')


print(dir())
