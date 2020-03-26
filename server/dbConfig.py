'''
数据库的配置信息
'''
import platform

current_system = platform.system()
def getUrl():
    URL = '127.0.0.1:3306'
    USERNAME = 'root'
    PASSWORD = '' if current_system == 'Linux' else '567984'  
    DATABASE = 'myblog'
    sqlType = 'mysql+pymysql' if current_system == 'Linux' else 'mysql'
    return  '{}://{}:{}@{}/{}'.format(sqlType,USERNAME,PASSWORD,URL,DATABASE)
