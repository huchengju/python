import unittest
from interface.Account_Security import bind_GA_page,change_GA_page
from interface.common import get_data_from_db,register,login

class ChangeGATest(unittest.TestCase):

    def setUp(self):
        self.email = "1001@1.com"
        check_email_result = get_data_from_db.get_user_id_by_email(self.email)
        if check_email_result == None:
            print("用户",self.email,"未存在，注册开始")
            register.register_action(self.email)
        else:
            print("用户",self.email,"已存在")
            self.userid = get_data_from_db.get_user_id_by_email(self.email)
            print("self.userid:", self.userid)
            check_result = get_data_from_db.get_user_GA_secret(self.userid)
            print("check_result:", check_result)
            if (check_result == None):
                print("用户",self.email,"未绑定GA，绑定GA开始")
                self.userid = get_data_from_db.get_user_id_by_email(self.email)
                self.token = login.login(self.email)
                response = bind_GA_page.bind_GA(self.email,self.token)
            else:
                print("用户",self.email,"已绑定手机，开始登录")
                self.token = login.login(self.email)


    def test_change_GA(self):
        response = change_GA_page.change_GA(self.userid,self.token)
        print("response",response)
        self.assertEqual(response.get("status"),"success","change GA success")



    def tearDown(self):
        print("-------------test change GA end-------------")

if __name__ == "__main__":
    unittest.main(verbosity=2)