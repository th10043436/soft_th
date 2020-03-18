#coding:utf-8
import time
from  selenium import  webdriver
from  selenium.webdriver.support.wait import  WebDriverWait
from  selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from  selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as  Ec
from  selenium.common.exceptions import  *
import  multiprocessing


class Base(object):
    def __init__(self,driver:webdriver.Chrome):
        self.driver=driver

    #显性等待
    def WebDriver_01(self,locator,timeout=4,t=0.6):
        if not isinstance(locator,tuple):
            print('locator 元素类型错误，必须是元组类型：loc=("id","value")')

        else:
            print('正在定位元素，定位方式key值: %s ,value值:%s'%(locator[0],locator[1]))

            try:
                ele=WebDriverWait(self.driver,timeout,t).until(lambda x:x.find_element(*locator))

                return ele
            except:

                return []
    #*判断元素是否存在
    def iselementExist(self,locat):
        ele=self.WebDriver_01(locat)
        if ele:
            return  True
        else:
            return  False



    #list，显性等待
    def WebDriver_02(self, locator, timeout=3, t=0.6):
        if not isinstance(locator, tuple):
            print('locator 元素类型错误，必须是元组类型：loc=("id","value")')

        else:
            print('正在定位元素，定位方式key值: %s ,value值:%s' % (locator[0], locator[1]))

            try:
                ele = WebDriverWait(self.driver, timeout, t).until(lambda x: x.find_elements(*locator))

                return ele
            except :

                return []

    #判断元素是多个
    def list_ele(self,*locat):
            ele=self.WebDriver_02(*locat)
            if len(ele)==0:
                print('没有找到元素')
            elif len(ele)==1:
                print('找到一个元素了')
            else:
                print('找到多个元素了')


    #判断alert 弹窗是否存在
    def ALEAR(self,timeout=5,t=0.5):
        try:
            result=self.driver.switch_to_alert()
            result.accept()
            return result.text
        except NoSuchElementException as a:
            print('没有alert 弹窗')
            return False

    #定位元素，并下输入框里输入
    def Send_Keys(self,locat,text):
        ele=self.WebDriver_01(locat)
        ele.clear()
        ele.send_keys(text)
    #元素点击
    def Click(self,locat):
        ele=self.WebDriver_01(locat)
        ele.click()

    #js,滚动条回到底部：
    def js_top(self,num):
        js = "window.scrollTo(%s,document.body.scrollHeight)"%num
        self.driver.execute_script(js)
    #滚动到顶部
    def js_t(self):
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    # 聚焦元素(滚动到元素出现的地方)
    def js_target(self,locat):
        target =self.WebDriver_01(locat)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    #鼠标悬停事件
    def Actions(self,*locat):
        ele=self.WebDriver_01(*locat)
        print(ele)
        ActionChains(self.driver).move_to_element(ele).perform()

    #select 下拉框,
    def Select(self,locat,index,value,text):
        ele=self.WebDriver_01(locat)
        Select(ele).select_by_index(index)  #下标选择
        time.sleep(3)

        Select(ele).select_by_value(value)  #数值选择
        time.sleep(3)

        Select(ele).select_by_visible_text(text)  #文本选择
        time.sleep(3)



if __name__ == '__main__':

    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.baidu.com/')
    B=Base(driver)
    B.Actions((By.LINK_TEXT,'设置'))
    B.Click((By.LINK_TEXT,'搜索设置'))
    B.Select((By.ID,'nr'),'1','20','每页显示50条')
    driver.close()

    #B.js_target((By.XPATH,'//*[@id="TopDiggPostsBlock"]/ul/li[10]/a'))
    # B.js_top(30)
    # time.sleep(3)
    # B.js_t()

    # B.Send_Keys((By.ID,'kw'),'12345')
    # B.Click((By.ID,'su'))

















