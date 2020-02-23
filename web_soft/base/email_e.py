#coding:utf-8
from email.mime.text import  MIMEText
import  smtplib


class Email(object):

   def emaa(self):
        try:
            content='这是正文'
            con=MIMEText(content,'plain','utf-8')
            reveivers='1054571495@qq.com'
            con['To']=reveivers
            con['From']=str('1054571495@qq.com')
            con['Subject']='这是一封主题'
            from_addr='1054571495@qq.com'
            password='lebqghmgxfkdbcih'
            smtp_server = 'smtp.qq.com'
            server=smtplib.SMTP_SSL(smtp_server,465)
            server.login(from_addr,password)
            server.send_message(con,from_addr,['1054571495@qq.com'])
            server.quit()
            print('11')
            print("发送成功")

        except :
            print('发送失败')

if __name__ == '__main__':
    ema=Email()
    ema.emaa()























