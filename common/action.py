import configparser
import os
import random
import shutil
import pymysql


def del_file(filepath):
    """
    删除某一目录下的所有文件或文件夹
    :param filepath: 路径
    :return:
    """
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


def connect_db(path, name):
    """
    数据库连接
    :param path: 配置文件路径
    :param name: section名
    :return:
    """
    data = get_config(path, name)
    try:
        db_connect = pymysql.connect(host=data['host'], user=data['user'], password=data['password'], db=data['db'],
                                     charset=data['charset'])
        return db_connect
    except Exception:
        print('连接失败')


def get_config(path, name):
    """
    配置文件读取
    :param path: 路径
    :param name: section名
    :return: 该section下的所有键值对
    """
    cf = configparser.ConfigParser()
    dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cf.read(dir_path+path)  # 读取配置文件，如果写文件的绝对路径，就可以不用os模块
    # secs = cf.sections()  # 获取文件中所有的section(一个配置文件中可以有多个配置，如数据库相关的配置，邮箱相关的配置)
    # host = cf.get(name, 'host')  # 获取host
    items = dict(cf.items(name))  # 获取section名为Mysql-Database所对应的全部键值对
    return items


def mobile():
    """
    随机生成122开头手机号
    :return:
    """
    phone_n = '122' + ''.join(random.choice("0123456789") for i in range(8))
    return phone_n
