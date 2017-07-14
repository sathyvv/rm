import requests

print(requests.get("http://httpbin.org/get?q=42").text)
