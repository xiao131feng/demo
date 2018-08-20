import requests

# def get():
#     url = 'http://www.itblacklist.top/'  
#     res = requests.get(url)
#     res.encoding = 'utf-8'
#     print(res.text)
#     print(res.status_code)
"""
1. http://www.itblacklist.top:2333/login
	username:admin
	password:123456
	检查一下登陆成功. code=200
	
	response.text ->str  =》 dict =（eval(response.text)）
	
2. http://www.itblacklist.top:2333/chicktoken
	token: - data
	
	code：200
	msg：成功
	
	输出成功的提示


"""
def post():
    url = 'http://www.itblacklist.top:2333/login'  
    data1 = {}
    data1["username"] = "admin" # username
    data1["password"] = "123456"
    res = requests.post(url=url,data=data1)
    l =  eval(res.text)
    if l["code"] == 200:
        return l
    else:
        return None

def post1():
    url = 'http://www.itblacklist.top:2333/chicktoken' # http:// -> url
    data = {}                                          # 字典
    token =  post()                                    
    data["token"] = token["data"]
    res = requests.post(url, data=data) 
    print(res.text)


   

if __name__ == '__main__':
    # 执行post1()
    post1()


    
