from three import twotwotwo
from appium import webdriver


def task(self):
    self.desired_caps2 = desired_caps2
    self.driver = webdriver.Remote('http://127.0.0.1:4726/wd/hub', desired_caps2)
    time.sleep(10)
    print('华为启动')
    self.driver.quit()