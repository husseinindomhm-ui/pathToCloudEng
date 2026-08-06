# while loop 
"""""
x = 0
while x < 3:
    print("Meow")
    x+=1
"""""

# while true
"""""
while True:
    n = int(input('Please enter an integer: '))
    if n > 0:
        break     # ----> to break out of while loop
for _ in range(n):   
    print ("Meow")
"""""

# for loop - to itrate through a list
# List - Range
"""""
numbers = [0,1,2,3]
for i in range(3):
    print(i)
"""""

# \n - new line - combine it with end="" to tell end the line when you hit an empty string
# int("meow \n" * 3, end="") -- its other way to itrate or loop but its not a good practice

"""""
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("Enter an integer: "))
        if n > 0:
            return n
def meow(n):
    for _ in range(n):
        print ("Meow")

main()
"""""
"""""
students = ["Hussein", "Nada", "Alyssa"]
for student in students:
    print (student)

for i in range(len(students)):
    print(i, students[i])
"""""

# Dict - it's a key with value 
"""""
# each key hold one valeu
family  = {"Husb":"Hussein",
           "Wife":"Parka",
            "Child":"Nada"
        }

for member in family:
    print(member, family[member], sep=" : ")


# each key that holding multiple values we use list

fams = {
    "HusFam": ["Hussein", "Parka"],
    "ParkaFam": ["Ami", "Aji"]
}

for family in fams:
    print(family, fams[family], sep=" : ")

"""""

# list of families with their members as values

"""""
families = [
    {"name_fam": "Hussein Family", "husband name": "Hussein", "wife name": "Parka"},
    {"name_fam": "Aji Family", "husband name": "Aji", "wife name": "Mandi"}
]

for fam in families:
    print(fam["husband name"], fam["wife name"], sep="-")
"""""

def main():
    print_square(5)

"""""
def print_square(size):
    # for each row in square
    for i in range(size):
        # for each brick in row
        for j in range(size):
            # print brick
            print(" # ", end="")
        print()
"""""
def print_square(size):
    for i in range(size):
        print(" # " * size)

main()