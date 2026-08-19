# Take a messy string like "   Test Passed   ", clean it with .strip(),
# then check if it .startswith("Test").
value = "   Test Passed   "
print(value.strip())
print(value.startswith("Test"))

# Take a CSV-style string "apple,banana,cherry", split it into a list,
# then join it back together using " | " as the separator instead of a comma.
value2 = "apple,banana,cherry"
listValue2 = value2.split(",")
print(listValue2)
listValue2Join = " | ".join(listValue2)
print(listValue2Join)

# Take a sentence and replace one word with another using .replace().
text = "I like cats and cats."
text = text.replace("cats", "dogs")
print(text)

# To replace 1st word in the sentence called count limit
text = text.replace("dogs", "cats", 1)
print(text)

# Check whether a filename ends with .csv and starts with "data_".
fileName = "data_info.csv"
print(fileName.startswith("data"))
print(fileName.endswith(".csv"))

# Clean the extra whitespace
# Check if it contains "200" (pass) or an error code like "404"/"500" (fail)
# Split the cleaned string by spaces and print each piece
# Bonus: use .replace() to mask the endpoint, e.g. replace "/users/1" with "/users/***"
api_log = "  [200] GET /users/1 - 145ms  "
api_log = api_log.strip()
if "200" in api_log:
    print("Pass")
elif "404" in api_log or "500" in api_log:
    print("Fail")

api_log_list = api_log.split(" ")

for words in api_log_list:
    print(words)

# End point masking
mask = api_log.replace("users/1", "users/***")
print(f'The masked value: {mask}')

# Dynamic masking
user_id = api_log.split("/users/")[1].split(" ")[0] #This line first gives ["", "1 - 145ms  "] and we get the index 1
# Then from frist index string we split it with the space, it gives ["1", "-", "145ms"], from here we get the 0th index
print(user_id)
maskedValue = api_log.replace(user_id, "***", 1)
print(maskedValue)

# Bug what if 1 is present in [201]
# FIX
before, separator, after = api_log.partition("/users/")
print(before)
print(separator)
print(after)

userID, rest = after.split(" ", 1)
print(userID)
print(rest)

masked = before + separator + "***" + rest
print(masked)