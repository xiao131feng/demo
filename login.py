import unittest
from selenium import webdriver
import time
class TestDemo_login(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        cls.driver.get("http://192.168.1.192:8001/Login")
        cls.driver.find_element_by_name("UserName").send_keys("admin")
        cls.driver.find_element_by_name("Password").send_keys("admin8118")
        cls.driver.find_element_by_xpath("//*[@id=\"btnLogin\"]").click()
        time.sleep(5)       
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
    def test_01_login(self):
        lhcookie = self.driver.get_cookies()
        lhck = str(lhcookie[0]["name"])+"="+str(lhcookie[0]["value"])
        print(lhck)
        lhsy=self.driver.find_element_by_xpath("//*[@id=\"app_sidebar\"]/div/nav/ul/li[2]/a/span").text
        self.assertEqual(lhsy,"首页")
    

if __name__ == '__main__':
    unittest.main()
    