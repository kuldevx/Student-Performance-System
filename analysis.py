# ============================================================
# FILE: analysis.py
# PURPOSE: Analyze student performance
# ============================================================

from algorithms import (
    calculate_sum,
    calculate_average,
    count_if,
    partition_students
)


# ------------------------------------------------------------
# GET TOTAL MARKS
# ------------------------------------------------------------

def get_total_marks(student):

    marks = list(student["marks"].values())

    return calculate_sum(marks)


# ------------------------------------------------------------
# GET STUDENT AVERAGE
# ------------------------------------------------------------

def get_student_average(student):

    marks = list(student["marks"].values())

    return calculate_average(marks)


# ------------------------------------------------------------
# GET PERCENTAGE
# ------------------------------------------------------------

def get_percentage(student):

    return get_student_average(student)


# ------------------------------------------------------------
# GRADE CALCULATION
# ------------------------------------------------------------

def get_grade(percentage):

    if percentage >= 90:
        return "A+"

    elif percentage >= 80:
        return "A"

    elif percentage >= 70:
        return "B"

    elif percentage >= 60:
        return "C"

    elif percentage >= 50:
        return "D"

    else:
        return "F"


# ------------------------------------------------------------
# PASS / FAIL
# ------------------------------------------------------------

def is_pass(student):

    for mark in student["marks"].values():

        if mark < 40:
            return False

    return True


# ------------------------------------------------------------
# CLASS AVERAGE
# ------------------------------------------------------------

def calculate_class_average(students):

    if len(students) == 0:
        return 0

    averages = []

    for student in students:

        averages.append(
            get_student_average(student)
        )

    return calculate_average(averages)


# ------------------------------------------------------------
# HIGHEST PERFORMER
# ------------------------------------------------------------

def get_highest_performer(students):

    if len(students) == 0:
        return None

    highest = students[0]

    for student in students:

        if (
            get_student_average(student)
            > get_student_average(highest)
        ):
            highest = student

    return highest


# ------------------------------------------------------------
# LOWEST PERFORMER
# ------------------------------------------------------------

def get_lowest_performer(students):

    if len(students) == 0:
        return None

    lowest = students[0]

    for student in students:

        if (
            get_student_average(student)
            < get_student_average(lowest)
        ):
            lowest = student

    return lowest


# ------------------------------------------------------------
# COUNT PASSING STUDENTS
# ------------------------------------------------------------

def count_passing_students(students):

    return count_if(
        students,
        is_pass
    )


# ------------------------------------------------------------
# COUNT FAILING STUDENTS
# ------------------------------------------------------------

def count_failing_students(students):

    return (
        len(students)
        - count_passing_students(students)
    )


# ------------------------------------------------------------
# SUBJECT AVERAGE
# ------------------------------------------------------------

def calculate_subject_average(students, subject):

    if len(students) == 0:
        return 0

    marks = []

    for student in students:

        marks.append(
            student["marks"][subject]
        )

    return calculate_average(marks)


# ------------------------------------------------------------
# PERFORMANCE CATEGORIES
# ------------------------------------------------------------

def categorize_students(students):

    def excellent(student):

        return get_student_average(student) >= 80

    excellent_students, remaining_students = (
        partition_students(
            students,
            excellent
        )
    )

    def needs_improvement(student):

        return get_student_average(student) < 50

    improvement_students, average_students = (
        partition_students(
            remaining_students,
            needs_improvement
        )
    )

    return (
        excellent_students,
        average_students,
        improvement_students
    )


# ------------------------------------------------------------
# COMPLETE CLASS ANALYSIS
# ------------------------------------------------------------

def class_analysis(students):

    print("\n" + "=" * 60)
    print("                 CLASS ANALYSIS")
    print("=" * 60)

    if len(students) == 0:

        print("No student records available.")

        return

    class_average = calculate_class_average(students)

    highest = get_highest_performer(students)

    lowest = get_lowest_performer(students)

    passed = count_passing_students(students)

    failed = count_failing_students(students)

    excellent, average, improvement = (
        categorize_students(students)
    )

    print(
        f"\nTotal Students       : {len(students)}"
    )

    print(
        f"Class Average        : {class_average:.2f}%"
    )

    print(
        "\nHighest Performer    :",
        highest["name"],
        f"({get_student_average(highest):.2f}%)"
    )

    print(
        "Lowest Performer     :",
        lowest["name"],
        f"({get_student_average(lowest):.2f}%)"
    )

    print(
        f"\nPassing Students     : {passed}"
    )

    print(
        f"Failing Students     : {failed}"
    )

    print("\nPerformance Categories")

    print(
        f"Excellent            : {len(excellent)}"
    )

    print(
        f"Average              : {len(average)}"
    )

    print(
        f"Needs Improvement    : {len(improvement)}"
    )

    # --------------------------------------------------------
    # SUBJECT ANALYSIS
    # --------------------------------------------------------

    print("\n" + "-" * 60)
    print("SUBJECT-WISE PERFORMANCE")
    print("-" * 60)

    subjects = [
        "Mathematics",
        "Physics",
        "Computer Science"
    ]

    for subject in subjects:

        average_mark = calculate_subject_average(
            students,
            subject
        )

        print(
            f"{subject:<20}: {average_mark:.2f}%"
        )