import  unittest
from  selenium import  webdriver
import  time
from  logView.logview import object_class
from  selenium.webdriver.common.by import  By

locat_01=(By.CLASS_NAME,'toptitle')
dict={'accout':'1054571495@qq.com','password':'15021675587'}

class TEST(unittest.TestCase):
    '''qq'''
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://mail.qq.com/')

    def  test_01(self):
        '''qq登入功能'''
        self.driver.switch_to.frame('login_frame')
        o= object_class(self.driver)
        o.login(dict['accout'],dict['password'])
        ele=o.WebDriver_01(locat_01)
        print('具体元素 ：%s'%ele)
        self.assertTrue(ele)


    def tearDown(self):
        time.sleep(6)
        self.driver.close()


if __name__ == '__main__':
    unittest.main()