import pandas as pd
import random
from datetime import datetime, timedelta
import os

def setup():
    if not os.path.exists('data'): os.makedirs('data')
    
    # 1. Generate 4,800 Donors
    blood_groups = ['O+', 'O-', 'A+', 'A-', 'B+', 'B-', 'AB+', 'AB-']
    donors = []
    for i in range(4800):
        days_ago = random.randint(10, 180)
        last_date = (datetime.now() - timedelta(days=days_ago)).strftime('%Y-%m-%d')
        donors.append([f"D{i}", f"Donor_{i}", random.choice(blood_groups), last_date, f"91{random.randint(7000000000, 9999999999)}"])
    pd.DataFrame(donors, columns=['DonorID', 'Name', 'BloodGroup', 'LastDonationDate', 'Phone']).to_csv('data/donors.csv', index=False)

    # 2. Generate 400 Patients
    patients = [[f"P{i}", f"Patient_{i}", random.choice(blood_groups), "2", (datetime.now() + timedelta(days=random.randint(1,15))).strftime('%Y-%m-%d')] for i in range(400)]
    pd.DataFrame(patients, columns=['PatientID', 'Name', 'BloodGroup', 'UnitsRequired', 'NextVisit']).to_csv('data/patients.csv', index=False)

    # 3. Initial Inventory
    inv = [[bg, random.randint(5, 25), 15] for bg in blood_groups]
    pd.DataFrame(inv, columns=['BloodGroup', 'Units_In_Stock', 'Min_Required']).to_csv('data/inventory.csv', index=False)
    print("System files initialized successfully!")

if __name__ == "__main__": setup()
