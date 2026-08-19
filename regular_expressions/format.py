import re

# := the walrus operator in python - its assign a value and check the condition

"""
name = input("What is your name?").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)

#if matches:
#    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name.title()}")
"""

# cleaning up input - for example asking user for url to get a username from the url
# https://randomfunfacts.com/husseinmhm

# using regular python function
"""
url = input("URL:").strip()     
username = url.replace("https://randomfunfacts.com/", "")
print(f"username: {username}")
"""


# using regular expressions to handle multiple cases of urls
# https://randomfunfacts.com/husseinm
# re.sub(pattern, repl, string, count=0, flags=0) 


 
# url = input("URL:").strip()  
# username = re.sub(r"^(https?://)?(www\.)?randomfunfacts\.com/", "", url) 
# print(f"username: {username}")


url = input("URL:").strip() 
if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z-0-9_]+)$", url, re.IGNORECASE):
    print(f"username:", matches.group(1))
else:
    print("Invalid URL")



