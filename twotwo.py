from appium import webdriver
import time
import threading
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.multi_action import MultiAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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
desired_caps2 = {
                'platformName': 'Android',
                'deviceName': 'FAHUNRAEHISS9HLV',   #小米
                'platformVersion': '6.0',
                'appPackage': 'com.sz.gcyh.KSHongBao',
                'appActivity': 'com.sz.gcyh.KSHongBao.view.WelcomeAcitivity',
                #'noReset': 'true',
                'resetKeyboard': 'true',
                'unicodeKeyboard': 'true'
                }

def task():
    driver = webdriver.Remote('http://127.0.0.1:4726/wd/hub', desired_caps2)
    time.sleep(15)
    print('华为启动')
    driver.find_element_by_name('手机登录').click()
    print('------------------点击登录----------------------')
    driver.find_element_by_name('请输入手机号').send_keys(13066909086)
    print('---------------输入手机号-------------------------------')

def task1():
    driver = webdriver.Remote('http://127.0.0.1:4725/wd/hub', desired_caps)
    time.sleep(10)
    print('小米启动')
    driver.find_element_by_name('手机登录').click()
    print('------------------点击登录----------------------')
    driver.find_element_by_name('请输入手机号').send_keys(18312486990)
    print('---------------输入手机号-------------------------------')

def always_allow(number=3):
    for i in range(number):
        loc = ("xpath", "//*[@text='允许']")
        try:
            e = WebDriverWait(10,0.5).until(EC.presence_of_element_located(loc))
            e.click()
        except:
            print('未找到')

threads = []
t1 = threading.Thread(target=task)
threads.append(t1)

t2 = threading.Thread(target=task1)
threads.append(t2)

t3 = threading.Thread(target=always_allow)
threads.append(t3)

if __name__ == '__main__':
    for t in threads:
        t.start()
