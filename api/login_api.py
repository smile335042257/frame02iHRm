"""
    封装类：
        请求函数封装
"""
from app import BASE_URL


class Login:
    def __init__(self):  # 封装url
        self.login_url = BASE_URL + '/api/sys/login'

    def login(self, session, mobile, password):
        # 登录函数 响应结果返回给调用者，必须返回
        my_login = {"mobile": mobile,
                    "password": password}
        return session.post(self.login_url, json=my_login)
