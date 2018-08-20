from flask import Flask,jsonify,request

app = Flask(__name__)
@app.route("/")
def index():
    return '<h1> 哈哈</h1>'
@app.route("/getinfo",methods = ['GET'])
def getinfo():
    hdict = {}
    hdict["name"] = "lh"
    hdict["aget"] = 26
    hdict["sex"] ="女"
    return jsonify(hdict)

@app.route("/login",methods = ['POST'])
def login():   
    hdict = request.get_json()
    username = hdict.get("username")
    password = hdict.get("password")
    respone = {}
    if username == "admin" and password == "123456":
        respone["code"] =200
        respone["data"] = {"token":"safdsfkjhasdikjashdik"}
        respone["msg"] ="登陆成功"
        return jsonify(respone)
    else:
        respone["code"] =400
        respone["msg"] ="账号或密码错误"
        return jsonify(respone)           

if __name__ == '__main__':
    app.run(debug=True,port=5050)
