#coding:utf-8
from email.mime.text import  MIMEText
import  smtplib
from base.config_cc import Conig_c

class Email(object):

   def emaa(self,email,password,smtp_server,post):

            content='这是正文'
            con=MIMEText(content,'plain','utf-8')
            reveivers=email
            con['To']=reveivers
            con['From']=email
            con['Subject']='这是一封主题'
            from_addr='1054571495@qq.com'
            password=password
            smtp_server=smtp_server
            server=smtplib.SMTP_SSL('smtp.qq.com','465')
            server.login('1054571495@qq.com','lebqghmgxfkdbcih')
            server.send_message(con,from_addr,['1054571495@qq.com'])
            server.quit()
            print("发送成功")



if __name__ == '__main__':
    path='../config_c/config.ini'
    c=Conig_c(path)
    list=c.key_value('config_emalil')
    print(list)
    ema=Email()
    print(list[0][1],list[1][1],list[2][1],list[3][1])

    #email,password,smtp_server,post
    ema.emaa(list[0][1],list[1][1],list[2][1],list[3][1])



