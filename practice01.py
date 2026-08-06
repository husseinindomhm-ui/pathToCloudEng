"""""
Challenge 1: E-Commerce Receipt Formatter
Scenario: You are building a point-of-sale terminal for a local coffee shop.
Objective:

1. Ask the user for:
    .The customer's full name.
    .The coffee item they ordered (e.g., " iced mocha ").
    .The quantity ordered.
    .The price per item (e.g., 4.5).
2. Clean up the user input:
    .Capitalize the customer's name properly (Title Case) and remove leading/trailing spaces.
    .Strip spaces and lowercase the item name.
3. Calculate the total cost (including a 10% tax).
4. Output a clean receipt where:
    .The customer is greeted by name.
    .The total amount is formatted as currency with two decimal places (e.g., $9.90).
Key concepts tested: input(), strip(), title(), lower(), type casting (float(), int()), basic math, and f-strings formatting (:.2f).
"""""
"""""
cus_name = input("What is your name?").title()
cof_ordered = input("What is your coffee item ordered?").lower().strip()
qty_ordered = int(input("How many you ordered"))
price_per_item = float(input("What is price per item? "))

tax = 0.1
total = qty_ordered * price_per_item
calc_tax = total * tax
total_bill = calc_tax + total

print(f"Welcome {cus_name}")
print(f"Your item is {cof_ordered} - Qty{qty_ordered}")
print(f"Total bill is ${total_bill:.2f}")
"""""
"""""
Challenge 2: Tip & Bill Split Calculator
Scenario: A group of friends is splitting a dinner bill at a restaurant.
Objective:
Write a program that prompts the user for:
    .Total bill amount (e.g., $125.50 or 125.50).
    .Tip percentage they'd like to give (e.g., 15 for 15%).
    .Total number of people splitting the bill.
Requirements:
    .Handle inputs cleanly (if the user types a $ in the bill, handle or strip it out using .replace("$", "")).
    .Create a custom function named calculate_split(bill, tip_percent, people) that returns the amount each person owes.
    .Print the final amount per person formatted to two decimal places.
Key concepts tested: Custom functions (def), return values, string manipulation (replace), float conversion, and arithmetic operators.
"""""

"""""
Challenge 3: User Profile & Username Generator
Scenario: A website registration system needs to standardise input data and auto-generate a handle for new users.
Objective:
    .Ask the user for their first name and last name in a single input() prompt (e.g., "  john DOE  ").
    .Use string splitting (.split()) to separate the first and last name into two variables.
    .Define a custom function create_username(first, last) that:
        .Takes the first letter of the first name (lowercased) + the entire last name (lowercased).
        .Example: "John Doe" becomes "jdoe".
    .Define a custom function greet_user(name="Guest") with a default parameter value that prints a welcome message.

    .Print out the formatted greeting and their generated username.
Key concepts tested: split(), indexing strings (name[0]), default parameter values in functions, and string concatenation/f-strings.
"""""



