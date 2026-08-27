# Write a function sum_all(*args) that adds up any number of arguments passed to it.
# Test it with 2 numbers, then 5 numbers.
def sum_all(*args):
    add = 0
    for n in args:
        add += n
    print(add)

sum_all(1, 2)
sum_all(1, 2, 3, 4, 5)

# Write a function print_details(**kwargs) that prints each keyword argument on its own line.
# Call it with at least 3 different keyword arguments.
def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print_details(name="Santhosh", age=28, male=True)

# Recreate the UnboundLocalError bug yourself
# Write a function that tries to modify a variable defined outside it without using global or passing it in, and observe the error.
add = 0
def sum_all2(**kwargs):
    try:
        global add
        for value in kwargs.values():
            add += value
        return add
    except Exception as e:
        print(f'Error: {e}')

sum_all2()

# Fix that same function two ways: once using global (just to see it work),
# and once using the "pass in, return out" pattern (the better way).
test = {"a": 5, "b": 4}
test2 = {"c":3, "d": 8}
print(sum_all2(**test, **test2))

# Call it with a few test names and some keyword metadata, and print the returned count
def build_test_report(*passed_tests, **metadata):
    passed_tests_sum = 0
    # Print each passed test name
    for test in passed_tests:
        print(test)
        passed_tests_sum += 1

    # Print each piece of metadata (like duration=120, environment="staging")
    for key, value in metadata.items():
        print(f'{key}: {value}')

    # Return a count of how many tests passed
    return passed_tests_sum

count = build_test_report("testLogin", "testHomePage", "testLogout", duration="120", environment="staging")
print(f'Number of passed tests: {count}')