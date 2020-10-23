# Random-Movie-Lines

<h2>Project overview</h2>

this project is an API with two endpoints that returns a random
line from a movie or a famous quote from a known movie

is the live demo at : 
- http://randommovielines.herokuapp.com//api/v1.0/randomlines
- http://randommovielines.herokuapp.com//api/v1.0/famousquotes

<h2>Endpoints</h2>

currently, there are 2 endpoints, first one is ../api/v1.0/
randomlines
and the second endpoint is /api/v1.0/famousquotes
the first endpoint picks a movie line between more than 450.000 
lines and returns it. 
The second endpoint is returning a famous quote form known 
movies 

<h2>how to use the API</h2>

this API is easy to use only thing you have to do is send an 
HTTP request to the desired endpoint contents body will be the 
proper response
you can see the example form example_request.py or down below  
```python
import requests 

response = requests.get("http://randommovielines.herokuapp.com/api/v1.0/randomlines")
#raw response
print(response.json())
#cleaned up response
print(response.json()["line"])
```

<h2>License</h2>  

This project is licensed under the MIT License (see the [LICENSE](https://github.com/YigitGunduc/Random-Movie-Lines/blob/main/LICENSE) file for details).

