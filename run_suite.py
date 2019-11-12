"""
    测试套件：
        按照需求组合被执行的测试函数
    自动化测试执行顺序：
        增 ---> 改 ---> 查 ---> 删
    补充说明：
        关于套件的组织，接口业务测试中，需要保证测试套件中的执行顺序；
        合法实现：suite.addTest(类名（"函数名"）) 逐一添加
        非法实现：suite.addTest(unittest.makeSuite(类名)) 虽然可以一次性添加多个测试函数，但是无法保证执行顺序
"""
# 1.导包
import time
import unittest

import app
from case.Test_iHRM_Login import TestLogin
from case.test_iHRM_Emp import TestEmp
from tools.HTMLTestRunner import HTMLTestRunner

# 2.实例化套件对象，组织被执行的测试函数
suite = unittest.TestSuite()
suite.addTest(TestLogin('test_login_success'))  # 组织登录成功的测试函数
suite.addTest(TestEmp('test_add'))  # 组织员工新增的测试函数
suite.addTest(TestEmp('test_update'))  # 修改员工信息
suite.addTest(TestEmp('test_get'))  # 查询员工信息
suite.addTest(TestEmp('test_delete'))  # 删除员工信息
# suite.addTest(unittest.makeSuite(TestEmp))   # 不能保证测试顺序，所以会报错
# 3.执行套件生成测试报告,打开文件流
with open(app.pro_path + '/report/report.html', 'wb') as f:
    runner = HTMLTestRunner(f, title='我的报告', description='IHRM V1.0')
    runner.run(suite)

# runner = unittest.TextTestRunner()
# runner.run(suite)
