# Def -- handmade function


def great(to = "world"):
    print(f"hello to: {to} !")

name = input("enter your name : ")
if name == "":
    great()
else: great(name)