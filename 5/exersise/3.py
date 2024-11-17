lesson = {
    "name": "",
    "department": "",
    "unit": "",
    "teacher": "",
    "semester": 0,
    "year": 0,
}

lesson["name"] = input("Course name: ")
lesson["department"] = input("Department name: ")
lesson["unit"] = input("Unit : ")
lesson["teacher"] = input("Teacher name: ")
lesson["semester"] = input("semester number: ")
lesson["year"] = input("Year : ")

print("----------------------------------------------------------------")

for item in lesson:
    print(f"{item}: {lesson[item]}")
