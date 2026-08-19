# Create a tuple of 3 coordinates (like (x, y) pairs aren't needed — just 3 plain values).
# Try to modify one item and observe the error.
t_values = (10, 21, 10)
try:
    t_values[0] = 11
except TypeError as e:
    print(f"Error: {e}")

# Create a list with duplicate numbers, convert it to a set to remove duplicates, then print how many unique values remain.
list_value = [1, 4, 5, 1, 5, "One", "One", "Two"]
set_value = set(list_value)
print(f"Number of unique values are {len(set_value)}")

# Create two sets of your own choosing (like favorite foods) and find their .union() and .intersection().
set_1 = {"Two", 2.22, "Three", "Five", "Mutton", 6}
set_2 = {"Two", 2.20, "Three", "Six", 6}
print(f'Combined set value {set_1.union(set_2)}')
print(f'Common values are {set_1.intersection(set_2)}')

# Print bugs that appeared in BOTH runs (intersection)
# Print bugs that are new in run2 (in run2 but not run1)
# Print bugs that were fixed (in run1 but not run2)
run1_bugs = {"BUG-101", "BUG-102", "BUG-103", "BUG-104"}
run2_bugs = {"BUG-103", "BUG-104", "BUG-105"}
print(f'Bugs that appeared in BOTH runs {run1_bugs.intersection(run2_bugs)}')
print(f'Bugs that are new in run2 {run2_bugs - run1_bugs}')
print(f'Bugs that were fixed in run1 but not run2 {run1_bugs - run2_bugs}')

for bug in run2_bugs:
    print(bug)

if "Bug-103".upper() in run2_bugs:
    print(f'{"Bug-103".upper()} is present')