import unittest
# from interface.ieo import get_ieo_list
from  interface.common import login,get_data_from_db,register,ieo_list_page


class getIeoListTest(unittest.TestCase):

    def setUp(self):
        self.email = "1001@1.com"
        check_email_result = get_data_from_db.get_user_id_by_email(self.email)
        if check_email_result == None:
            print("用户", self.email, "未存在，注册开始")
            register.register_action(self.email)
        else:
            print("用户", self.email, "已存在")

    def testGetIeoList(self):
        """测试没有token时获取IEO列表"""

        self.response = ieo_list_page.get_ieo_list()
        self.assertEqual(self.response.get("status"),"success","get ieo list without token success")

    def testGetIeoListWithToken(self):
        """测试有token时获取IEO列表"""

        self.token = login.login(self.email)
        self.response = ieo_list_page.get_ieo_list()
        self.assertEqual(self.response.get("status"),"success","get ieo list with token success")


if __name__ == "__main__":
    unittest.main(verbosity=2)