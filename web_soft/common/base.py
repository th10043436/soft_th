#coding:utf-8
import time
from  selenium import  webdriver
from  selenium.webdriver.support.wait import  WebDriverWait
from  selenium.webdriver.common.by import By
from  selenium.webdriver.common.action_chains import  ActionChains
from  selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as  Ec
from  selenium.common.exceptions import  *

class Base(object):
    def __init__(self,driver:webdriver.Chrome):
        self.driver=driver

    def WebDriver_01(self,locator,timeout=4,t=0.6):
        if not isinstance(locator,tuple):
            print('locator 元素类型错误，必须是元组类型：loc=("id","value")')

        else:
            print('正在定位元素，定位方式key值: %s ,value值:%s'%(locator[0],locator[1]))

            try:
                ele=WebDriverWait(self.driver,timeout,t).until(lambda x:x.find_element(*locator))

                return ele
            except NoSuchElementException as  a:
                print('定位失败：%s',a)

    #判断alert 弹窗是否存在
    def ALEAR(self,timeout=5,t=0.5):
        try:
            result=self.driver.switch_to_alert()
            result.accept()
            return result.text
        except NoSuchElementException as a:
            print('没有alert 弹窗')
            return False



if __name__ == '__main__':
    driver=webdriver.Chrome()
    driver.get('https://www.baidu.com/')
    B=Base(driver)
    ele=B.WebDriver_01(('id','kw'))
    ele.send_keys('1111')
















