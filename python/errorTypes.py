# # NameError
# print(userName)
#
# # ZeroDivisionError
# print(10/0)
#
# # ValueError
# print(int("abc"))
#
# # TypeError
# print("abc" + 123)
#
# # SyntaxError
# # print(

# Write a try/except/else/finally block around a division operation.
# Test it with valid numbers (see else and finally both run) and with a zero divisor (see except and finally run, but not else).
def division(number):
    return 5/number

def call_out(number):
    try:
        a = division(number)
        print(a)
    except ZeroDivisionError as e:
        print(e)
    else:
        print("Given value divided successfully")
    finally:
        print("Division funtion executed")

call_out(5)
call_out(0)

# Write a function withdraw(balance, amount) that raises a ValueError if amount > balance.
# Call it with valid and invalid values, wrapped in a try/except to catch and print your custom message.
user_input = float(input("Please enter the amount to withdraw: "))
balance = 10000
def withdraw(withdraw_amount):
    if withdraw_amount > balance:
        raise ValueError(f'Entered amount greater than balance amount {balance}')
    else:
        print("Amount withdraw successfully")

try:
    withdraw(user_input)
except Exception as e:
    print(e)

# Deliberately write a bare except: version of some risky code,
# then rewrite it catching only the specific exception type — compare the two.
def risky_funtion():
    b = [1,2,4]
    print(b[2])
    a = int(input("Enter the value: "))

try:
    a = risky_funtion()
except ValueError:
    print("Value Error")
except:
    print("In exception")

# Write a function that opens a (possibly non-existent) file, using try/except FileNotFoundError,
# with a finally block that prints "Attempt finished" regardless of outcome.
def file_open(file_name):
    try:
        file = open(file_name)
    except FileNotFoundError:
        print("File not found")
    finally:
        print("Attempt finished")

file_open("data.py")

def validate_response(status_code, response_time_ms):
    # Raise a ValueError if status_code is not in [200, 201, 204]
    if status_code not in [200, 201, 204]:
        raise ValueError(f'{status_code} is not in the list')
    # Raise a ValueError if response_time_ms is negative
    if response_time_ms < 0:
        raise ValueError(f'response_time {response_time_ms} is negative')
    # Otherwise, return "Valid response"
    return "Valid response"

# Call this function wrapped in try/except, testing:
# - a normal valid case
try:
    a = validate_response(200, 102.34)
    print(a)
except Exception as e:
    print(e)
finally:
    print("Validation attempt complete")

print("#-----------#")

# - an invalid status code
try:
    a = validate_response(301, 102.34)
    print(a)
except Exception as e:
    print(e)
finally:
    print("Validation attempt complete")

print("#-----------#")

# - a negative response time
try:
    a = validate_response(200, -0.1)
    print(a)
except Exception as e:
    print(e)
finally:
    print("Validation attempt complete")
# Print appropriate messages for each case, and use finally to print "Validation attempt complete"
print("#-----------#")