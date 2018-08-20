import unittest
import time
from utils import pyselenium
import conifg

class Test_Ui_01(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = pyselenium.Pyselenium(conifg.browser)
    
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    
    def test_01(self):
        self.driver.open("http://www.baidu.com/")
        self.driver.send_and_click("id-->kw","浪晋的测试小讲堂","id-->su")
        time.sleep(2)
        title = self.driver.get_title()
        self.assertEqual(title,"浪晋的测试小讲堂_百度搜索","判断title是否一致")

    def test_02(self):
        self.driver.open("http://www.baidu.com/")
        self.driver.send_and_click("id-->kw","浪晋的测试小讲堂","id-->su")
        time.sleep(2)
        title = self.driver.get_title()
        self.assertEqual(title,"浪晋的测试小讲堂_百度搜索","判断title是否一致")
