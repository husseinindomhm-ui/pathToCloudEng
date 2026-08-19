def main():
    name = input("what's your name?")
    print(hello(name))
    
def hello(to="world"):
    return f"Hello to {to}"


if __name__ == "__main__:":
    main()
    