import time
from selenium import webdriver

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.set_window_size(1280,960)
    driver.get("https://weibo.com")
    time.sleep(5)
    loginname = driver.find_element_by_id('loginname')
    password = driver.find_element_by_xpath('//input[@name="password"]')

    loginname.send_keys('1339829613@qq.com')
    password.send_keys('580580')




