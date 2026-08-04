'''''''''
grocery_list = ["Milk", "Eggs", "Bread", "Butter", "Cheese", "Yogurt", "Juice", "Cereal", "Pasta", "Rice"]

print(grocery_list)
print(grocery_list[0])  # Output: Milk
print(grocery_list[1])  # Output: Eggs
print(grocery_list[2])  # Output: Bread

print(grocery_list[-1])  # Output: Bread
print(grocery_list[-2])  # Output: Eggs
print(grocery_list[-3])  # Output: Milk

grocery_list[1] = "Almond Milk"
print(grocery_list)  # Output: ['Milk', 'Almond Milk', 'Bread']

#insert(index, item) adds at a specific position and shifts the rest along
grocery_list.insert(0, "Cola")

# append(item) adds to the end
grocery_list.append("Butter")
grocery_list.remove("Cola")
grocery_list.pop()  # Removes the last item, which is "Butter"


grocery_list.sort()  # Sorts the list in alphabetical order
#slicing A slice grabs a sublist with [start:end]. The start index is included, the end index is not:
print(grocery_list[:2])  # Output: ['Almond Milk', 'Bread']
print(grocery_list[2:5])  # Output: ['Butter', 'Cheese', 'Cereal']
print(grocery_list[-2:]) # Output: ['Pasta', 'Rice']


#List length -- len(my_list) returns how many items are in a list:
count = len(grocery_list)
limit = 12

print("Number of items in grocery list:", count)
if count <= limit:
    print("Grocery list is within the limit.")

else:
    print("Grocery list exceeds the limit.")


print("Sorted grocery list:", grocery_list) 


# Nasted lists:
#  are lists that contain other lists as elements. 
# They can be used to represent more complex data structures, 
# such as matrices or tables.

teams = [
    ["Team A", "Player 1", "Player 2", "Player 3"],
    ["Team B", "Player 4", "Player 5", "Player 6"],
    ["Team C", "Player 7", "Player 8", "Player 9"]
]

print(teams[0])  # Output: ['Team A', 'Player 1', 'Player 2', 'Player 3']
print(teams[1][2])  # Output: Player 5  

'''''''''

# Loops and Lists
# A loop is a programming construct that allows you to repeat 
# a block of code multiple times.

'''''''''
grocery_list = ["Milk", "Eggs", "Bread", "Butter", "Cheese", "Yogurt", "Juice", "Cereal", "Pasta", "Rice"]
for item in grocery_list:
    print(item)  # Output: Each item in the grocery list

for x in range(1,101):
    print(x)  # Output: 1, 2, 3, ... 100

'''''''''

# Looping over lists with conditions
# You can use loops to iterate over lists and apply conditions to each item.
'''''''''
grocery_list = ["Milk", "Eggs", "Bread", "Butter", "Cheese", "Yogurt", "Juice", "Cereal", "Pasta", "Rice"]
dairy_items = ["Milk", "Cheese", "Yogurt"]
cereal_items = ["Cereal", "Pasta", "Rice"]
breakfast_items = ["Eggs", "Bread", "Butter"]

for item in grocery_list:
    if item in dairy_items:
        print(f"{item} is a dairy item.")
    elif item in cereal_items:
        print(f"{item} is a cereal item.")
    elif item in breakfast_items:
        print(f"{item} is a breakfast item.")
    else:
        print(f"{item} is not categorized.")


guests = ["Alice", "Bob", "Charlie", "David", "Eve"]
vip_guests = ["Alice", "Charlie"]
for guest in guests:
    if guest in vip_guests:
        print (f"VIP:{guest}")
    else:
        print(f"Regular guest: {guest}")

'''''''''


# Looping through strings
# You can also loop through each character in a string using a for loop.
'''''''''

word = "mississippi"
total_characters = len(word)
count = 0
for letter in word:
    print(letter)  # Output: m, i, s, s, i, s, s, i, p, p, i
print(f"Number of characters in '{word}': {total_characters}")

for count_s in word:
    if count_s == "s":
        count +=1
print(f"Number of 's' characters in '{word}': {count}")

'''''''''

# While loops
# A while loop is a control flow statement that 
# allows code to be executed repeatedly based on a given Boolean condition. 
# The loop will continue to execute as long as the condition evaluates to True. 
'''''''''
count = 0
while count <= 5:
    print(f"Count is {count}")
    count += 1  # Increment count to avoid infinite loop


password = "secret123"
attempts = ["letmein", "password", "secret123"]
i = 0

while attempts[i] != password:
    i = i + 1
    print(f"Attempt {i}: {attempts[i-1]} is incorrect.")

print("Access granted.")

explaining the code: what dose the attempts[i-1] mean in the print statement?
In the print statement `print(f"Attempt {i}: {attempts[i-1]} is incorrect.")`, 
the expression `attempts[i-1]` 
is used to access the previous attempt made by the user.
'''''''''

# Finding Values in Lists
# You can use the `in` keyword to check if a value exists in a list.   

