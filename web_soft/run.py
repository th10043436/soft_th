# -*- coding:utf-8  -*-
import  os
from Html import  html_config
import  logging
import  logging.config
import  unittest
import  time
from  common.Email import email_e
from  common.config_ccc import Conig_c
# 日志文件目录
path_t = os.path.dirname(os.path.realpath(__file__))
# 文件路径拼接，不能添加'/'
path_log = os.path.join(path_t, 'tail_log', 'log.conf')
#print(path_log)

logging.config.fileConfig(path_log)
logging = logging.getLogger()
def case_report():
    #日期格式化
    time_t=time.strftime('%Y-%m-%d %H-%M-%S')

    case_path=os.path.join(path_t,'case')
    html_path=os.path.join(path_t,'Html','test_report.html')
   # print(case_path,html_path)
    discover=unittest.defaultTestLoader.discover(start_dir=case_path,pattern='test*')

    #经验： 以上代码将转义字符’\’修改为’/’,即可运行通过
    #运行用例并生成测试报告

    ph=r'D:\soft\github\web_soft\Html'+'/'+time_t+'_test_report.html'
    print("ph: %s"%ph)
    print("path_t: %s"%path_t)
    with open(ph,'wb') as file:
        runner=html_config.HTMLTestRunner(stream=file,title='qq邮箱登入功能',description='测试登入',retry=1)
        runner.run(discover)
        logging.info('测试报告已经生成')


def send_email():
    #发送报告给邮箱
    re=os.listdir('./Html')
    li=re[-5]
    print(li)
    path=os.path.join(path_t,'Html',li)
    print("报告路径： %s"%path)
    return path

if __name__ == '__main__':

    path_i = os.getcwd() #获取当前文件位置
    print("path_i :%s"%path_i)
    case_report()
    pa=send_email()
    path = './config_c/config.ini'  # ‘./’代表同级 ‘../’代表上级
    con = Conig_c(path)
    list = con.key_value('config_emalil')
    print(list)
    e = email_e(list[0][1], list[1][1], list[3][1], list[2][1])
    e.massage_ee(pa)



