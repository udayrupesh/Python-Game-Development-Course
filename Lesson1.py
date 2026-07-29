students = {
    "S001":{
        "name":"Mbappe",
        "age": 15,
        "class": "10th",
        "marks": {
            "Maths": 88,
            "Science": 92,
            "English": 85
        }
    },
    "S002":{
        "name": "Yamal",
        "age": 14,
        "class": "9th",
        "marks": {
            "Maths": 78,
            "Science": 81,
            "English": 89
        }
    },
    "S003":{
        "name": " Vinicius Jr",
        "age": 16,
        "class":"11th",
        "marks":{
            "Maths": 99,
            "Science":98,
            "English":100
        }
    }
}
# Display student details and marks
for student_id, student_data in students.items():
    print("\nStudent ID:", student_id)
    print("Name:", student_data["name"])
    print("Age:", student_data["age"])
    print("Class:", student_data["class"])

    print("Marks")
    for subject, score in student_data["marks"].items():
        print(" ", subject , ":" , score)

# Add bonus marks to Maths for each student
for student_data in students.values():
    student_data["marks"]["Maths"] += 5

print("\n Updated Maths Marks after Bonus:")
for student_id, student_data in students.items():
    print(student_id, "->", student_data["marks"]["Maths"])
    