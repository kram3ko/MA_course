import requests

my_request = requests.get("https://www.google.com/")
print(my_request.status_code)