'''''''''
fruits = ["apple", "banana", "cherry", "date", "fig", "grape"]
print("banana" in fruits)  # Output: True
print("kiwi" in fruits)    # Output: False

if "banana" in fruits:
    print("Banana is in the list of fruits.")
else:
    print("Banana is not in the list of fruits.")


guest_list = ["Alice", "Bob", "Charlie", "David", "Eve"]
guest = "same"

if guest in guest_list:
    print(f"{guest} - Welcome to the party!")
else:
    print(f"{guest} - Sorry, you are not on the guest list.")

'''''''''

# Break - The `break` statement is used to exit a loop prematurely 
# when a certain condition is met.

'''''''''
usernames = ["user1", "user2", "admin", "user3"]

for name in usernames:
    if name == "usr4":  # Check for a specific username
        print(f"Found {name}, stopping the search.")
        break  # Exit the loop when "user2" is found    
    else:
        print(f"{name} is not the username we are looking for.")


password = "password"
attempts = ["secret123", "letmein", "password", "qwerty"]

for attempt in attempts:
    if attempt == password:
        print("Access granted.")
        break  # Exit the loop when the correct password is found
    else:
        print("Wrong password.")

'''''''''

# Continue - The `continue` statement is used to skip the current  
# iteration of a loop and move on to the next iteration.

'''''''''
for n in range(1, 6):
    if n == 3:
        continue
    print(n)  # Output: 1, 2, 4, 5

# When n is 3, continue jumps straight to the next iteration, 
# so 3 never gets printed:

emails = ["alice@example.com", "bob@example.com", "charlie@example.com", "spam1@example.com"]
spam_email = ["spam1@example.com", ""]

for email in emails:
    if email in spam_email:
        continue  # Skip the spam email
    print(f"Sending email to: {email}")  # Output: Sending email to: alice@example.com
                                         #         Sending email to: bob@example.com
                                         #         Sending email to: charlie@example.com

'''''''''


# Nested Loops - A nested loop is a loop inside another loop.
# The inner loop will run completely every time the outer loop runs once.
'''''''''
seating = [
    ["Ann", "Ben"],
    ["Cara", "Dan"],
]
 
for row in seating:
    for name in row:
        print(name)  # Output: Ann, Ben, Cara, Dan

# explaining the code: The outer loop iterates over each row in the seating list,
# and the inner loop iterates over each name in that row, printing each name one by one.

board = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

for row in board:
    for number in row:
        print(number)

'''''''''


# Loops in practice 
'''''''''
temps = [70, 75, 80]
 
total = 0
for temp in temps:
    total = total + temp
 
average = total / len(temps)
print(total)      # 225
print(average)    # 75.0

scores = [85, 90, 78, 92, 88]
total_score = 0

for score in scores:
    total_score += score

average_score = total_score / len(scores)
print(f"total score: {float(total_score)} - average score: {average_score}")


for word in ["hello", "world", "python"]:
    print(word) 

'''''''''


#example of input function
'''''''''
name =input("what is your name? ")
print(f"Hello, {name}!")



input_number = input("Please enter a number: ")
print(f"You entered: {int(input_number) + 10}")  # Convert the string to an integer before adding 10
'''''''''
# String Methods
# Strings in Python come with a variety of built-in methods that allow you to manipulate and analyze them. 
# Here are some commonly used string methods: 

"""
name.lower() - Converts all characters in the string to lowercase.
name.upper() - Converts all characters in the string to uppercase.
name.title() - Converts the first character of each word to uppercase and the rest to lowercase.
name.strip() - Removes any leading and trailing whitespace from the string.
name.replace(old, new) - Replaces occurrences of a specified substring (old) with another substring (new).
name.split(separator) - Splits the string into a list of substrings based on the specified separator. If no separator is provided, it splits on whitespace by default.
name.find(substring) - Returns the index of the first occurrence of the specified substring. Returns -1 if the substring is not found.
name.count(substring) - Returns the number of occurrences of the specified substring in the string. 
name.startswith(prefix) - Returns True if the string starts with the specified prefix, otherwise returns False.
name.endswith(suffix) - Returns True if the string ends with the specified suffix, otherwise returns False.
name.isdigit() - Returns True if all characters in the string are digits, otherwise returns False. 
name.isalpha() - Returns True if all characters in the string are alphabetic, otherwise returns False.
name.isalnum() - Returns True if all characters in the string are alphanumeric (letters and numbers), otherwise returns False.
name.join(iterable) - Joins the elements of an iterable (like a list or tuple) into a single string, with the string acting as a separator between elements.    
name.format() - Allows you to format strings by inserting values into placeholders defined by curly braces {}. You can specify the order of the values and apply formatting options.    
name.replace(old, new) - Replaces occurrences of a specified substring (old) with another substring (new). 
name.splitlines() - Splits the string into a list of lines, breaking at line boundaries.
name.capitalize() - Capitalizes the first character of the string and converts the rest to lowercase.
name.swapcase() - Swaps the case of each character in the string, converting uppercase to lowercase and vice versa.
"""

name = "    hussein mohammed     "
name = name.strip().title()
first, last = name.split(" ")
print(first)