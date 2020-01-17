from interface.Account_Security import bind_GA_page
from interface.common import get_GA_code, login, register,get_data_from_db,get_data_from_redis
import unittest
from config import global_variable
import time



# #绑定GA整个流程test


class BindGATest(unittest.TestCase):

    def setUp(self):
        # 准备email
        # 注册
        # 登录获取token
        now_time = time.strftime("%Y-%m-%d_%H_%M_%S")
        # email = now_time + "@1.com"
        email = global_variable.cir_var + "_" + now_time + "@1.com"
        print("email:", email)
        register.register_action(email)
        self.token = login.login_with_param(email)

        bind_GA_page.get_GA_secret_api(self.token)
        self.userid = get_data_from_db.get_user_id_by_email(email)
        self.secret = get_data_from_db.get_bind_GA_secret_fromdb(self.userid)
        print("secret",self.secret)
        self.GA_code = get_GA_code.get_google_code(self.secret)
        print("GA_code",self.GA_code)
        bind_GA_page.bind_GA_send_email_api(self.token)
        self.email_code = get_data_from_redis.get_bind_GA_email_code_from_redis(self.userid)
        print("email_code", self.email_code)


    def test_bind_GA_with_wrongEmailCode(self):
        """email code错误，GA code正确，绑定失败"""

        response = bind_GA_page.bind_GA_api("000000", self.GA_code, self.token)
        print(response)
        self.assertEqual(response.get("status"), "fail", "bind_GA 失败")

    def test_bind_GA_with_wrongGACode(self):
        """email code正确，GA code错误，绑定失败"""

        response = bind_GA_page.bind_GA_api(self.email_code, "000000", self.token)
        print(response)
        self.assertEqual(response.get("status"), "fail", "bind_GA 失败")


    def test_bind_GA_success(self):
        """email code正确，GA code正确，绑定成功"""

        response = bind_GA_page.bind_GA_api(self.email_code, self.GA_code, self.token)
        self.assertEqual(response.get("status"),"success","bind_GA 成功")

    def tearDown(self):
        print("-------------test bind_GA end-------------")


if __name__ == "__main__":
    unittest.main(verbosity=2)

