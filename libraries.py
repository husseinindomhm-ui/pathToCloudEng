import random # its a defult library of python, import modules_name will import the entire module 
# --> using from keyword we can select only specific functions to be imported from a module, 
#     therefore we dont need to call the module name before the function name

# from random import choice  
#x = choice([1, 4, 5])


# num = random.randint(1, 6) # returns a random integer between the specified range
# print(num) 
"""""
cards = ["jack", "queen", "king"]
random.shuffle(cards) # it will shuffle a list of values randomly 

for card in cards:
    print(card)
"""""

check_even = lambda x: "Even" if x % 2 == 0 else "Odd"

print(check_even(5))
