# ============================================================
# FILE: test_cases.py
# PURPOSE: Test fundamental algorithms and calculations
# ============================================================

from algorithms import (
    calculate_sum,
    calculate_average,
    find_max,
    find_min,
    remove_duplicates,
    linear_search
)

from analysis import get_grade


# ------------------------------------------------------------
# TEST 1: SUM
# ------------------------------------------------------------

def test_sum():

    numbers = [10, 20, 30, 40]

    result = calculate_sum(numbers)

    assert result == 100

    print("✓ Test 1 Passed: Summation")


# ------------------------------------------------------------
# TEST 2: AVERAGE
# ------------------------------------------------------------

def test_average():

    numbers = [10, 20, 30]

    result = calculate_average(numbers)

    assert result == 20

    print("✓ Test 2 Passed: Average")


# ------------------------------------------------------------
# TEST 3: MAXIMUM
# ------------------------------------------------------------

def test_max():

    numbers = [10, 80, 30, 50]

    result = find_max(numbers)

    assert result == 80

    print("✓ Test 3 Passed: Maximum")


# ------------------------------------------------------------
# TEST 4: MINIMUM
# ------------------------------------------------------------

def test_min():

    numbers = [10, 80, 30, 50]

    result = find_min(numbers)

    assert result == 10

    print("✓ Test 4 Passed: Minimum")


# ------------------------------------------------------------
# TEST 5: DUPLICATE REMOVAL
# ------------------------------------------------------------

def test_duplicate_removal():

    numbers = [1, 2, 2, 3, 3, 4]

    result = remove_duplicates(numbers)

    assert set(result) == {1, 2, 3, 4}

    print("✓ Test 5 Passed: Duplicate Removal")


# ------------------------------------------------------------
# TEST 6: GRADE CALCULATION
# ------------------------------------------------------------

def test_grade():

    assert get_grade(95) == "A+"
    assert get_grade(85) == "A"
    assert get_grade(75) == "B"
    assert get_grade(65) == "C"
    assert get_grade(55) == "D"
    assert get_grade(35) == "F"

    print("✓ Test 6 Passed: Grade Calculation")


# ------------------------------------------------------------
# TEST 7: LINEAR SEARCH
# ------------------------------------------------------------

def test_linear_search():

    students = [
        {"id": 101, "name": "Aarav"},
        {"id": 102, "name": "Riya"}
    ]

    result = linear_search(
        students,
        102
    )

    assert result["name"] == "Riya"

    print("✓ Test 7 Passed: Linear Search")


# ------------------------------------------------------------
# RUN ALL TESTS
# ------------------------------------------------------------

def run_tests():

    print("\n")
    print("=" * 55)
    print("             PROGRAM VERIFICATION")
    print("=" * 55)

    test_sum()
    test_average()
    test_max()
    test_min()
    test_duplicate_removal()
    test_grade()
    test_linear_search()

    print("=" * 55)
    print("       ALL TESTS PASSED SUCCESSFULLY!")
    print("=" * 55)


# ------------------------------------------------------------
# START TESTING
# ------------------------------------------------------------

if __name__ == "__main__":

    run_tests()