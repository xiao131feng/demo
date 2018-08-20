from utils import HTMLTestRunner
import unittest

suite = unittest.TestSuite()
suite = unittest.defaultTestLoader.discover(start_dir='./testcass', pattern='test_04.py')
with open("./reports/测试报告.html",'wb+') as f:
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,verbosity=2)
    runner.run(suite)
    