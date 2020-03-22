import  unittest
from  selenium import  webdriver
import  time,os
from  logView.logview import object_class
from  selenium.webdriver.common.by import  By
from  common.xlrd_x import Class_Xlrd

locat_01=(By.CLASS_NAME,'toptitle')
#dict={'accout':'1054571495@qq.com','password':'15021675587'}
path = os.path.dirname(os.path.dirname(__file__))

class TEST(unittest.TestCase):

    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://mail.qq.com/')


    def  test_01(self):
        '''qq登入功能'''
        #'./在runn文件运行' '../在本文件运行'
        self.path = os.getcwd()
        print(self.path)
        print("---------------------------")
        #xlrd=Class_Xlrd('D:/soft/github/web_soft/config_c/ceshi.xlsx')#解析excel 表格，里面存的是qq账号
        xlrd = Class_Xlrd(path + '/config_c/ceshi.xlsx')
        #print(xlrd)
        list=xlrd.dict_data()
        print(list)

        self.driver.switch_to.frame('login_frame')
        o= object_class(self.driver)
        o.login(list[0]['name'],list[0]['password'])
        ele=o.WebDriver_01(locat_01)
        print('具体元素 ：%s'%ele)
        self.assertTrue(ele)


    def tearDown(self):
        time.sleep(6)
        self.driver.delete_all_cookies()
        self.driver.close()


if __name__ == '__main__':
    unittest.main()