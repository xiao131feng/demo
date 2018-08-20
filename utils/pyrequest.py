import requests

def get(url=""):
        """
            get方法
        """
        try:
            respose = requests.get(url=url)
        except Exception as e:
            print(e)

        return respose


def post(url="", data={}, headers={}, json={}):
        """
            post方法, 这里增加json
        """
        response = None
        try:
            response = requests.post(url=url, data=data, headers=headers, json=json)
        except Exception as e:
            print(e)

        return response
