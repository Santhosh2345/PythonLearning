# Create a list of 6 unsorted numbers.
# Print it sorted ascending using sorted() (without changing the original),
# then sort the original in place using .sort().
numbers = [45, 88, 2, 0, 45, 00]
copy = sorted(numbers)
print(copy)
numbers.sort()
print(numbers)

# Using min(), max(), sum(), and len(), calculate and print the average of a list of numbers.
print(f'Average of number: {sum(numbers)/len(numbers)}')

# Create two small lists and combine them with +.
# Then create a list of 5 zeros using *.
list1 = ["Home", "Car"]
list2 = [1, 2, 0]
list_1_2 =  list1 + list2
print(f'Combined list {list_1_2}')

if 0 in list_1_2:
    position = list_1_2.index(0)
    zeros = [list_1_2[position]] * 5
    print(zeros)

# Recreate the copy trap yourself: create a list, assign it to a second variable without .copy(),
# modify the second one, and print both to see the shared-reference bug happen firsthand.
# Then fix it using .copy() and confirm the original stays untouched.
original = ["Hello", 1]
copy = original.copy()
copy.remove(1)
copy.append("World")
print(original[-1], copy[-1])

# response_times = [120, 340, 95, 480, 210, 150]  # in milliseconds
# Print the fastest response, slowest response, and average response time
# Then sort the list ascending and print it, without modifying the original list
response_times = [120, 340, 95, 480, 210, 150]
print(f"Fastest response time {min(response_times)}")
print(f"Slowest response time {max(response_times)}")
print(f"Average response time {sum(response_times)/len(response_times)}")

asceding_response_times = sorted(response_times)
print(f"Ascending response times: {asceding_response_times}")