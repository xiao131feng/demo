from untils.pyrequests import httprequest
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
        hjson = response.json()
        global token
        token = hjson["data"]["login"]["token"]
        for key,value in hjson.items():
            if key == "errors":
                print (key,'value:',value)
            elif key == "id":
                # id1 = value
                self.assertEqual(value,"2")
            elif key == "name":
                # name1 = value
                self.assertEqual(value,"test")
if __name__ == '__main__':
    unittest.main()         
    