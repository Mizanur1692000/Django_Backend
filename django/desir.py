import requests, json

URL="http://127.0.0.1:8000/aicreate/"
data={
    "teacher_name":"Mizanur Rahman",
    "course_name":"AI Quest",
    "course_duration":30,
    "seat":100
}

json_data=json.dumps(data)
r=requests.post(url=URL, data=json_data)
data=r.json()
print(data)