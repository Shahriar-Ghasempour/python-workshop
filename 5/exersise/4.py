lesson = {
    "name": "",
    "department": "",
    "unit": "",
    "teacher": "",
    "semester": 0,
    "year": 0,
}

for item in lesson:
    lesson[item] = input(f"{item}: ")

print("----------------------------------------------------------------")

for item in lesson:
    print(f"{item}: {lesson[item]}")
