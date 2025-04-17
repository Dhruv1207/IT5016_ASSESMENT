import random

def student_result(*marks):
    """
    This function accepts any number of marks, calculates the average,
    and prints whether the student passed or failed.
    """
    total = 0
    for mark in marks:
        total += mark
    avg = total / len(marks)
    print("\nTask 1: Student Result Check")
    print("Average score =", avg)
    if avg >= 50:
        print("Student Passed!")
    else:
        print("Student Failed!")

# Call the function with example scores
student_result(45, 67, 90, 50)

# -------------------------------
# Task 2 (i): fruit_price(**kwargs) with explanation
# -------------------------------

def fruit_price(**kwargs):
    """
    This function accepts fruit names and their prices as keyword arguments,
    then calculates and returns the total price.
    """
    sum = 0  # Initialize sum
    for i in kwargs.values():  # Loop through all prices
        sum += i  # Add each price to the sum
    return sum  # Return the total

# Call the function with sample fruits
k = fruit_price(mango=10, Apple=5, Orange=15)

# Print result
print("Task 2 (i): Total fruit price")
print(k)

# -------------------------------
# Task 2 (ii): Display only keys from kwargs
# -------------------------------

def fruit_names_only(**kwargs):
    """
    This function prints only the fruit names (i.e., the keys of the kwargs dictionary).
    """
    print("\nTask 2 (ii): Fruit names only")
    for fruit in kwargs.keys():  # Loop through only keys
        print(fruit)

# Call the function
fruit_names_only(mango=10, Apple=5, Orange=15)

# -------------------------------
# Task 3: Average student scores using **kwargs
# -------------------------------

def average_scores(**student_scores):
    """
    This function accepts student IDs and their scores using **kwargs,
    calculates the average score, and prints it.
    """
    total = 0
    count = 0
    for score in student_scores.values():
        total += score
        count += 1
    avg = total / count
    print("Task 3: Average student scores")
    print("Average score of all students =", avg)

# Call the function with student data
average_scores(IT5014=60, IT7809=80, IT6798=50, IT5048=70)

# -------------------------------
# Task 4: Generate random numbers
# -------------------------------

# (i) Using random method
print("Task 4 (i): Single random number between 1 and 20")
print(random.randint(1, 20))

# (ii) Generate random numbers from 1 to 20 without repetition
def unique_random_numbers():
    """
    This function generates and prints 20 unique random numbers from 1 to 20.
    """
    numbers = random.sample(range(1, 21), 20)  # Get 20 unique numbers
    print("Task 4 (ii): Random numbers from 1 to 20 without repetition")
    print(numbers)

# Call the function
unique_random_numbers()