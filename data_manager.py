# ============================================================
# FILE: data_manager.py
# PURPOSE: Manage student records
# ============================================================

from validation import (
    get_valid_student_id,
    get_valid_name,
    get_valid_marks,
    get_valid_attendance
)

from algorithms import linear_search


# ------------------------------------------------------------
# ADD STUDENT
# ------------------------------------------------------------

def add_student(students):

    print("\n" + "=" * 55)
    print("                 ADD STUDENT")
    print("=" * 55)

    student_id = get_valid_student_id()

    # Check duplicate ID
    if linear_search(students, student_id) is not None:

        print("\n❌ Student ID already exists.")

        return

    name = get_valid_name()

    mathematics = get_valid_marks("Mathematics")
    physics = get_valid_marks("Physics")
    computer_science = get_valid_marks("Computer Science")

    attendance = get_valid_attendance()

    student = {
        "id": student_id,
        "name": name,

        "marks": {
            "Mathematics": mathematics,
            "Physics": physics,
            "Computer Science": computer_science
        },

        "attendance": attendance
    }

    students.append(student)

    print("\n✅ Student added successfully!")


# ------------------------------------------------------------
# VIEW ALL STUDENTS
# ------------------------------------------------------------

def view_students(students):

    print("\n" + "=" * 70)
    print("                    ALL STUDENTS")
    print("=" * 70)

    if len(students) == 0:

        print("No student records available.")

        return

    print(
        f"{'ID':<8}"
        f"{'Name':<20}"
        f"{'Maths':<10}"
        f"{'Physics':<10}"
        f"{'Computer':<12}"
        f"{'Attendance':<12}"
    )

    print("-" * 70)

    for student in students:

        print(
            f"{student['id']:<8}"
            f"{student['name']:<20}"
            f"{student['marks']['Mathematics']:<10.1f}"
            f"{student['marks']['Physics']:<10.1f}"
            f"{student['marks']['Computer Science']:<12.1f}"
            f"{student['attendance']:<12.1f}"
        )


# ------------------------------------------------------------
# SEARCH STUDENT
# ------------------------------------------------------------

def search_student(students):

    print("\n" + "=" * 55)
    print("                 SEARCH STUDENT")
    print("=" * 55)

    student_id = get_valid_student_id()

    student = linear_search(students, student_id)

    if student is None:

        print("\n❌ Student not found.")

    else:

        print_student(student)


# ------------------------------------------------------------
# DISPLAY ONE STUDENT
# ------------------------------------------------------------

def print_student(student):

    print("\n" + "-" * 45)

    print("Student ID :", student["id"])
    print("Name       :", student["name"])

    print("\nMarks:")

    print(
        "Mathematics     :",
        student["marks"]["Mathematics"]
    )

    print(
        "Physics         :",
        student["marks"]["Physics"]
    )

    print(
        "Computer Science:",
        student["marks"]["Computer Science"]
    )

    print(
        "\nAttendance      :",
        student["attendance"],
        "%"
    )

    print("-" * 45)


# ------------------------------------------------------------
# UPDATE STUDENT
# ------------------------------------------------------------

def update_student(students):

    print("\n" + "=" * 55)
    print("                 UPDATE STUDENT")
    print("=" * 55)

    student_id = get_valid_student_id()

    student = linear_search(students, student_id)

    if student is None:

        print("\n❌ Student not found.")

        return

    print("\nUpdating record for:", student["name"])

    student["name"] = get_valid_name()

    student["marks"]["Mathematics"] = get_valid_marks(
        "Mathematics"
    )

    student["marks"]["Physics"] = get_valid_marks(
        "Physics"
    )

    student["marks"]["Computer Science"] = get_valid_marks(
        "Computer Science"
    )

    student["attendance"] = get_valid_attendance()

    print("\n✅ Student record updated successfully!")


# ------------------------------------------------------------
# DELETE STUDENT
# ------------------------------------------------------------

def delete_student(students):

    print("\n" + "=" * 55)
    print("                 DELETE STUDENT")
    print("=" * 55)

    student_id = get_valid_student_id()

    student = linear_search(students, student_id)

    if student is None:

        print("\n❌ Student not found.")

        return

    print("\nStudent found:", student["name"])

    confirmation = input(
        "Are you sure you want to delete this record? (y/n): "
    ).strip().lower()

    if confirmation == "y":

        students.remove(student)

        print("\n✅ Student deleted successfully!")

    else:

        print("\nDeletion cancelled.")