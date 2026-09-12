import json
from python.FileHandle import workingWithJson as path

user_input = "" # User input variable
get_last_index_id = 0 # List last index id value from json file
expenses_list = [] # To append expenses dictionary in each index
json_data_reader = {} # Load the json file
user_expenses_len = 0 # To store the length of user_expenses list from the json file
category_key: dict[str, int] = {} # To store category key and sum the total amount

# Start with an empty list (or load existing expenses from a JSON file, if one exists)
def load_expenses_if_exist():
    try:
        # Reading file and get the data, user_expenses list length, id value of last index
        # Appending the read user_expenses list to expenses_list variable if expenses exists in the json
        with open(f'{path.project_root_path}\\Expenses.json', "r") as file:
            global json_data_reader
            global user_expenses_len
            global get_last_index_id
            json_data_reader = json.load(file)
            user_expenses_len = len(json_data_reader.get("user_expenses"))
            print(f"Number of user expenses: {user_expenses_len}")

        if user_expenses_len > 0:
            for i in range(0, user_expenses_len):
                expenses_list.append(json_data_reader.get("user_expenses")[i])
                get_last_index_id = json_data_reader.get("user_expenses")[-1].get("id")
            print(json_data_reader)
        else:
            print("No expenses data")

    except Exception as e:
        print(e)

# Calling function
load_expenses_if_exist()

# Continuously ask the user to select the option until user choose option "4 for Save & Exit"
while True:
    user_input = input("Please choose an option:\n 1 for Add Expense\n 2 for View All\n "
                       "3 for View Summary by category\n 4 for Save & Exit\n")
    if user_input != "1" and user_input != "2" and user_input != "3" and user_input != "4":
        print("Please enter valid input!")
        continue

    # If user input is 1 entered values are added to the dictionary and dictionary appending to the expenses_list (from 0 or existing index)
    # dictionary variable created inside the while loop to avoid override dictionary value in the list
    if user_input == "1":
        while True:
            amount = input("Please enter the amount: ")
            try:
                amount = float(amount)
                break
            except Exception as e:
                print(e)
        category = input("Please enter the category: ")
        description = input("Please enter the description: ")

        # Adding the input to the dictionary
        get_last_index_id += 1
        expenses_dict = {}
        expenses_dict["id"] = get_last_index_id
        expenses_dict["amount"] = amount
        expenses_dict["category"] = category
        expenses_dict["description"] = description

        # Append the dictionary to the list
        expenses_list.append(expenses_dict)
        print(f'This is expenses adding list: {expenses_list}')
        json_data_reader["user_expenses"] = expenses_list
        print(json_data_reader)

    # If the user_input is 2, prints the existing expenses data in the json format if data exist else prints nothing
    elif user_input == "2":
        for expense in expenses_list:
            data = json.dumps(expense, indent=4)
            print(data)

    # If user_input is "3" loop through the expenses_list and get the category and stored in tuple to avoid duplicate key
    elif user_input == "3":
        for expense in expenses_list:
            # Check the is the key is not in the category_key variable, then add that key with the amount
            if expense.get("category") not in category_key:
                category_key[expense.get("category")] = 0 + int(expense.get("amount"))
            # else, if the key is already exist in the category_key variable, sum with the exiting value
            else:
                category_key[expense.get("category")] = int(expense.get("amount")) + category_key.get(expense.get("category"))
                print(category_key.get(expense.get("category")))
        print(json.dumps(category_key, indent=4))

    # When the user_input is "4",
    # Parse the existing JSON file using json_data_reader and append the new expense record to the user_expenses list.
    # And then update the user_expenses key in the json_data_reader dictionary
    # Then break the loop
    else:
        with open(f'{path.project_root_path}\\Expenses.json', "w") as file:
            json.dump(json_data_reader, file, indent=4)
        print("Thank You:)")
        break


# AI given data structure
# expenses = load_expenses()
#
# while True:
#     print("\n--- Expense Tracker ---")
#     print("1. Add Expense")
#     print("2. View All Expenses")
#     print("3. View Category Summary")
#     print("4. Save & Exit")
#
#     choice = input("Choose an option: ")
#
#     if choice == "1":
#         # your turn: get input, call add_expense()
#         pass
#     elif choice == "2":
#         view_all_expenses(expenses)
#     elif choice == "3":
#         summary = category_summary(expenses)
#         # your turn: print the summary nicely
#         pass
#     elif choice == "4":
#         save_expenses(expenses)
#         print("Expenses saved. Goodbye!")
#         break
#     else:
#         print("Invalid choice, please try again.")