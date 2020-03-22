# coding:utf-8
import time
import sys
import os
import  logging
import logging.config
import os
pa=os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
path_t=os.path.join(pa,'tail_log','log.conf')
print(path_t)

#日志设置
con_log='../taiL_log/log.conf'
logging.config.fileConfig(path_t)
logging=logging.getLogger()

curPath = os.path.abspath(os.path.dirname(__file__))

rootPath = os.path.split(curPath)[0]

sys.path.append(rootPath)

from  common.config_ccc import Conig_c
#发送字符串的邮件
from email.mime.text import MIMEText
import  smtplib
from email.header import  Header


print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

class email_e(object):
    def __init__(self,fromadder,password,post,stmp_server):
        self.fromadder=fromadder
        self.password=password
        self.toaddrs=['1054571495@qq.com']
        self.post=post
        self.stmp_server=stmp_server

    #不带附件的方法
    def messag_e(self):
        # 设置email信息
        # ---------------------------发送字符串的邮件-----------------------------
        # 邮件内容设置
        message=MIMEText('hello','plain','utf-8')
        message['Subject']='ziqiiii test email'
        message['From']=self.fromadder
        message['To']=self.toaddrs[0]
        try:
            smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 注意：如果遇到发送失败的情况（提示远程主机拒接连接），这里要使用SMTP_SSL方法
            smtpObj.connect(self.stmp_server)
            smtpObj.login(self.fromadder, self.password)
            smtpObj.sendmail(self.fromadder, self.toaddrs, message.as_string())
            print('邮件发送成功')
        except  smtplib.SMTPException as a:
            print('发送失败%s'%a)

    #发送各种带附件的邮件
    def massage_ee(self,path=r'C:\Users\tanghuan\Desktop\33.html'):
        mail_title='登入自动化测试报告'
        # 读取文件内容
        f = open(path, 'rb')
        mail_boedy=f.read()
        f.close()
        # 邮件内容，编码，格式
        message = MIMEText(mail_boedy, 'html', 'utf-8')
        # 如下两行代码是确定以html发送还是以附件的形式发送
        message['Content-Type'] = 'application/octet-stream'
        message['Content-Disposition'] = 'attachment;filename="%s.html"' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        message['From'] = self.fromadder
        message['To'] = self.toaddrs[0]
        message['Subject'] = Header(mail_title, 'utf-8')

        try:
            smtpObj = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 注意：如果遇到发送失败的情况（提示远程主机拒接连接），这里要使用SMTP_SSL方法
            smtpObj.connect(self.stmp_server)
            smtpObj.login(self.fromadder, self.password)
            smtpObj.sendmail(self.fromadder, self.toaddrs, message.as_string())
            logging.info('发送成功')

        except smtplib.SMTPException as fail:
            logging.info('发送失败：%s'%fail)

if __name__ == '__main__':
    path='../config_c/config.ini'
    con=Conig_c(path)
    list=con.key_value('config_emalil')
    #print(list)
    e=email_e(list[0][1],list[1][1],list[3][1],list[2][1])
    e.massage_ee(r'C:\Users\tanghuan\Desktop\33.html')















