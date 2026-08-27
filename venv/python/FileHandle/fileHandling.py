import csv
import os
# Write a .txt file with 3 lines of your choosing.
# Then read it back three different ways: .read(), .readlines(), and looping line-by-line.
dir_path = os.path.dirname(os.path.abspath(__file__))
project_root_path = os.path.join(dir_path, "..", "..", "..") #This means cd.. means Change Directory to the parent folder, 3 "..", 3 folder up
print(f'Project folder path: {project_root_path}')
with open(f'{project_root_path}\\test_data.txt', "r") as file:
    value = file.read()
    print(value)
print("#____#")

with open(f'{project_root_path}\\test_data.txt', "r") as file:
    value = file.readline()
    print(value)
print("#____#")

with open(f'{project_root_path}\\test_data.txt', "r") as file:
    value = file.readlines()
    print(value)
    print(value[0])
print("#____#")

# Create a list of dictionaries representing 3 fake test results (test_name, status, duration_ms).
# Write them to a .csv file using csv.DictWriter.
test_results = [
    {"test_name":"Smoke Test", "status":"Success", "duration_ms": 200.45},
    {"test_name":"Sanity Test", "status":"Fail", "duration_ms": 500},
    {"test_name":"Setting Test", "status":"Success", "duration_ms": 200.45}
]

with open(f'{project_root_path}\\test_data.csv', "w", newline="") as file:
    fieldnames = ["test_name", "status", "duration_ms"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(test_results)

# Read that same CSV file back using csv.DictReader, and print each row's test_name and status.
with open(f'{project_root_path}\\test_data.csv', "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f'{row["test_name"]}: {row["status"]}')

# Try opening a file that doesn't exist,
# wrapped in try/except FileNotFoundError, and confirm it fails gracefully instead of crashing.
try:
    with open(f'{project_root_path}\\file_not_found.txt', "r") as file:
        list_var = file.readlines()
except FileNotFoundError:
    print(f'File not exist in the directory: {project_root_path}')
