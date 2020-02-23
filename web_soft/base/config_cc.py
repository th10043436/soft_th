import  configparser

class Conig_c(object):
    # 类实例化
    def __init__(self,path):

        self.config =configparser.ConfigParser()
        #读取文件
        self.config.read(path)
    def key_value(self,session):
        #解析config_emalil 数据
        list=[]
        list=self.config.items(session)
        return list
if __name__ == '__main__':
    path = '../config_c/config.ini'
    con=Conig_c(path)
    print(con.key_value('config_emalil'))

