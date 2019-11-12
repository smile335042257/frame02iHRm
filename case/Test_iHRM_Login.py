"""
    封装unittest相关实现
"""
# 1.导包
import json
import unittest
import requests

import app
from api.login_api import Login
from parameterized import parameterized


def read_json():
    my_list = []
    with open(app.pro_path + '/data/login_data.json', encoding='utf-8') as f:
        data = json.load(f)
        for i in data.values():
            my_list.append((i.get('mobile'),
                            i.get('password'),
                            i.get('success'),
                            i.get('code'),
                            i.get('message')
                            ))

        return my_list


# 2.创建测试类（unittest.TestCase）
class TestLogin(unittest.TestCase):
    # 3.初始化函数
    def setUp(self) -> None:
        self.session = requests.Session()  # 初始化session对象
        self.login_obj = Login()  # 初始化api对象

    # 4.资源卸载函数
    def tearDown(self) -> None:
        self.session.close()

    # 5.测试函数——登录
    @parameterized.expand(read_json())
    def test_login(self, mobile, password, success, code, message):
        # 请求业务
        response = self.login_obj.login(self.session, mobile, password)
        print('参数化读取的数据', mobile, password, success, code, message)
        print('登录响应结果', response.json())
        print('-' * 100)
        # 断言
        success_response = response.json().get('success')
        code_response = response.json().get('code')
        message_response = response.json().get('message')
        self.assertEqual(success, success_response)
        self.assertEqual(code, code_response)
        self.assertIn(message, message_response)

    # 编写登录成功的测试函数
    def test_login_success(self):
        # 1.请求业务——直接通过提交正向数据发送请求业务
        response = self.login_obj.login(self.session, '13800000002', '123456')
        print('登录成功的结果', response.json())
        # 2.断言
        """
         登录成功的结果 {'success': True, 'code': 10000, 'message': '操作成功！', 
        'data': '773738de-71de-4e8d-ba1c-86458162b313'}
        """
        self.assertEqual(True, response.json().get('success'))
        self.assertEqual(10000, response.json().get('code'))
        self.assertIn('操作成功', response.json().get('message'))
        # 提取token值
        token = response.json().get('data')
        print('登录后响应的token：', token)
        # 预期允许其他文件调用token值，可以扩大token的作用域（将token赋值给app的一个变量）
        app.TOKEN = token


if __name__ == '__main__':
    unittest.main()
