# Given a list of numbers 1 to 20, use a list comprehension to build a list of only the numbers divisible by 3.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,16, 17, 18, 19, 20]
numbers_div_3 = [n for n in numbers if n % 3 == 0]
print(numbers_div_3)

# Given a list of words, use a list comprehension to build a list of their lengths (hint: len(word)).
words = ["Light", "Spark", "Heaven", "Space", "Orbit", "Milkyway"]
word_len = [len(word) for word in words]
print(word_len)

# Take one of your OLD Day 8 or Day 9 loop-based solutions
# (like building a list of successful status codes) and rewrite it as a one-line comprehension. Compare the two side by side.

# Given a dictionary of {name: score} pairs,
# use a dict comprehension to build a new dictionary containing only entries where the score is above 50.
score_board = {"Mercury": 50, "Earth": 100, "Venus": 49, "Saturn": 51}
entries = {name: score for name, score in score_board.items() if score > 50}
print(entries)

# QA-flavored: create a list of HTTP status codes (mix of 200s, 404s, 500s).
# Loop through and print "OK" for 200, "Client Error" for 4xx codes, "Server Error" for 5xx codes.
# (Hint: you can check ranges with comparisons, like code >= 400 and code < 500.)
status_codes = [200, 400, 500, 401, 201, 501, 302]
count = 0
entries_code = ["Ok" if status_code >= 200 and status_code < 300 else "Client Error" if status_code >= 400 and status_code < 500
                else "Server Error" if status_code >= 500 and status_code < 600 else "Unknown Error" for status_code in status_codes]
print(entries_code)

# Use a list comprehension to get only response times under 300ms (consider these "fast")
# Use a list comprehension to build a list of strings like "145ms" from the numbers
# Bonus: use a dict comprehension to map each index to its response time, e.g. {0: 120, 1: 340, ...}
response_times = [120, 340, 95, 480, 210, 150, 610, 88]
response_times_under_300ms = [f'{str(response_time)}ms' for response_time in response_times if response_time < 300]
print(response_times_under_300ms)

response_dic = {response_times.index(response_time): response_time for response_time in response_times}
print(response_dic)

# Alternative method
response_dic1 = {index:value for index, value in enumerate(response_times)}
print(response_dic1)