# Exeptions - In Python, exceptions are objects that represent conditions 
# under which your program can run properly (usually an error occurred). 
# These errors occur during the execution of a Program and give instructions 
# on how to handle them. This is done through try-except blocks - these allow you control flow
# by handling different types or instances/errors in case they happen at runtime.

# Type of errors :
# ValueError -- the error that caused by the value of a variable 
# NameError - the name you are trying to reference in your code is not defined in any scope


# Try 
"""""
try:
    x = int(input("Please enter an integer: "))
    print(f"x is {x}")
except ValueError:
    print('You did not entered a number')
#-------------------------------------------------
try:
    x = int(input("Please enter an integer: "))
except ValueError:
    print('You did not entered a number')
else:
    print(f"x is {x}")
"""""
"""""
while True:
    try:
        x = int(input("what is x"))
    except:
        print('x is not a number')
    else:
        break
print(f"x is {x}")
"""""

"""""
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("what is x "))
        except ValueError:
            # pass # we can just pass - means if we dont want to display a message to the user - used the pass statement
            print("please enter a number")              # instead of using pass you can put any print
        else:
           return x # if you use return here it will

main()
"""""
# more refiments on the get_int to make more reusable
def main():
    x = get_int("What is X")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            # pass # we can just pass - means if we dont want to display a message to the user - used the pass statement
            print("please enter a number")              # instead of using pass you can put any print
        else:
           return x # if you use return here it will

main()
