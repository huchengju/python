import unittest
from interface.common import login, get_data_from_db, register, ieo_list_page


class GetBannerListTest(unittest.TestCase):

    def setUp(self):
        self.email = "1001@1.com"
        check_email_result = get_data_from_db.get_user_id_by_email(self.email)
        if check_email_result == None:
            print("用户", self.email, "未存在，注册开始")
            register.register_action(self.email)
        else:
            print("用户", self.email, "已存在")

    def testGetBannerList(self):
        """测试没有token时获取banner列表"""

        self.response = ieo_list_page.get_banner_list()
        self.assertEqual(self.response.get("status"),"success","get banner list without token success")

    def testGetBannerListWithToken(self):
        """测试有token时获取banner列表"""

        self.token = login.login(self.email)
        self.response = ieo_list_page.get_banner_list()
        self.assertEqual(self.response.get("status"),"success","get banner list with token success")


if __name__ == "__main__":
    unittest.main(verbosity=2)