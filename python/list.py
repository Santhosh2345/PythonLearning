# Create a list of 5 fruits. Print the first, the last, and a slice of the middle 3
fruits = ["Apple", "Cherry", "Dragon Fruit", "Mango", "Ezhantha Pazham"]

print(f"The first fruit is {fruits[0]}")
print(f"The last fruit is {fruits[-1]}")
print(f"The last fruit is {fruits[1:4]}")

# Add a new fruit to the end. Insert one at position 0. Remove one by value
fruits.append("Seetha Pazham")
fruits.insert(0, "Sappotta Pazham")
fruits.remove("Apple")
print(len(fruits))

# Loop through the list using enumerate() and print "Item 0: apple" style output for each.
for index, fruit in enumerate(fruits):
    print(f"Item {index}: {fruit}")

# QA-flavored: create a list of HTTP status codes (mix of 200s, 404s, 500s).
# Loop through and print "OK" for 200, "Client Error" for 4xx codes, "Server Error" for 5xx codes.
# (Hint: you can check ranges with comparisons, like code >= 400 and code < 500.)
status_codes = [200, 405, 202, 204, 409, 500, 501, 503, 431]
for status_code in status_codes:
    if status_code >= 200 and status_code < 300:
        print("OK")
    elif status_code >= 400 and status_code < 500:
        print("Client Error")
    elif status_code >= 500 and status_code < 600:
        print("Server Error")