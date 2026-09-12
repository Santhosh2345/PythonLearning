# Write a function square(number) that returns the number squared.
# Call it with a few different values and print the results.
def square(number):
    return number ** 2

print(square(2))
print(square(34))

# Write a function is_even(number) that returns True if the number is even, False otherwise.
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(55))
print(is_even(126))

# Write a function greet_user(name, time_of_day="morning") with a default parameter,
# and call it both with and without specifying time_of_day.
def gree_user(name, time_of_day="morning"):
    print(f'Good {time_of_day} {name}:)')

gree_user("Santhosh", "Night")
gree_user("Santhees")

# Write a function that deliberately only uses print() internally (no return),
# then try to save its result into a variable and print that variable — observe the None result firsthand, like the lesson showed.
def test():
    print()

a = test()
print(a)

# QA Flavoured task
def is_valid_status_code(code):
    # return True if code is one of 200, 201, 204 — False otherwise
    return code in [200, 201, 204]

def format_test_result(test_name, passed):
    # return a formatted string like "test_login: PASS" or "test_login: FAIL"
    if passed:
        return f'{test_name}: PASS'
    else:
        return f'{test_name}: FAIL'

# Try calling both functions with a few different inputs and print the results
print(is_valid_status_code(204))
print(format_test_result("Test_Credential_Page", is_valid_status_code(500)))
print(format_test_result("Test_Credential_Page", is_valid_status_code(200)))
