import random
import csv
from datetime import datetime, timedelta

# Lists to draw random values from
first_names = ["John", "Jane", "Alex", "Emily", "Michael", "Sara", "Chris", "Laura", "David", "Anna", "NA"]
last_names = ["Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Taylor", "Clark", "NA"]
middle_initials = ["A", "B", "C", "D", "E", "F", "G", "H", "NA"]
genders = ["Male", "Female", "Other"]
job_titles = ["Software Engineer", "Data Scientist", "Accountant", "Manager", "Sales Representative", "HR Specialist"]
departments = ["IT", "Finance", "HR", "Sales", "Operations", "Marketing"]
salary_range = (40000, 120000)  # Base annual salary range

# Function to generate a random hire date
def random_hire_date():
    start_date = datetime(1951, 6, 23)
    end_date = datetime(2023, 12, 31)
    return (start_date + timedelta(days=random.randint(0, (end_date - start_date).days))).strftime('%d/%m/%Y')

# Function to generate a termination date or null if not terminated
def random_termination_date(hire_date):
    if random.choice([True, False]):
        hire_date_dt = datetime.strptime(hire_date, '%d/%m/%Y')
        termination_date = hire_date_dt + timedelta(days=random.randint(30, (datetime.now() - hire_date_dt).days))
        return termination_date.strftime('%d/%m/%Y')
    return None

# Generate data for 140 employees (110 active, 30 terminated)
employees = []
unique_id = 1
for i in range(140):
    # Determine if the employee is terminated or not
    is_terminated = i >= 110
    
    # Generate employee data
    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    middle_initial = random.choice(middle_initials)
    gender = random.choice(genders)
    job_title = random.choice(job_titles)
    department = random.choice(departments)
    hire_date = random_hire_date()
    
    # If the employee is terminated, assign a termination date; otherwise, leave it null
    termination_date = random_termination_date(hire_date) if is_terminated else None
    
    # Generate random salary
    annual_salary = random.randint(*salary_range)
    
    # Add employee data to the list
    employees.append({
        "UniqueID": unique_id,
        "LastName": last_name,
        "MiddleInitial": middle_initial,
        "FirstName": first_name,
        "Gender": gender,
        "JobTitle": job_title,
        "Department": department,
        "HireDate": hire_date,
        "TerminationDate": termination_date,
        "AnnualSalary": annual_salary
    })
    
    unique_id += 1

# Write the employee data to a CSV file
with open('prompt3.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=["UniqueID", "LastName", "MiddleInitial", "FirstName", "Gender", "JobTitle", "Department", "HireDate", "TerminationDate", "AnnualSalary"])
    writer.writeheader()
    writer.writerows(employees)

print("Employee data has been generated and saved to prompt3.csv.")
