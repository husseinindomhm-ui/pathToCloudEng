"""
with open("students.csv") as file:
    for line in file:
        # row = line.strip().split(",")
        name, city = line.rstrip().split(",")
        print(f"name: {name} | city: {city}")
"""

"""
students = []
with open("students.csv") as file:
    for line in file:
        name, city = line.rstrip().split(",")
        students.append((f"{name} is in {city}"))

for student in sorted(students):
        print(student)
"""
import csv
students = []
with open("students.csv") as file:
    reader = csv.reader(file)
    for name, city in reader:
        students.append({"name": name, "city": city})
    # for line in file:
        #name, city = line.rstrip().split(",")
        #student = {"name": name, "city": city}
        # student["name"] = name
        # student["city"] = city
        # students.append(student)

#for student in students:
 #   print(f"{student['name']} is in {student['city']}")
 
#def get_house(student):      # replacing it with lambda function
#    return student["city"]

for student in sorted(students, key = lambda student: student["city"]):
   print(f"{student['name']} is in {student['city']}")

