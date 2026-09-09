# Create a Book class with __init__ accepting title, author, and pages.
# Create 2-3 different book objects and print their details.
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def is_long(self):
        return self.pages > 300

book1 = Book("Ravanan", "Ravana", 255)
print(f'{book1.title}, {book1.author}, {book1.pages}')
book2 = Book("Emotional Inteligence", "Doctor", 182)
print(f'{book2.title}, {book2.author}, {book2.pages}')

# Add a method is_long(self) to the Book class that returns True if pages > 300. Test it on your book objects.
print(book1.is_long())
print(book2.is_long())

# Create a Car class with make, model, and year attributes,
# plus a method describe(self) that returns a nicely formatted string describing the car.
class Car:
    def __init__(self, make, model, year = 1978):
        self.make = make
        self.model = model
        self.year = year

    def describe(self):
        return f'This {self.make} {self.model} car was manufactured in {self.year}'

car1 = Car("BMW", "M1", "1978")
print(car1.describe())

# # Create 3 TestResult objects with different values
# # Call is_success(), is_slow(), and summary() on each, and print the results
class TestResult:
    def __init__(self, test_name, status_code, response_time_ms):
        self.test_name = test_name
        self.status_code = status_code
        self.response_time_ms = response_time_ms

    def is_success(self):
        return self.status_code in (200, 201, 204)

    def is_slow(self, threshold_ms=300):
        return self.response_time_ms > threshold_ms

    def summary(self):
        result = "PASS" if self.is_success() else "FAIL"
        return f'{self.test_name}: {result} ({self.response_time_ms}ms)'

report1 = TestResult("Login Page", 200, 300)
report2 = TestResult("Payment API", 400, 301)

for report in (report1, report2):
    print(report.is_success())
    print(report.is_slow())
    print(report.summary())