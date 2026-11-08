#customers.py
#Author: Keerthana Pallela
#Module 11 Lab: Customer Dictionary & Lookup

# Reflection Questions 

# 1. In Exercise 3, I looked up the email key I had deleted in two different ways and got different results. 
# When I used customer.get("email", "no email on file"), it returned the default text and the program kept running.
# However, when I used customer["email"], it gave me a KeyError because the key was missing. 
# The program would have crashed if I had not used try/except to catch the error.
# In real work, I would use bracket notation when a key is required for the program to work correctly. 
# For example, in a billing system, if an invoice is missing its total, I would want the program to show an error instead of treating it as $0. 
# This helps identify the problem right away. I would use .get() when a key is optional and it is normal for it to be missing, such as an email address or phone number on a customer record. 
# The final conclusion is that if a missing key means something is wrong, I use brackets, but if it is normal for a key to be missing, I use .get() with a default value.

# 2. Exercise 8 reminded me of an Excel PivotTable or the SUMIF function because a PivotTable organizes data into groups and shows a total for each group. 
# SUMIF is an Excel function that adds numbers together only when they meet a specific condition. In my code, the loop goes through each transaction one at a time and uses .get(region, 0) to find the total for that region. 
# If it is the first time that region appears, it starts at 0 and then adds the new amount. The dictionary keys work like the row labels in a PivotTable, and the values represent the total for each region.

print("---Exercise 1---")
# One customer stored as a dictionary of key: value pairs
customer = {
    "name": "Alice",                 # text value
    "email": "alice@example.com",    # text value
    "tier": "gold",                  # text value
    "ytd_spend": 12400,              # number value (year-to-date spend)
}

# Key access with square brackets: one field per line
print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
# Print the whole dictionary at once
print(customer)


print("---Exercise 2---")
# Add a new key by assigning to it
customer["phone"] = "555-123-4567"
print("After adding phone:", customer)
 
# Update an existing key by assigning a new value to it
customer["tier"] = "platinum"
print("After updating tier:", customer)
 
# Delete a key (and its value) with del
del customer["email"]
print("After deleting email:", customer)


print("---Exercise 3---")
# .get() returns the default if the key is missing, so no crash
print(customer.get("email", "no email on file"))
 
# Bracket notation raises KeyError when the key is missing,
# so we catch it with try/except
# try:
#     print(customer["email"])
# except KeyError as error:
#     print("KeyError caught: the key", error, "does not exist")

print("---Exercise 4---")
# .items() gives (key, value) pairs, so we can unpack both in the loop
for key, value in customer.items():
    print(f"{key}: {value}")
 
# Looping WITHOUT .items(): only the keys come back
print("Without .items():")
for key in customer:
    print(key)
# Difference: iterating over a dictionary directly gives only the KEYS.
# .items() gives each key AND its value together, which is what we need
# when we want to print "name: Alice". (Without it we'd have to do
# customer[key] inside the loop to get the value.)
 
print("---Exercise 5---")
tier_discounts = {
    "bronze": 0,
    "sliver": 0.05,
    "gold": 0.1,
    "platinum": 0.15
}

purchase = 200
discount_rate = tier_discounts .get(customer["tier"], 0)
final_price = purchase * (1 - discount_rate)

print(f"Tier: {customer['tier']}")
print(f"Discount Rate: {discount_rate *100}%")
print(f"Final Price: ${final_price:.2f}")


print("---Exercise 6---")
customers = [
    {"name": "Bob", "tier": "sliver", "ytd_spend": 3200},
    {"name":"Carol", "tier": "platinum", "ytd_spend": 310},
    {"name": "David", "tier": "bronze", "ytd_spend": 345}
]

# come back to this 
purchase = 300
for record in customers:
    rate = tier_discounts.get(record["tier"], 0)   # look up this customer's rate
    discount_amount = purchase * rate         # dollars saved
    print(f"{record['name']} | {record['tier']} | discount on ${purchase}: ${discount_amount:.2f}")
 

print("---Exercise 7---")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Widget C": {"price": 49.99, "stock": 8},
}

for product_name, product_details in catalog.items():
    if product_details["stock"] < 20:
        print(f"LOW STOCK: {product_name} - only {product_details['stock']} left")


print("---Exercise 8---")
 
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

sales_by_region = {}
for sale in transactions:
    region = sale["region"]
    amount = sale["amount"]
    sales_by_region[region] = sales_by_region.get(region,0) + amount
    print(sales_by_region)

for region in sorted(sales_by_region):
        print(f"{region}: ${sales_by_region [region]}")

