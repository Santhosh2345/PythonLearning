# Create a dictionary representing a test case: test_name, status (pass/fail), and duration_ms.
# Print each value using both [] and .get().
dic_one = {
    "testCase": "Test One",
    "status": "Pass",
    "duration_ms": 204
}
print(dic_one["testCase"])
print(dic_one["status"])
print(dic_one["duration_ms"])

print(dic_one.get("testCase"))
print(dic_one.get("status"))
print(dic_one.get("duration_ms"))

# Add a new key "tags" with a list of values (like ["smoke", "regression"]).
# Update the status value.
# Remove the duration_ms key.
dic_one["tags"] = ["smoke", "regression"]
dic_one["status"] = "Fail"
del dic_one["duration_ms"]

# Loop through the dictionary using .items() and print each key-value pair nicely formatted.
# Enumerate funtion, we can get the key, value pair
for key, value in dic_one.items():
    print(f'{key}: {value}')
list1 = [12, 45, 11]
for index, value in enumerate(list1):
    print(f'{index}: {value}')

# Try accessing a key that doesn't exist using [] (observe the KeyError),
# then safely access it using .get() with a default value instead.
try:
    print(dic_one["Key not exist"])
except Exception as e:
    print(f"Error occurred: {e}")

print(dic_one.get("Key not exist"))

# Print the status code using .get()
# If status_code is not 200, print the nested error message from inside "body"
# Print a default message using .get() if "response_time_ms" doesn't exist in the dictionary
api_response = {
    "status_code": 404,
    "endpoint": "/users/99",
    "body": {
        "error": "User not found"
    }
}

print(f'Status code is: {api_response.get("status_code")}')
if api_response.get("status_code") != 200:
    print(api_response["body"]["error"])

print(f'Response time is: {api_response.get("response_time_ms", "Response time is missing")}')