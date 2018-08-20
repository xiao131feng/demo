import unittest
from utils import pyrequest
from utils import readxls


class TestRequest(unittest.TestCase):
    def test_login(self):
        res = pyrequest.get('http://127.0.0.1:8050/getinfo')
        a = res.json()
        name = a['name']
        self.assertEqual(name, '浪')
   
    def test_post(self):
        url = "http://127.0.0.1:8050/login"
        name = readxls.gettestdata(0, 0)
        word = readxls.gettestdata(0, 1)
        payload = {"username":name,"password":str(int(word))}
        print(payload)
        headers = {
            'Content-Type': "application/json",
            }
        res = pyrequest.post(url=url, json=payload, headers=headers)
        a = res.json()
        print(a)
        token = a['data']['token']
        self.assertEqual(token, 'asdsd')
