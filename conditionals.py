# Conditionals in Python are used to perform different actions based on different conditions. 
# The most common conditional statements are "if", "elif", "else" - ">, >=, <, <=, ==, !=" -
# "or, "and", "not" are logical operators used to combine conditional statements.

"""""
x, y = 10, 20

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x is equal to y")
#--------------------------------------
if x == 10 and y == 20:
    print("x is 10 and y is 20")
elif x == 10 or y == 20:
    print("Either x is 10 or y is 20")
else:
    print("Neither x is 10 nor y is 20")
#--------------------------------------
if x == y:
    print("it equal")
else:
    print("not equal")
#--------------------------------------
score = 85
if score >= 90:
    print("a")
elif score >= 80:
    print("b")
elif score >= 70:
    print("c")
elif score >= 60:
    print("d")
else:
    print("f")
"""""
# Parity 
# even or odd

"""""
x = int(input("what is x"))
if  x % 2 == 0:
    print("EVEN")
else:
    print("ODD")
"""""
"""""
def main():
    x = int(input("x"))
    if is_even(x):
        print("even")
    else:
        print("odd")
      
      """""
"""""  
def is_even(x):
    
    if x % 2 == 0:
        return True
    else:
        return False
    # improving
    """""
    #improving 01
"""""
    return True if x % 2 == 0 else False
    """""
    # improving 01
"""""
    return x % 2 == 0
main()

x = int(input("What is x"))

"""""
# Match Statements - 
"""""
name = input('what is your name') 
match name:
    case "Harry" | "hermione" | "Ron":
        print("G")
    case "Draco":
        print("S")
    case "Luna":
        print("H")
"""""



