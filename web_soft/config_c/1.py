import  configparser
config=configparser.ConfigParser()
config.read('config.ini',encoding='GB18030')
print(config.sections())
print(config.options('path'))
print(config.items('path'))