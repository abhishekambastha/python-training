import requests

result = requests.get('localhost:8080/quadratic', dict(a=8, b=22, c=15)).json
print result
