# ============================================================
# FILE: reports.py
# PURPOSE: Generate formatted reports
# ============================================================

from algorithms import linear_search

from analysis import (
    get_total_marks,
    get_student_average,
    get_grade,
    is_pass,
    calculate_subject_average
)


# ------------------------------------------------------------
# INDIVIDUAL STUDENT REPORT
# ------------------------------------------------------------

def individual_report(students):

    print("\n" + "=" * 60)
    print("              INDIVIDUAL REPORT")
    print("=" * 60)

    student_id_input = input(
        "Enter Student ID: "
    ).strip()

    if not student_id_input.isdigit():

        print("\n❌ Invalid Student ID.")

        return

    student_id = int(student_id_input)

    student = linear_search(
        students,
        student_id
    )

    if student is None:

        print("\n❌ Student not found.")

        return

    total = get_total_marks(student)

    average = get_student_average(student)

    grade = get_grade(average)

    status = (
        "PASS"
        if is_pass(student)
        else "FAIL"
    )

    print("\n" + "=" * 60)

    print("           STUDENT PERFORMANCE REPORT")

    print("=" * 60)

    print(
        f"Student ID       : {student['id']}"
    )

    print(
        f"Student Name     : {student['name']}"
    )

    print("\nSubject Marks")
    print("-" * 40)

    print(
        f"Mathematics      : "
        f"{student['marks']['Mathematics']:.1f}"
    )

    print(
        f"Physics          : "
        f"{student['marks']['Physics']:.1f}"
    )

    print(
        f"Computer Science : "
        f"{student['marks']['Computer Science']:.1f}"
    )

    print("-" * 40)

    print(
        f"Total Marks      : {total:.1f} / 300"
    )

    print(
        f"Average          : {average:.2f}%"
    )

    print(
        f"Grade            : {grade}"
    )

    print(
        f"Attendance       : {student['attendance']:.1f}%"
    )

    print(
        f"Status           : {status}"
    )

    print("=" * 60)


# ------------------------------------------------------------
# CLASS REPORT
# ------------------------------------------------------------

def class_report(students):

    print("\n" + "=" * 75)
    print("                    CLASS REPORT")
    print("=" * 75)

    if len(students) == 0:

        print("No student records available.")

        return

    print(
        f"{'ID':<8}"
        f"{'Name':<20}"
        f"{'Average':<12}"
        f"{'Grade':<10}"
        f"{'Status':<10}"
    )

    print("-" * 75)

    for student in students:

        average = get_student_average(student)

        grade = get_grade(average)

        status = (
            "PASS"
            if is_pass(student)
            else "FAIL"
        )

        print(
            f"{student['id']:<8}"
            f"{student['name']:<20}"
            f"{average:<12.2f}"
            f"{grade:<10}"
            f"{status:<10}"
        )

    print("=" * 75)


# ------------------------------------------------------------
# SUBJECT REPORT
# ------------------------------------------------------------

def subject_report(students):

    print("\n" + "=" * 60)
    print("                  SUBJECT REPORT")
    print("=" * 60)

    if len(students) == 0:

        print("No student records available.")

        return

    subjects = [
        "Mathematics",
        "Physics",
        "Computer Science"
    ]

    for subject in subjects:

        average = calculate_subject_average(
            students,
            subject
        )

        highest = None
        lowest = None

        for student in students:

            mark = student["marks"][subject]

            if highest is None or mark > highest:
                highest = mark

            if lowest is None or mark < lowest:
                lowest = mark

        print("\n" + "-" * 45)

        print(
            f"Subject : {subject}"
        )

        print(
            f"Average : {average:.2f}%"
        )

        print(
            f"Highest : {highest:.2f}"
        )

        print(
            f"Lowest  : {lowest:.2f}"
        )

    print("\n" + "=" * 60)