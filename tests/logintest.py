import unittest
from flask import json
from  ..app.main.main import app  # 导入Flask应用实例

class TestFlaskRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()

    def test_login_handler(self):
        response = self.client.post('/login', data=json.dumps(dict(
            username='testuser',
            password='password'
        )), content_type='application/json')
        self.assertEqual(response.status_code, 200)  # 成功的情况下应该返回状态码200
        data = json.loads(response.data)
        self.assertEqual(data["msg"], "登录成功")  # 成功的情况下应该返回 "登录成功"

    def test_register_handler(self):
        response = self.client.post('/register', data=json.dumps(dict(
            username='testuser',
            password='password'
        )), content_type='application/json')
        self.assertEqual(response.status_code, 200)  # 成功的情况下应该返回状态码200
        data = json.loads(response.data)
        self.assertEqual(data["msg"], "注册成功")  # 成功的情况下应该返回 "注册成功"


if __name__ == '__main__':
    unittest.main()
