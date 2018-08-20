import unittest

class TestDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("测试开始")

    @classmethod
    def tearDownClass(cls):
        print("测试结束")

    def test_01(self):
        self.assertEqual(1+1,2,"判断1+1是不是等于2")

    def test_02(self):
        self.assertEqual(1+1,3,"判断1+1是不是等于3")

    def test_03(self):
        self.assertEqual(1+1,4,"判断1+1是不是等于4")


