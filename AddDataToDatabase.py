import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancerealtime-12822-default-rtdb.firebaseio.com/"
})
ref = db.reference('Students')

data = {
    "en21cs304061":
        {
            "name": "MADHUR JAIN",
            "major" : "CSE- AI",
            "current_year": 2024,
            "total_attendance": 6,
            "Sub":"NLP",
            "Sem": "VII",
            "last_attendance_time": "2024-10-20 10:26:34"
        },
    "en21cs304062":
        {
            "name ": "Rohit Sharma ",
            "major" : "CSE- AI",
            "current_year": 2024,
            "total_attendance": 4,
            "Sub":"NLP",
            "Sem": "VII",
            "last_attendance_time": "2024-10-20 10:26:34"
        },
    "en21cs304063":
        {
            "name": "Virat Kohli ",
            "major" : "CSE- AI",
            "current_year": 2024,
            "total_attendance": 5,
            "Sub":"NLP",
            "Sem": "VII",
            "last_attendance_time": "2024-10-20 10:26:34"
        },
    "en21it301021":
        {
            "name": "Ansh Gaur ",
            "major" : "IT ",
            "current_year": 2024,
            "total_attendance": 5,
            "Sub":"NLP",
            "Sem": "VII",
            "last_attendance_time": "2024-10-20 10:26:34"
        },
"en21cs304072":
        {
            "name": "Nikhil Raghuwanshi ",
            "major" : "CSE-AI ",
            "current_year": 2024,
            "total_attendance": 0,
            "Sub":"NLP",
            "Sem": "VII",
            "last_attendance_time": "2024-10-20 10:26:34"
        }

}

for key,value in data.items():
    ref.child(key).set(value)