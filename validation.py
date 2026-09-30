# ============================================================
# FILE: validation.py
# PURPOSE: Handle and validate user input
# ============================================================


def validate_student_id(student_id):
    """
    Checks whether Student ID is a positive integer.
    """
    return student_id.isdigit() and int(student_id) > 0


def validate_name(name):
    """
    Checks whether the name contains only alphabets and spaces.
    """
    cleaned_name = name.replace(" ", "")

    return (
        len(name.strip()) > 0
        and cleaned_name.isalpha()
    )


def validate_marks(marks):
    """
    Checks whether marks are between 0 and 100.
    """
    try:
        marks = float(marks)
        return 0 <= marks <= 100

    except ValueError:
        return False


def validate_attendance(attendance):
    """
    Checks whether attendance is between 0 and 100.
    """
    try:
        attendance = float(attendance)
        return 0 <= attendance <= 100

    except ValueError:
        return False


def get_valid_student_id():
    """
    Keeps asking until a valid Student ID is entered.
    """

    while True:

        student_id = input("Enter Student ID: ").strip()

        if validate_student_id(student_id):
            return int(student_id)

        print("❌ Invalid ID. Enter a positive integer.")


def get_valid_name():
    """
    Keeps asking until a valid name is entered.
    """

    while True:

        name = input("Enter Student Name: ").strip()

        if validate_name(name):
            return name.title()

        print("❌ Invalid name. Use alphabets and spaces only.")


def get_valid_marks(subject):
    """
    Keeps asking until valid marks are entered.
    """

    while True:

        marks = input(
            f"Enter {subject} Marks (0-100): "
        ).strip()

        if validate_marks(marks):
            return float(marks)

        print("❌ Invalid marks. Enter a value between 0 and 100.")


def get_valid_attendance():
    """
    Keeps asking until valid attendance is entered.
    """

    while True:

        attendance = input(
            "Enter Attendance Percentage (0-100): "
        ).strip()

        if validate_attendance(attendance):
            return float(attendance)

        print("❌ Invalid attendance. Enter a value between 0 and 100.")