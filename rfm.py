from datetime import datetime

DONATIONS = [
    {"Contacts._id": "Harry", "amount": 200, "paidAt": datetime(2020, 1, 1), "status": "Active"},
    {"Contacts._id": "Harry", "amount": 200, "paidAt": datetime(2021, 2, 1), "status": "Active"},
    {"Contacts._id": "Ron", "amount": 200, "paidAt": datetime(2021, 1, 1), "status": "Cancelled"},
    {"Contacts._id": "Hermione", "amount": 200, "paidAt": datetime(2020, 4, 7), "status": "Open"},
    {"Contacts._id": "Hagrid", "amount": 200, "paidAt": datetime(2021, 8, 9), "status": "Active"},
    {"Contacts._id": "Harry", "amount": 200, "paidAt": datetime(2020, 1, 1), "status": "Active"},
    {"Contacts._id": "Hogwarts", "amount": 200, "paidAt": datetime(2018, 2, 1), "status": "Draft"},
    {"Contacts._id": "Hogwarts", "amount": 200, "paidAt": datetime(2029, 6, 1), "status": "Active"},
    {"Contacts._id": "Hogwarts", "amount": 200, "paidAt": datetime(2020, 1, 1), "status": "Cancelled"},
]

CONTACTS = [
    {"_id": "Harry"},
    {"_id": "Hermione"},
    {"_id": "Ron"},
    {"_id": "Neville"},
    {"_id": "Hogwarts"},
    {"_id": "Draco"},
]


def rfm():
    """https://www.optimove.com/resources/learning-center/rfm-segmentation"""
    pass