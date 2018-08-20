from utils.pyq import httprequest
# from ..import utils
import unittest

class Test_01_user(unittest.TestCase):
    def test_01_login(self):
        req = {
            "method":"POST",
            "url":"https://rental.ygwit.net:7001/api/app",
            "json":{
                "query":"{login(user:{name:\"testuser\"  password:\"123456\"  type:tenant}) {token,id,name}}"
            },
            "headers":{
                'Content-Type': "application/json"
            }
        } 
        response = httprequest(**req)
        code = response.status_code
        if code == 200:
            hjson = response.json()
            login = hjson["data"]["login"]
            for key in login:
                print(hjson)
                self.assertIsNotNone(login[key])
                
            global token
            token = hjson["data"]["login"]["token"]
        else:
            self.assertEqual(code,200)

# if __name__ == '__main__':
#     unittest.main()         
    