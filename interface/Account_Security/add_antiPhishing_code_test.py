import unittest
import time
from config import global_variable
from interface.Account_Security import bind_GA_page,antiPhishing_code_page
from interface.common import register,login,get_data_from_db,get_GA_code



class AddAntiPhishingCodeTest(unittest.TestCase):

    def setUp(self):
        nowtime = time.strftime("%Y_%m_%d_%H_%M_%S")
        self.email = global_variable.cir_var + "_" + nowtime + "@1.com"
        self.new_antiPhishing_code = "11111111111"

        register.register_action(self.email)
        self.userid = get_data_from_db.get_user_id_by_email(self.email)

        self.token = login.login_with_param(self.email)
        data = bind_GA_page.bind_GA(self.email, self.token)


    def test_add_antiPhishing_code_success(self):
        """add antiPhishing_code success"""
        self.secret = get_data_from_db.get_bind_GA_secret_fromdb(self.userid)
        self.GA_code = get_GA_code.get_google_code(self.secret)
        response = antiPhishing_code_page.add_antiPhishing_code_api(self.new_antiPhishing_code, self.GA_code, self.token)
        print(response)
        self.assertEqual(response.get("status"),"success","add antiPhinshing_code success")


    def tearDown(self):
        print("-------------test add antiPhishing_code end-------------")


if __name__ == "__main__":
    unittest.main(verbosity=2)