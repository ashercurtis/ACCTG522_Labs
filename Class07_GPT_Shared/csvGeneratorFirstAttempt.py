import random
import pandas as pd

# List of sample first and last names
first_names = ['John', 'Jane', 'Emily', 'Michael', 'Sarah', 'David', 'Laura', 'Robert', 'Jessica', 'Daniel']
last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Martinez', 'Wilson']

# List of departments
departments = ['Finance', 'HR', 'Engineering', 'Marketing', 'Sales', 'Customer Support']

# Function to generate a random employee ID
def generate_employee_id():
    return f"EMP{random.randint(1000, 9999)}"

# Function to generate a random salary between a specified range
def generate_salary():
    return round(random.uniform(50000, 120000), 2)

# Function to generate random employee data
def generate_employee_data(num_employees=100):
    employees = []
    for _ in range(num_employees):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        full_name = f"{first_name} {last_name}"
        employee_id = generate_employee_id()
        department = random.choice(departments)
        salary = generate_salary()
        
        # Append employee data to the list
        employees.append({
            'Employee ID': employee_id,
            'Name': full_name,
            'Department': department,
            'Salary': salary
        })
    
    return employees

# Number of employees to generate
num_employees = 100

# Generate the employee data
employee_data = generate_employee_data(num_employees)

# Create a pandas DataFrame
df = pd.DataFrame(employee_data)

# Output the data to a CSV file
output_file = 'employee_data.csv'
df.to_csv(output_file, index=False)

print(f"Employee data for {num_employees} employees has been written to {output_file}.")
