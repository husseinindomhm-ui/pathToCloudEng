# Def -- handmade function

"""""
def great(to = "world"):
    print(f"hello to: {to} !")

name = input("enter your name : ")
if name == "":
    great()
else: great(name)
"""""
def main():
    name = input("enter your name : ")
    if name == "":
        great()
    else: great(name)


def great(to = "world"):
    print(f"hello to: {to} !")

main()

"""""
def main():
    x = int(input("what is x ?"))
    print("x squared is", square(x))

def square(n):
    return n * n

main()
"""""