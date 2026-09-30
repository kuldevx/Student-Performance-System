# ============================================================
# FILE: sample_data.py
# PURPOSE: Provide fixed sample student records
# ============================================================


def get_sample_students():
    """
    Returns a fixed set of sample student records.
    """

    students = [

        {
            "id": 101,
            "name": "Aarav",
            "marks": {
                "Mathematics": 92,
                "Physics": 88,
                "Computer Science": 95
            },
            "attendance": 94
        },

        {
            "id": 102,
            "name": "Riya",
            "marks": {
                "Mathematics": 85,
                "Physics": 91,
                "Computer Science": 89
            },
            "attendance": 91
        },

        {
            "id": 103,
            "name": "Rahul",
            "marks": {
                "Mathematics": 72,
                "Physics": 68,
                "Computer Science": 75
            },
            "attendance": 82
        },

        {
            "id": 104,
            "name": "Ananya",
            "marks": {
                "Mathematics": 96,
                "Physics": 94,
                "Computer Science": 98
            },
            "attendance": 97
        },

        {
            "id": 105,
            "name": "Arjun",
            "marks": {
                "Mathematics": 45,
                "Physics": 52,
                "Computer Science": 48
            },
            "attendance": 72
        },

        {
            "id": 106,
            "name": "Ishita",
            "marks": {
                "Mathematics": 78,
                "Physics": 82,
                "Computer Science": 80
            },
            "attendance": 88
        },

        {
            "id": 107,
            "name": "Vivaan",
            "marks": {
                "Mathematics": 35,
                "Physics": 42,
                "Computer Science": 38
            },
            "attendance": 65
        },

        {
            "id": 108,
            "name": "Meera",
            "marks": {
                "Mathematics": 88,
                "Physics": 84,
                "Computer Science": 90
            },
            "attendance": 93
        }

    ]

    return students