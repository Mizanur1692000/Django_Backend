import requests
import json
URL="http://127.0.0.1:8000/aicreate/"

data={
    "id":3,
    "teacher_name":"Mizanur Rahman",
    "couser_name":"AI and Backend",
    "course_duration":30,
    "seat":100
}

json_data=json.dumps(data)
r=requests.put(url=URL, data=json_data)
data=r.json()
print(data)