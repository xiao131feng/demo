import unittest
from utils import pyrequest
class TestRequest(unittest.TestCase):
    def Test_01(self):
        url = "http://127.0.0.1:5050/getinfo"
        res = pyrequest.get(url)
        rjson = res.json()
        name = rjson ["name"]
        self.assertEqual(name,"l")
    def Test_02(self):
        url = "http://127.0.0.1:5050/login"        
        json = {'username':'admin','password' :'123456'}
        headers = {
            'Content-Type:"application/json"
        }
        res = pyrequest.post(url,json=payload, headers=headers)
        rjson = res.json()
        code = rjson["code"] 
        self.assertEqual(code,'200')

 

    
        