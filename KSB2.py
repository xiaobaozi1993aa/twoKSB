from KSB import *

a = android_driver()

def login():
    a.find_element_by_name('手机登录').click()
    print('调用')



if __name__ == '__main__':
    login()