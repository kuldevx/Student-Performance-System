# ============================================================
# FILE: main.py
# PURPOSE: Main program and menu control
# ============================================================

from data_manager import (
    add_student,
    view_students,
    search_student,
    update_student,
    delete_student
)

from analysis import class_analysis

from reports import (
    individual_report,
    class_report,
    subject_report
)

from sample_data import get_sample_students


# ------------------------------------------------------------
# DISPLAY HEADER
# ------------------------------------------------------------

def display_header():

    print("\n")
    print("=" * 60)
    print("       STUDENT PERFORMANCE ANALYSIS SYSTEM")
    print("=" * 60)
    print("          Python & Fundamental Algorithms")
    print("=" * 60)


# ------------------------------------------------------------
# DISPLAY MENU
# ------------------------------------------------------------

def display_menu():

    print("\n")
    print("┌──────────────────────────────────────────────┐")
    print("│                  MAIN MENU                   │")
    print("├──────────────────────────────────────────────┤")
    print("│  1. Add Student                              │")
    print("│  2. View All Students                        │")
    print("│  3. Search Student                           │")
    print("│  4. Update Student                           │")
    print("│  5. Delete Student                           │")
    print("│  6. Analyze Class Performance                │")
    print("│  7. Generate Individual Report               │")
    print("│  8. Generate Class Report                    │")
    print("│  9. Generate Subject Report                  │")
    print("│ 10. Load Fixed Sample Data                   │")
    print("│ 11. Exit                                     │")
    print("└──────────────────────────────────────────────┘")


# ------------------------------------------------------------
# LOAD SAMPLE DATA
# ------------------------------------------------------------

def load_sample_data(students):

    sample_students = get_sample_students()

    added = 0

    for sample in sample_students:

        already_exists = False

        for student in students:

            if student["id"] == sample["id"]:

                already_exists = True

                break

        if not already_exists:

            students.append(sample)

            added += 1

    if added == 0:

        print("\n⚠️ Sample data is already loaded.")

    else:

        print(
            f"\n✅ {added} sample student(s) loaded successfully!"
        )


# ------------------------------------------------------------
# MAIN FUNCTION
# ------------------------------------------------------------

def main():

    # List containing all student records
    students = []

    display_header()

    print("\nWelcome!")

    print(
        "Use the menu below to manage and analyze student performance."
    )

    while True:

        display_menu()

        choice = input(
            "\nEnter your choice (1-11): "
        ).strip()

        # ----------------------------------------------------
        # OPTION 1
        # ----------------------------------------------------

        if choice == "1":

            add_student(students)

        # ----------------------------------------------------
        # OPTION 2
        # ----------------------------------------------------

        elif choice == "2":

            view_students(students)

        # ----------------------------------------------------
        # OPTION 3
        # ----------------------------------------------------

        elif choice == "3":

            search_student(students)

        # ----------------------------------------------------
        # OPTION 4
        # ----------------------------------------------------

        elif choice == "4":

            update_student(students)

        # ----------------------------------------------------
        # OPTION 5
        # ----------------------------------------------------

        elif choice == "5":

            delete_student(students)

        # ----------------------------------------------------
        # OPTION 6
        # ----------------------------------------------------

        elif choice == "6":

            class_analysis(students)

        # ----------------------------------------------------
        # OPTION 7
        # ----------------------------------------------------

        elif choice == "7":

            individual_report(students)

        # ----------------------------------------------------
        # OPTION 8
        # ----------------------------------------------------

        elif choice == "8":

            class_report(students)

        # ----------------------------------------------------
        # OPTION 9
        # ----------------------------------------------------

        elif choice == "9":

            subject_report(students)

        # ----------------------------------------------------
        # OPTION 10
        # ----------------------------------------------------

        elif choice == "10":

            load_sample_data(students)

        # ----------------------------------------------------
        # OPTION 11
        # ----------------------------------------------------

        elif choice == "11":

            print("\n")
            print("=" * 60)
            print("Thank you for using the Student Performance")
            print("Analysis System!")
            print("=" * 60)
            print("Program terminated successfully.")
            print("=" * 60)

            break

        # ----------------------------------------------------
        # INVALID OPTION
        # ----------------------------------------------------

        else:

            print(
                "\n❌ Invalid choice."
                "\nPlease enter a number from 1 to 11."
            )


# ------------------------------------------------------------
# PROGRAM START
# ------------------------------------------------------------

if __name__ == "__main__":

    main()