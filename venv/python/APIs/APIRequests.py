import requests
import json
# Make a GET request to https://jsonplaceholder.typicode.com/users/1, print the status code,
# and print the user's name and email from the JSON response.
class UserAPI:
    def __init__(self, url = "https://jsonplaceholder.typicode.com"):
        self.url = url

    def get_one_user_detail(self, path, data):
        response = requests.get(f'{self.url}/{path}', timeout=5)
        response.raise_for_status()
        user_data = response.json()
        print(json.dumps(user_data, indent=4))

        dict1 = {}
        for key, value in user_data.items():
            if key in data:
                dict1[key] = user_data[key]
        print(dict1)
        return dict1

url = "https://jsonplaceholder.typicode.com"
userAPI = UserAPI(url)
datas = ("title", "body")
response = userAPI.get_one_user_detail("posts/1", datas)
title = response.get(datas[0])
body = response.get(datas[1])
print(title)
print(body)