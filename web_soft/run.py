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

    ph=r'D:\soft\github\web_soft\Html'+'\\'+time_t+'_test_report.html'
    print("ph: %s"%ph)
    print("path_t: %s"%path_t)
    with open(ph,'wb') as file:
        runner=html_config.HTMLTestRunner(stream=file,title='qq邮箱登入功能',description='测试登入',retry=1)
        runner.run(discover)
        logging.info('测试报告已经生成')


def send_email():
    #发送报告给游戏
    re=os.listdir('./Html')
    li=re[-3]
    print(li)
    path=os.path.join(path_t,'Html',li)
    print(path)

if __name__ == '__main__':
    case_report()



