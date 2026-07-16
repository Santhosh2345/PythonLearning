askingNumber = input('Please enter any number: ')
userEnteredNumber = float(askingNumber)

if userEnteredNumber > 0:
    print(f"You entered number {userEnteredNumber} is Positive")
elif userEnteredNumber < 0:
    print(f"You entered number {userEnteredNumber} is Negative")
else:
    print(f"You entered number {userEnteredNumber} is Zero")