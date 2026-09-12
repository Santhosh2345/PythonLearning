# Task 1
# Write a while loop that counts down from 10 to 1, then prints "Liftoff!"
count = 10
while count > 0:
    print ("Liftoff")
    count -= 1

# Task 2
# Write a sentinel loop: keep asking the user to enter numbers, and stop when they type "done."
# Keep a running total of all numbers entered (accumulator pattern), and print the total at the end.
inputNumber = []
count = 0
total = 0
while True:
    userInput = input("Please enter the number (or enter DONE to exit): ")
    try:
        if userInput.upper() == "DONE":
            break
        inputNumber.append(float(userInput))
        count += 1
    except ValueError:
        print(f"That's not a valid number.", end=" ")
print(inputNumber)

for num in inputNumber:
    total += num
print(total)

# Task 3
# Write a while loop that keeps asking "What's the password?"
# until the user types the correct password (pick any word you like), then prints "Access granted."
password = "Password!44"
while True:
    userInput = input("What's the password? ")
    if userInput == password:
        print ("Access granted")
        break