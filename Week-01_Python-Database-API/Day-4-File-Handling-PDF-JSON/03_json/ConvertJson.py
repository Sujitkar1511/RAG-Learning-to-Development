import json

student = {
    "name": "Sujit",
    "age": 21,
    "course": "BCA"
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)  
