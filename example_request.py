import requests 


response = requests.get("http://randommovielines.herokuapp.com/api/v1.0/randomlines")
print(response.json())
print(response.json()["line"])