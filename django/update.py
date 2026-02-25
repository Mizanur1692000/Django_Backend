import requests
import json

data={
    "id":3,
    "teacher_name":"Mizanur Rahman",
    "course_name":"AI and Backend",
    "course_duration":30,
    "seat":100
}

URL = f"http://127.0.0.1:8000/aicreate/{data['id']}/"
json_data=json.dumps(data)
r=requests.put(url=URL, data=json_data, headers={"Content-Type": "application/json"})
data=r.json()
print(data)