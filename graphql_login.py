import requests
import unittest
# from utils import pyrequest
class TestGraphql_login1(unittest.TestCase):
    def test_01_graphql_login(self):
        url = "https://rental.ygwit.net:7001/api/app"
        payload = {"query":"{login(user:{name:\"testuser\"  password:\"123456\"  type:tenant}) {token,id,name}}"}
        headers = {
            'Content-Type': "application/json",
            }
        # res = pyrequest.post(url=url,json=payload,headers=headers)    
        res = requests.request("POST", url, json=payload, headers=headers)
        # code = res.status_code   # 获取接口的状态码
        jres = res.json()          # 将返回的数据转换为json格式
        # print (jres) 
        # print (code)
        name = jres['data']['login'] ['name']
        # print (name)
        global token
        token = jres["data"]["login"]["token"]
        # return token
        id1 = jres["data"]["login"]["id"]
        # self.assertEqual(name,"test")
        for key,value in jres.items():
            if key == "errors":
                print (key,'value:',value)
        print (jres)                
    def test_02_getUserprofile(self):
        url = "https://rental.ygwit.net:7001/api/app"
        payload = {"query":"{getUserProfile(id:1){name,id,telno,type,credentialsType,credentialsNO,credentialsFront,cardNO,valid,age,gender,nation,birthday,platforms{id,name,host}}}"}
        headers = {
            'authorization': token,
            'content-type': "application/json",
        }
        res = requests.request("POST", url, json=payload, headers=headers)
        jres = res.json()
        for key,value in jres.items():
            if key == "errors":
                print (key,'value:',value)
                

if __name__ == '__main__':
    unittest.main()




