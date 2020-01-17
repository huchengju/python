import unittest
from interface.Account_Security import bind_GA_page, antiPhishing_code_page
from interface.common import register, login, get_data_from_db, get_GA_code


class ModifyAntiPhishingCodeTest(unittest.TestCase):

    def setUp(self):
        self.email = "1003@1.com"
        self.new_antiPhishing_code = "1111111111"
        self.modify_antiPhishing_code = "2222222222"
        check_email_result = get_data_from_db.get_user_id_by_email(self.email)
        if check_email_result == None:
            print("用户", self.email, "未存在，注册开始")
            register.register_action(self.email)
        else:
            print("用户", self.email, "已存在")
            self.userid = get_data_from_db.get_user_id_by_email(self.email)
            print("self.userid:", self.userid)
            check_result = get_data_from_db.get_user_GA_secret(self.userid)
            print("check_result:", check_result)
            if (check_result == None):
                print("用户", self.email, "未绑定GA，绑定GA开始")
                self.userid = get_data_from_db.get_user_id_by_email(self.email)
                self.token = login.login(self.email)
                response = bind_GA_page.bind_GA(self.email, self.token)
            else:
                print("用户", self.email, "已绑定GA")
                self.token = login.login(self.email)
                apCode_result = get_data_from_db.get_apcode_by_userid(self.userid).get("ap_code")
                if apCode_result == None:
                    print("用户", self.email, "未绑定防钓鱼码，开始绑定防钓鱼码")
                    self.secret = get_data_from_db.get_bind_GA_secret_fromdb(self.userid)
                    self.GA_code = get_GA_code.get_google_code(self.secret)
                    response = antiPhishing_code_page.add_antiPhishing_code_api(self.new_antiPhishing_code,self.GA_code, self.token)
                else:
                    print("用户", self.email, "已设置防钓鱼码")
                    self.token = login.login(self.email)

    def test_modify_antiPhishing_code_success(self):
        """modify antiPhishing_code success"""
        self.secret = get_data_from_db.get_user_GA_secret(self.userid).get("secretKey")
        self.GA_code = get_GA_code.get_google_code(self.secret)
        response = antiPhishing_code_page.modify_antiPhishing_code_api(self.new_antiPhishing_code,self.modify_antiPhishing_code, self.GA_code, self.token)
        print(response)
        self.assertEqual(response.get("status"), "success", "modify antiPhinshing_code success")

    def tearDown(self):
        print("-------------test modify antiPhishing_code end-------------")


if __name__ == "__main__":
    unittest.main(verbosity=2)