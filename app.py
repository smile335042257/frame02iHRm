"""
    框架搭建：
        核心：api + case +data
            api：封装请求业务
            case：继承unittest实现，调用api以及参数化解析data
            data：封装测试套件
        报告：report + tools + run.suite.py
            report：保存测试报告
            tools：封装工具文件
            run.suite.py：组织测试套件
        配置：app.py
            app.py：封装程序常量以及配置信息
        日志：log
            log：保存日志文件

    app.py 封装数据
"""
# 封装接口的 URL 前缀
import logging
import os
import logging.handlers

BASE_URL = 'http://182.92.81.159'

# 封装项目路径(动态获取绝对路径)
file_path = os.path.abspath(__file__)  # 获取当前文件的路径
pro_path = os.path.dirname(file_path)  # 获取项目路径

# 获取项目路径的另一种方法
pro_path2 = os.getcwd()
print(pro_path2)

# 定义一个变量
TOKEN = None
USER_ID = None


# 日志
# 写出格式：年月日时分秒用户级别函数.
def my_log_config():
    # 1. 获取日志对象
    logger = logging.getLogger()
    # 2.为日志输出日志级别
    logger.setLevel(logging.INFO)
    # 3.设置日志的输出目标（多目标）
    to_1 = logging.StreamHandler()  # 默认到控制台
    # 输出到文件
    to_2 = logging.handlers.TimedRotatingFileHandler(pro_path + '/log/mylog.log',
                                                     when='h',
                                                     interval=12,  # 每12小时产生一个日志文件
                                                     backupCount=10,  # 保留的文件个数
                                                     encoding='utf-8')
    # 4.指定输出格式
    formatter = logging.Formatter(
        "%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
    # 5.组合要将输出格式与输出目标和日志对象相组合
    to_1.setFormatter(formatter)
    to_2.setFormatter(formatter)
    # 将日志的输出目标添加进日志对象
    # 然后输出的时候就会把日志按照指定的格式和指定输出的地方输出出来
    logger.addHandler(to_1)
    logger.addHandler(to_2)


# 调用 在需求位置输出日志
"""
需求：为测试函数添加日志输出
实现：
步:1：包下的__init__.py初始化日志配置
      import app
      app.my_log_config()
步骤2：在测试函数中（测试用例中）调用logging.xxx('日志信息')
"""
# my_log_config()
# logging.info('hello')
