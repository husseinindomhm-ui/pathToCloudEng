"""
print("Hello, World!")
x = 5
print("The value of x is:", x)

def main(x = 10, y = 20):
    print("The value of x in main is:", x)
    print("The value of y in main is:", y)
    print("The sum of x and y is:", x + y)


main()  # Calls main with default values"
"""

small = "HELLO".lower()  # Converts "HELLO" to lowercase and assigns it to small


def area(length, width):
    return length * width


def main_area():

    house = area(10, 20)
    yard = area(5, 15)
    total = house + yard
    print(str(total) + " is the total area of the house and yard.")
    print(small)  # Prints the lowercase version of "HELLO"


main_area()  # Calls main_area to calculate and print the total area
