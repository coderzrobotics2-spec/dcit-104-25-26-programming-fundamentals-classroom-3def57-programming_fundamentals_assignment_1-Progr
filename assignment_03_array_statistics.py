# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 3
# Topic: Lists (Arrays), Loops, and Functions
# =============================================================================
#
# TASK: Array Statistics Calculator
#
# Write a Python program that reads a collection of numbers from the user
# and computes key statistical values using separate functions.
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT / OUTPUT EXAMPLE
# -----------------------------------------------------------------------------
#
#   How many numbers? 5
#   Enter number 1: 4
#   Enter number 2: 7
#   Enter number 3: 2
#   Enter number 4: 9
#   Enter number 5: 1
#
#   Results:
#   Sum:     23
#   Average: 4.6
#   Maximum: 9
#   Minimum: 1
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - You MUST implement each calculation in its own function (see scaffold).
# - You may NOT use Python's built-in sum(), max(), or min() functions.
#   Implement the logic yourself using loops inside each function.
# - N must be a positive integer. If the user enters 0 or a negative
#   number, print an error message and stop.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def get_sum(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total


def get_average(numbers):
    total = get_sum(numbers)
    average = total / len(numbers)
    return average


def get_max(numbers):
    biggest = numbers[0]
    for n in numbers:
        if n > biggest:
            biggest = n
    return biggest


def get_min(numbers):
    smallest = numbers[0]
    for n in numbers:
        if n < smallest:
            smallest = n
    return smallest


# main part of the program
how_many = int(input("How many numbers? "))

if how_many <= 0:
    print("Error: You must enter a positive number.")
else:
    numbers = []

    for i in range(how_many):
        num = int(input("Enter number " + str(i + 1) + ": "))
        numbers.append(num)

    total = get_sum(numbers)
    average = get_average(numbers)
    biggest = get_max(numbers)
    smallest = get_min(numbers)

    print()
    print("Results:")
    print("Sum:    ", total)
    print("Average:", average)
    print("Maximum:", biggest)
    print("Minimum:", smallest)