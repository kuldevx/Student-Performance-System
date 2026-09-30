# ============================================================
# FILE: algorithms.py
# PURPOSE: Implement fundamental algorithms
# ============================================================


# ------------------------------------------------------------
# SUMMATION ALGORITHM
# ------------------------------------------------------------

def calculate_sum(numbers):
    """
    Calculates the sum of numbers without using Python's
    built-in sum() function.
    """

    total = 0

    for number in numbers:
        total = total + number

    return total


# ------------------------------------------------------------
# AVERAGE ALGORITHM
# ------------------------------------------------------------

def calculate_average(numbers):
    """
    Calculates average using the summation algorithm.
    """

    if len(numbers) == 0:
        return 0

    total = calculate_sum(numbers)

    return total / len(numbers)


# ------------------------------------------------------------
# MAXIMUM NUMBER ALGORITHM
# ------------------------------------------------------------

def find_max(numbers):
    """
    Finds the largest number without using max().
    """

    if len(numbers) == 0:
        return None

    maximum = numbers[0]

    for number in numbers:

        if number > maximum:
            maximum = number

    return maximum


# ------------------------------------------------------------
# MINIMUM NUMBER ALGORITHM
# ------------------------------------------------------------

def find_min(numbers):
    """
    Finds the smallest number without using min().
    """

    if len(numbers) == 0:
        return None

    minimum = numbers[0]

    for number in numbers:

        if number < minimum:
            minimum = number

    return minimum


# ------------------------------------------------------------
# COUNTING ALGORITHM
# ------------------------------------------------------------

def count_if(items, condition):
    """
    Counts the number of items satisfying a condition.
    """

    count = 0

    for item in items:

        if condition(item):
            count = count + 1

    return count


# ------------------------------------------------------------
# LINEAR SEARCH ALGORITHM
# ------------------------------------------------------------

def linear_search(students, student_id):
    """
    Searches for a student using Linear Search.
    """

    for student in students:

        if student["id"] == student_id:
            return student

    return None


# ------------------------------------------------------------
# DUPLICATE REMOVAL
# ------------------------------------------------------------

def remove_duplicates(numbers):
    """
    Removes duplicate values using a set.
    """

    unique_numbers = set()

    for number in numbers:
        unique_numbers.add(number)

    return list(unique_numbers)


# ------------------------------------------------------------
# PARTITIONING ALGORITHM
# ------------------------------------------------------------

def partition_students(students, condition):
    """
    Divides students into two groups based on a condition.
    """

    group_one = []
    group_two = []

    for student in students:

        if condition(student):
            group_one.append(student)

        else:
            group_two.append(student)

    return group_one, group_two