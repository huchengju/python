import unittest
from config import global_variable
from interface.common import login, get_data_from_db, register, ieo_detail_page,create_ieo,manage_login


class GetIeoDetailTest(unittest.TestCase):

    def setUp(self):
        self.email = "1001@1.com"
        check_email_result = get_data_from_db.get_user_id_by_email(self.email)
        if check_email_result == None:
            print("用户", self.email, "未存在，注册开始")
            register.register_action(self.email)
        else:
            print("用户", self.email, "已存在")

        # 查看是否有存在的进行中的IEO项目
        self.result = get_data_from_db.get_ongoing_ieoid()
        if self.result != None:
            self.ieoId = self.result.get("id")
        else:
            print("没有存在的进行中的IEO项目，开始创建")
            self.manage_token = manage_login.manage_login_by_cir(global_variable.cir_var)
            create_ieo.create_ieo(self.manage_token)
            self.result = get_data_from_db.get_ongoing_ieoid()
            if self.result != None:
                self.ieoId = self.result.get("id")

    def testGetIeoDetail(self):
        """测试没有token时获取IEO详细信息"""

        self.response = ieo_detail_page.get_ieo_detail(self.ieoId)
        self.assertEqual(self.response.get("status"),"success","get ieo detail without token success")

    def testGetIeoDetailWithToken(self):
        """测试有token时获取IEO详细信息"""

        self.token = login.login(self.email)
        self.response = ieo_detail_page.get_ieo_detail(self.ieoId,self.token)
        self.assertEqual(self.response.get("status"),"success","get ieo detail with token success")


if __name__ == "__main__":
    unittest.main(verbosity=2)