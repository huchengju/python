import unittest
import time
import random
from config import global_variable
from interface.Account_Security import bind_phone_page,modify_phone_page
from interface.common import get_data_from_db,login,register

class ModifyPhoneTest(unittest.TestCase):
    def setUp(self):
        self.email = "1000@1.com"
        self.new_country = 359
        # self.new_phoneNumber = "10001231230"
        self.result = {'id': 100257, 'canSignin': 1}
        while (self.result != None):
            self.new_phoneNumber = random.randint(20000000000, 99999999999)
            self.result = get_data_from_db.get_userid_by_phoneNumber(self.new_phoneNumber)
        print("self.result", self.result)
        print("new_country:", self.new_country, "new_phoneNumber:", self.new_phoneNumber)

        check_email_result = get_data_from_db.get_user_id_by_email(self.email)
        if check_email_result == None:
            print("用户", self.email, "未存在，注册开始")
            register.register_action(self.email)
        else:
            print("用户", self.email, "已存在")
            self.userid = get_data_from_db.get_user_id_by_email(self.email)
            print("self.userid:",self.userid)
            check_result = get_data_from_db.get_phoneNumber_by_userid(self.userid)
            print("check_result:",check_result)
            if (check_result.get("phone_number") == None):
                print("用户", self.email, "未绑定手机，绑定手机开始")
                self.old_country = 86
                self.result = {'id': 100257, 'canSignin': 1}
                while (self.result != None):
                    self.old_phoneNumber = random.randint(20000000000, 99999999999)
                    self.result = get_data_from_db.get_user_id_by_email(self.old_phoneNumber)
                print("self.result:", self.result)
                print("old_country:",self.old_country,"old_phoneNumber:", self.old_phoneNumber)

                self.userid = get_data_from_db.get_user_id_by_email(self.email)
                self.token = login.login(self.email)
                print("old_phoneNumber:", self.old_phoneNumber)
                response = bind_phone_page.bind_phone(self.userid,self.old_country,self.old_phoneNumber,self.token)
                print("绑定手机 response：",response)

                """由于短信发送60s限制，所以等待60s"""
                print("等待60s开始")
                time.sleep(60)
                print("等待60s结束")
            else:
                print("用户", self.email, "已绑定手机，开始登录")
                self.token = login.login(self.email)


    def test_modify_phone_succcess(self):
        response = modify_phone_page.modify_phone(self.userid,self.new_country,self.new_phoneNumber,self.token)
        self.assertEqual(response.get("status"),"success","modify_phone_succcess")
        print("修改手机 response：",response)



    def tearDown(self):
        print("-------------test modify phone end------------")


if __name__ == "__main__":
    unittest.main(verbosity=2)