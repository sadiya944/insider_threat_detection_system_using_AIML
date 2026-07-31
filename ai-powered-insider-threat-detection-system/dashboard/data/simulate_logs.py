import os
import random #Used to generate random values.
import pandas as pd
from datetime import datetime, timedelta #Used for generating dates and times.

os.makedirs('data', exist_ok=True) #This creates a folder named and If the folder already exists,
#prevents Python from throwing an error.Without this line,saving CSV files would fail if the folder didn't exist.
                                
USERS = [f'user{i}' for i in range(1, 21)] #This is called List Comprehension.Python automatically generates 20 employees
FILES = [f'file_{i}.docx' for i in range(1, 51)]#Total 50 documents These represent company files employees may access.
DEVICES = [f'usb_{i}' for i in range(1, 6)] #5 usbs are created similarly
EMAILS = [f'user{i}@company.com' for i in range(1, 21)]#email accounts are generated

START_DATE = datetime(2023, 1, 1)#in these lines the datefrom when data must be simulated is given
DAYS = 30#here the no. of days for which data is generated

random.seed(42)#in same sequence the randomn numbers are generated

def simulate_logins():#Creates employee login records.
    records = []
    for day in range(DAYS):
        date = START_DATE + timedelta(days=day)
        for user in USERS:
            login_time = date + timedelta(hours=random.randint(6, 10), minutes=random.randint(0, 59))
            logout_time = login_time + timedelta(hours=random.randint(6, 10))
            records.append({'user': user, 'login': login_time, 'logout': logout_time})
    pd.DataFrame(records).to_csv('data/logins.csv', index=False)

def simulate_file_access():# Generates records of employees opening files.
    records = []
    for day in range(DAYS):
        date = START_DATE + timedelta(days=day)
        for _ in range(random.randint(50, 100)):
            user = random.choice(USERS)
            file = random.choice(FILES)
            access_time = date + timedelta(hours=random.randint(0, 23), minutes=random.randint(0, 59))
            records.append({'user': user, 'file': file, 'access_time': access_time})
    pd.DataFrame(records).to_csv('data/file_access.csv', index=False)

def simulate_usb_usage():# Creates USB insertion logs. 
    records = []
    for day in range(DAYS):
        date = START_DATE + timedelta(days=day)
        for _ in range(random.randint(2, 8)):
            user = random.choice(USERS)
            device = random.choice(DEVICES)
            plug_time = date + timedelta(hours=random.randint(8, 18), minutes=random.randint(0, 59))
            unplug_time = plug_time + timedelta(minutes=random.randint(5, 120))
            records.append({'user': user, 'device': device, 'plug_time': plug_time, 'unplug_time': unplug_time})
    pd.DataFrame(records).to_csv('data/usb_usage.csv', index=False)

def simulate_emails():#Generates company email communication.
    records = []
    for day in range(DAYS):
        date = START_DATE + timedelta(days=day)
        for _ in range(random.randint(30, 60)):
            sender = random.choice(EMAILS)
            recipient = random.choice([e for e in EMAILS if e != sender])
            time = date + timedelta(hours=random.randint(7, 19), minutes=random.randint(0, 59))
            subject = random.choice(['Project Update', 'Meeting', 'Invoice', 'Confidential', 'Request'])
            records.append({'sender': sender, 'recipient': recipient, 'time': time, 'subject': subject})
    pd.DataFrame(records).to_csv('data/emails.csv', index=False)
#This checks whether the file is being run directly.If yes all four datasets are generated.
if __name__ == '__main__':
    simulate_logins()
    simulate_file_access()
    simulate_usb_usage()
    simulate_emails()
    print('Simulated logs generated in data/.') 