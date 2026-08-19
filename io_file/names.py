"""""
names = []

for _ in range(3):
    names.append(input("what is your name? "))
    
for name in sorted(names):
    print(f"hello, {name}")
"""

# "w" rewrites the entire conten
# "a" appends text to the end of a file
# "r" reads text from a file

"""
name = input("What is your name? ")
file = open("names.txt", "a") # open the file
file.write(f"{name}\n") # write the content
file.close() # close the file
"""
# using the keyword "with" will open and close the file automatically without having 
# to call the ".close()" method to close the file.
"""
with open("names.txt", "a") as write_file: # write_file here is not a keyword but it is a variable
    file.write(f"{name}\n")
"""

# read - to get or show the content of the file
"""
with open("names.txt", "r") as read_file:
    #lines = read_file.readlines() # return a list of the entire file and store it in the variable lines. using this will allows to use sorted() method which will sort the list.
    # instead we can use "for" to iterate through each line in within the file without having to recall and loop the content of the file.
    for line in read_file: # loop through each line
        print(f"hello, {line.rstrip()}")
"""


"""
names = []
with open("names.txt", "r") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name.title()}")
"""
# improved version of above program
"""
with open("names.txt", "r") as file:
    for line in sorted(file):
        print(f"hello, {line.rstrip().title()}")
"""

"""
names = []
fname = "lala"
with open("names.txt") as file:
    for name in file:
        names.append(name.rstrip())

try:
    fname = names.index(fname)
    print(names[fname])
except ValueError:  # this catches the error
    print(f"{fname} not found!")
"""
# improved version of above program
"""
fname = input("what is your name? ").strip().lower()
found = False

with open("names.txt", "r") as file:
    for line in file:
        if line.strip() == fname:
            found = True
            break # to avoid multiple

if found:
    print(f"{fname} found.")
else:
    print(f"{fname} not found.")
"""





            

    

    
    


