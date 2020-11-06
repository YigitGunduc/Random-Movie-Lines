"""
last update October 29 2020
@author: Yigit GUNDUC


this project is random movie lines 
api and webapp project for more information 
visit GitHub

GitHub : https://github.com/YigitGunduc/Random-Movie-Lines

License
This project is licensed under the MIT License (see the LICENSE file for details).
"""
import requests 

# random line api
response = requests.get("http://randommovielines.herokuapp.com/api/v1.0/randomlines")
#raw response
print(response.json())
#cleaned up response
print(response.json()["line"])

# famous quote api
response = requests.get("http://randommovielines.herokuapp.com/api/v1.0/famousquotes")
#raw response
print(response.json())
#cleaned up response
print(response.json()["quote"])
