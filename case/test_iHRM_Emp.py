"""
    测试员工模块的增删改查实现
"""
# 1.导包
import logging
import unittest
import requests

import app
from api.EmpAPI import EmpCrup


# 2.创建测试类
class TestEmp(unittest.TestCase):
    # 3.初始化函数
    def setUp(self) -> None:
        self.session = requests.Session()
        self.emp_obj = EmpCrup()

    # 4.资源卸载函数
    def tearDown(self) -> None:
        self.session.close()

    # 5.测试函数
    # 5.1 增
    def test_add(self):
        logging.warning('新增员工信息')
        """
        直接执行该测试函数失败，为什么
        原因：1.先执行登录操作  2.还需要提交银行卡（token）
        解决：1.使用测试套件组织接口的执行顺序
             2.如何提交银行卡，如何实现关联
                核心步骤1.需要从登录接口中提取响应的token值
                核心步骤2.在新接口中提交token值
        """
        # 需要先登录操作
        # 请求业务
        response = self.emp_obj.add(self.session, username='tomcat159', mobile='132332175032')
        print('响应结果', response.json())
        # 断言业务
        # 响应结果 {'success': True, 'code': 10000, 'message': '操作成功！', 'data': {'id': '1193826295066480640'}}
        # 提取id
        id = response.json().get('data').get('id')
        print('员工id：', id)
        app.USER_ID = id

        self.assertEqual(True, response.json().get('success'))
        self.assertEqual(10000, response.json().get('code'))
        self.assertIn('操作成功', response.json().get('message'))

    # 5.2 改
    def test_update(self):
        logging.info('修改员工信息')
        # 请求业务
        response = self.emp_obj.update(self.session, app.USER_ID, '猫和老鼠')
        # 断言业务
        print('修改后的员工信息：', response.json())

        self.assertEqual(True, response.json().get('success'))
        self.assertEqual(10000, response.json().get('code'))
        self.assertIn('操作成功', response.json().get('message'))

    # 5.3 查
    def test_get(self):
        # 请求业务
        response = self.emp_obj.get(self.session, app.USER_ID)
        print('查询的是：', response.json())

        self.assertEqual(True, response.json().get('success'))
        self.assertEqual(10000, response.json().get('code'))
        self.assertIn('操作成功', response.json().get('message'))

    # 5.4 删
    def test_delete(self):
        response = self.emp_obj.delete(self.session, app.USER_ID)
        print('删除数据', response.json())

        self.assertEqual(True, response.json().get('success'))
        self.assertEqual(10000, response.json().get('code'))
        self.assertIn('操作成功', response.json().get('message'))
