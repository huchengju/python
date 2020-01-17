import unittest
from interface.common import register,login,get_data_from_db,get_data_from_redis
import time
from config import global_variable
from interface.Account_Security import bind_phone_page,bind_GA_page
import random


class BindPhoneTest(unittest.TestCase):

    def setUp(self):
        nowtime = time.strftime("%Y_%m_%d_%H_%M_%S")
        self.email = global_variable.cir_var + "_" + nowtime + "@1.com"
        print("email:",self.email)
        self.country = 86
        # self.phoneNumber = "10001231230"
        self.result = {'id': 100257, 'canSignin': 1}
        while (self.result != None):
            self.phoneNumber = random.randint(20000000000,99999999999)
            self.result = get_data_from_db.get_userid_by_phoneNumber(self.phoneNumber)
            print("self.result",self.result)
        print("phoneNumber:",self.phoneNumber)


        register.register_action(self.email)
        userid = get_data_from_db.get_user_id_by_email(self.email)

        self.token = login.login_with_param(self.email)
        data = bind_GA_page.bind_GA(self.email,self.token)
        # self.token = data.get("token")
        bind_phone_page.bind_phone_send_email_api(self.token)
        bind_phone_page.bind_phone_send_message_api(self.country,self.phoneNumber,self.token)
        self.email_code = get_data_from_redis.get_bind_phone_email_code_from_redis(userid)
        print("email_code:", self.email_code)
        self.message_code = get_data_from_redis.get_bind_phone_message_code_from_redis(self.country,self.phoneNumber)
        print("message_code:",self.message_code)


    def test_bind_phone_success(self):
        """绑定手机成功"""
        print("-------------")
        print(self.country,self.email_code,self.message_code,self.phoneNumber,self.token)
        response = bind_phone_page.bind_phone_api(self.country,self.email_code,self.message_code,self.phoneNumber,self.token)
        print(response)
        self.assertEqual(response.get("status"),"success","bind_phone_success")


    def tearDown(self):
        print("-------------test bind_phone end-------------")


if __name__ == "__main__":
    unittest.main(verbosity=2)