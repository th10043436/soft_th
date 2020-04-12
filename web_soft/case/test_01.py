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
        self.path = os.path.dirname(__file__)
        print('99999999999' +self.path)
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

        try:
            self.assertTrue(ele)
        except Exception as error:
            print('断言失败 :%s'%error)
            now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            file_path='D:\\soft\\github\\web_soft\\screen_Shot\\'
            screen_name = file_path + '{}.png'.format(now)
            print(screen_name)

            self.driver.get_screenshot_as_file(screen_name)
            print('截图')

    def tearDown(self):
        time.sleep(6)
        self.driver.delete_all_cookies()
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
    suit = unittest.TestSuite()
    #  # 把这个类中需要执行的测试用例加进去，有多条再加即可
    suit.addTests(TEST('test_01'))
    # suit.addTest(counttest("test_add2"))#从上到下先后顺序
    runner = unittest.TextTestRunner()
    runner.run(suit)  # 运行测试用例

