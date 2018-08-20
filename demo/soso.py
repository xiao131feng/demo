import unittest
from selenium import webdriver
class test_soso(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="/chromedriver.exe")
        cls.driver.get("https://www.soso.com/")
    @classmethod
    def tearDown(cls):
        cls.driver.quit()
    def test_01_soso(self):
        attribute= self.driver.find_element_by_id("input").is_displayed()
        print(attribute)
        ba = self.driver.find_element_by_xpath("//*[@id=\"footer\"]/p").text
        print(ba)

if __name__ == '__main__':
    unittest.main()     