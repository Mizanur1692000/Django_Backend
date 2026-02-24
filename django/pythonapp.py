# Third-party app for seeing the data from the database
import requests

URL="http://127.0.0.1:8000/aiinfo/"
response=requests.get(url=URL)
data=response.json()
print(data)