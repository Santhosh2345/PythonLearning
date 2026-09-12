# Create an empty dictionary to hold contacts
# Loop forever, showing a menu each time
# Ask the user to pick an option (1-6, or whatever numbering you choose)
# Based on their choice, run the matching action:
# Add — ask for name + phone, store it in the dictionary
# Search — ask for a name, look it up, handle "not found" gracefully
# Update — ask for a name, check it exists, ask for new phone, overwrite it
# Delete — ask for a name, check it exists, remove it
# View All — loop through the dictionary and print every contact
# Exit — break out of the loop, end the program
# Repeat from step 2, until Exit is chosen

contacts = {}

while True:
    try:
        userChoosenOption = int(input(f"Pick an option: \n 1 for Add \n 2 for Search \n 3 for Update \n 4 for Delete \n 5 for VIew All \n 6 for Exit \n"))
    except Exception as e:
        print(f'Error in user input {e}')
        continue

    if userChoosenOption == 1: #Add
        print("Choosed option is Add")
        name = input(f'Enter the name: ')
        if name in contacts:
            print(f'Given name already exists')
        else:
            contacts[name] = int(input(f'Enter the number: '))
            print(f'Contact added successfully!')

    elif userChoosenOption == 2: #Search
        print("Choosed option is Search")
        givenName = input(f'Enter the name to search: ')
        count = 0
        for name, number in contacts.items():
            if givenName.lower() in name.lower():
                print(f'{name}: {number}')
            else:
                count += 1
                if count == len(contacts):
                    print(f'Entered name is not in the contact:(')

    elif userChoosenOption == 3: #Update
        print("Choosed option is Update")
        name = input(f'Enter the name to search: ')
        if name in contacts:
            contacts[name] = int(input("Update the number: "))
            print(f'{name} updated successfully!')
        else:
            print("Entered name is not in the contact:(")

    elif userChoosenOption == 4: #Delete
        print("Choosed option is Delete")
        givenName = input(f'Enter the name to search: ')
        for name, number in contacts.items(): #This is the alternate method using loop
            if givenName == name:
                deletedKeyNum = contacts.pop(givenName, None)
                print(f'Contact {name}: {deletedKeyNum} is deleted successfully!')
                break
            else:
                print("Entered name is not in the contact:(")

    elif userChoosenOption == 5: #View All
        print("Choosed option is View All")
        print("All contacts: ")
        for name, number in contacts.items():
            print(f'{name}: {number}')

    elif userChoosenOption == 6:
        print("Thank you :)")
        break