import random

max_attempts = 0
randomNumber = 0
level = input("Choose difficulty (easy/medium/hard): ").lower()

if level == "easy":
    max_attempts = 15
    randomNumber = random.randint(1, 50)
elif level == "medium":
    max_attempts = 10
    randomNumber = random.randint(1, 100)
elif level == "hard":
    max_attempts = 5
    randomNumber = random.randint(1, 200)
else:
    print("Invalid choice, defaulting to medium.")
    max_attempts = 10
    randomNumber = random.randint(1, 100)

user_attempts = 0
while user_attempts < max_attempts:
    userInput = int(input("Please enter the number: "))
    if userInput == randomNumber:
        print(f"Your entered number {userInput} is Correct!")
        break
    elif userInput < randomNumber:
        print("To low, try again")
    else:
        print("Too high, try again")
    user_attempts += 1
else:
    print(f"Out of attempts! The number was {randomNumber}.")
