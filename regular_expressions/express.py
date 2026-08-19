# re.search(pattern, string, flags=0)
# search returns an object of the re class that shows the match
#-------------------------------------------------------------------
# re symbols are: ^ (start of the string), $ (end of the string), 
# . (matches any character) matches any character other than newline
# * (matches 0 or more times) 
# + (matches 1 or more times)
# ? (0 or 1 repetitons)
# {m} (matches m repetitions)
# {m,n} (matches m to n repetitions)
# ^ (start of the string), matches the beginning of the string
# $ (end of the string), matches the end of the string or just before the newline at the end of the string
# [] set of characters (everything inside the bracket) 
# [^] complementing a set of characters
#-------------------------------------------------------------------
# r - run as a raw string 

import re


email = input("Email address: ").strip()
#if re.search(r"^.+@.+\.edu$", email):
#if re.search(r"^[^@]+@[^@]+\.edu$", email):
#if re.search(r"^[a-zA-Z0-9_\.]+@[a-zA-Z0-9_]+\.edu$", email):
#if re.search(r"^\w+@\w+\.edu$", email):
#if re.search(r"^\w+@(\w+\.)*\w+\.edu$", email): # * 0 or many times
#if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email):  # ? 0 or 1 time
if re.search(r"^\w+@(\w+\.)?\w+\.edu$", email, re.IGNORECASE):
    print("valid")
else:
    print("invalid")

