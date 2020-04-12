from  common.base  import  Base
from selenium import  webdriver
from  selenium.webdriver.common.by import  By

#账号，密码，登入按钮
locat_01=(By.ID,'u')
locat_02=(By.ID,'p')
locat_03=(By.ID,'login_button')



class object_class(Base):

    #登入方法
    def login(self,account,password):
        ele_a=self.WebDriver_01(locat_01)
        print(ele_a)
        ele_a.clear()
        ele_a.send_keys(account)
        ele_p=self.WebDriver_01(locat_02)
        ele_p.clear()
        ele_p.send_keys(password)
        ele_b=self.WebDriver_01(locat_03)
        ele_b.click()
        print('---------------------------')


if __name__ == '__main__':
    driver=webdriver.Chrome()
    driver.get('https://mail.qq.com/')
    driver.switch_to.frame('login_frame')
    ob=object_class(driver)
    ob.login('1054571495@qq.com','15021675587')





