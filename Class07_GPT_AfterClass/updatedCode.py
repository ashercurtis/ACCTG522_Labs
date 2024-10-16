import random
import csv
from datetime import datetime, timedelta

# Lists to draw random values from
brazilian_names = {
    "Adriana": "Female",
    "Afonso": "Male",
    "Alexandre": "Male",
    "Alessandra": "Female",
    "Ana": "Female",
    "Anderson": "Male",
    "Antonio": "Male",
    "Beatriz": "Female",
    "Bernardo": "Male",
    "Bruna": "Female",
    "Bruno": "Male",
    "Camila": "Female",
    "Carlos": "Male",
    "Carla": "Female",
    "Cecília": "Female",
    "Celso": "Male",
    "Cláudia": "Female",
    "Cláudio": "Male",
    "Daniela": "Female",
    "Daniel": "Male",
    "Débora": "Female",
    "Diogo": "Male",
    "Eduardo": "Male",
    "Eliana": "Female",
    "Elis": "Female",
    "Elisa": "Female",
    "Enzo": "Male",
    "Estela": "Female",
    "Fabiana": "Female",
    "Fábio": "Male",
    "Felipe": "Male",
    "Fernanda": "Female",
    "Fernando": "Male",
    "Gabriela": "Female",
    "Gabriel": "Male",
    "Guilherme": "Male",
    "Gustavo": "Male",
    "Heitor": "Male",
    "Helena": "Female",
    "Henrique": "Male",
    "Hugo": "Male",
    "Inês": "Female",
    "Isabel": "Female",
    "Isabela": "Female",
    "João": "Male",
    "José": "Male",
    "Júlia": "Female",
    "Juliano": "Male",
    "Juliana": "Female",
    "Leonardo": "Male",
    "Letícia": "Female",
    "Lucas": "Male",
    "Luana": "Female",
    "Luciana": "Female",
    "Luciano": "Male",
    "Luís": "Male",
    "Manuela": "Female",
    "Marcelo": "Male",
    "Marcos": "Male",
    "Maria": "Female",
    "Mariana": "Female",
    "Mateus": "Male",
    "Matheus": "Male",
    "Maurício": "Male",
    "Mauro": "Male",
    "Miguel": "Male",
    "Mônica": "Female",
    "Nadia": "Female",
    "Nicolas": "Male",
    "Olívia": "Female",
    "Otávio": "Male",
    "Patrícia": "Female",
    "Paulo": "Male",
    "Pedro": "Male",
    "Rafael": "Male",
    "Rafaela": "Female",
    "Raquel": "Female",
    "Renan": "Male",
    "Renata": "Female",
    "Ricardo": "Male",
    "Rodrigo": "Male",
    "Rogério": "Male",
    "Sandra": "Female",
    "Sara": "Female",
    "Silvia": "Female",
    "Simone": "Female",
    "Sophia": "Female",
    "Stefano": "Male",
    "Sérgio": "Male",
    "Tânia": "Female",
    "Thiago": "Male",
    "Tomás": "Male",
    "Valéria": "Female",
    "Vanessa": "Female",
    "Vera": "Female",
    "Vicente": "Male",
    "Vinícius": "Male",
    "Vítor": "Male",
    "Vitória": "Female",
    "Yara": "Female",
    "Yasmin": "Female",
}

brazilian_last_names = [
    "Silva",
    "Santos",
    "Oliveira",
    "Souza",
    "Pereira",
    "Costa",
    "Almeida",
    "Ferreira",
    "Gomes",
    "Martins",
    "Rodrigues",
    "Lima",
    "Barbosa",
    "Melo",
    "Carvalho",
    "Ribeiro",
    "Fernandes",
    "Araujo",
    "Moreira",
    "Castro",
    "Correia",
    "Nogueira",
    "Machado",
    "Teixeira",
    "Cardoso",
    "Pinto",
    "Monteiro",
    "Vieira",
    "Moura",
    "Dias",
    "Andrade",
    "Miranda",
    "Moraes",
    "Campos",
    "Freitas",
    "Rezende",
    "Vasconcelos",
    "Queiroz",
    "Batista",
    "Farias",
    "Guimarães",
    "Barros",
    "Assis",
    "Peixoto",
    "Lopes",
    "Braga",
    "Tavares",
    "Xavier",
    "Figueiredo",
    "Macedo",
    "Camargo",
    "Borges",
    "Coelho",
    "Lacerda",
    "Duarte",
    "Leal",
    "Pacheco",
    "Salvador",
    "Fonseca",
    "Ramos",
    "Cavalcanti",
    "Quevedo",
    "Severino",
    "Torres",
    "Cunha",
    "Amaral",
    "Dantas",
    "Antunes",
    "Siqueira",
    "Meireles",
    "Parreira",
    "Bittencourt",
    "Sabino",
    "Aguiar",
    "Porto",
    "Pires",
    "Rezende",
    "Vidal",
    "Valente",
    "Neves",
    "Montenegro",
    "Brandão",
    "Simões",
    "Arruda",
    "Furtado",
    "Padilha",
    "Bastos",
    "Goulart",
    "Rangel",
    "Bueno",
    "Viana",
    "Azevedo",
    "Sá",
    "Serra",
    "Guerreiro",
    "Franco",
    "Amado",
    "Leite",
    "Mendes",
    "Castilho",
]

pure_oils_roles = {
    "Founder": {
        "Department": "Executive Team",
        "Number_of_Employees": 1,
        "Salary_Range": (150000, 200000)  # Founder typically has a higher salary range
    },
    "Chief Scientist": {
        "Department": "Research and Development",
        "Number_of_Employees": 1,
        "Salary_Range": (120000, 150000)
    },
    "Biochemist": {
        "Department": "Research and Development",
        "Number_of_Employees": 3,
        "Salary_Range": (80000, 100000)
    },
    "Botanist": {
        "Department": "Research and Development",
        "Number_of_Employees": 2,
        "Salary_Range": (70000, 90000)
    },
    "R&D Technician": {
        "Department": "Research and Development",
        "Number_of_Employees": 4,
        "Salary_Range": (50000, 70000)
    },
    "Supply Chain Manager": {
        "Department": "Operations",
        "Number_of_Employees": 1,
        "Salary_Range": (90000, 110000)
    },
    "Production Manager": {
        "Department": "Operations",
        "Number_of_Employees": 2,
        "Salary_Range": (80000, 100000)
    },
    "Quality Control Specialist": {
        "Department": "Operations",
        "Number_of_Employees": 4,
        "Salary_Range": (60000, 80000)
    },
    "Field Operations Manager": {
        "Department": "Operations",
        "Number_of_Employees": 3,
        "Salary_Range": (70000, 90000)
    },
    "Sustainable Harvesting Specialist": {
        "Department": "Field Operations",
        "Number_of_Employees": 300,  # All the temporary employees
        "Salary_Range": (30000, 45000)
    },
        "Senior Sustainable Harvesting Specialist": {
        "Department": "Field Operations",
        "Number_of_Employees": 100,  # Bulk of the employees
        "Salary_Range": (30000, 45000)
    },
    "Sustainability Officer": {
        "Department": "Environmental and Sustainability",
        "Number_of_Employees": 2,
        "Salary_Range": (80000, 100000)
    },
    "Sales Manager": {
        "Department": "Sales and Marketing",
        "Number_of_Employees": 1,
        "Salary_Range": (90000, 110000)
    },
    "Marketing Director": {
        "Department": "Sales and Marketing",
        "Number_of_Employees": 1,
        "Salary_Range": (90000, 110000)
    },
    "Brand Ambassador": {
        "Department": "Sales and Marketing",
        "Number_of_Employees": 5,
        "Salary_Range": (50000, 70000)
    },
    "Content Creator": {
        "Department": "Sales and Marketing",
        "Number_of_Employees": 4,
        "Salary_Range": (50000, 70000)
    },
    "Chief Financial Officer (CFO)": {
        "Department": "Finance",
        "Number_of_Employees": 1,
        "Salary_Range": (120000, 150000)
    },
    "Operations Manager": {
        "Department": "Operations",
        "Number_of_Employees": 1,
        "Salary_Range": (100000, 120000)
    },
    "Human Resources Manager": {
        "Department": "Human Resources",
        "Number_of_Employees": 1,
        "Salary_Range": (70000, 90000)
    },
    "Regulatory Compliance Officer": {
        "Department": "Legal and Compliance",
        "Number_of_Employees": 1,
        "Salary_Range": (90000, 110000)
    },
    "Intellectual Property Lawyer": {
        "Department": "Legal and Compliance",
        "Number_of_Employees": 1,
        "Salary_Range": (110000, 130000)
    }
}

brazil_holidays = [
    # 2021 Holidays
    "01/01/2021",  # New Year's Day (Ano Novo)
    "15/02/2021",  # Carnival Monday (Carnaval)
    "16/02/2021",  # Carnival Tuesday (Carnaval)
    "02/04/2021",  # Good Friday (Sexta-feira Santa)
    "21/04/2021",  # Tiradentes' Day (Dia de Tiradentes)
    "01/05/2021",  # Labor Day (Dia do Trabalhador)
    "03/06/2021",  # Corpus Christi (Corpus Christi)
    "07/09/2021",  # Independence Day (Dia da Independência)
    "12/10/2021",  # Our Lady of Aparecida (Dia de Nossa Senhora Aparecida)
    "02/11/2021",  # All Souls' Day (Dia de Finados)
    "15/11/2021",  # Republic Day (Proclamação da República)
    "25/12/2021",  # Christmas (Natal)

    # 2022 Holidays
    "01/01/2022",  # New Year's Day (Ano Novo)
    "28/02/2022",  # Carnival Monday (Carnaval)
    "01/03/2022",  # Carnival Tuesday (Carnaval)
    "15/04/2022",  # Good Friday (Sexta-feira Santa)
    "21/04/2022",  # Tiradentes' Day (Dia de Tiradentes)
    "01/05/2022",  # Labor Day (Dia do Trabalhador)
    "16/06/2022",  # Corpus Christi (Corpus Christi)
    "07/09/2022",  # Independence Day (Dia da Independência)
    "12/10/2022",  # Our Lady of Aparecida (Dia de Nossa Senhora Aparecida)
    "02/11/2022",  # All Souls' Day (Dia de Finados)
    "15/11/2022",  # Republic Day (Proclamação da República)
    "25/12/2022",  # Christmas (Natal)

    # 2023 Holidays
    "01/01/2023",  # New Year's Day (Ano Novo)
    "20/02/2023",  # Carnival Monday (Carnaval)
    "21/02/2023",  # Carnival Tuesday (Carnaval)
    "07/04/2023",  # Good Friday (Sexta-feira Santa)
    "21/04/2023",  # Tiradentes' Day (Dia de Tiradentes)
    "01/05/2023",  # Labor Day (Dia do Trabalhador)
    "08/06/2023",  # Corpus Christi (Corpus Christi)
    "07/09/2023",  # Independence Day (Dia da Independência)
    "12/10/2023",  # Our Lady of Aparecida (Dia de Nossa Senhora Aparecida)
    "02/11/2023",  # All Souls' Day (Dia de Finados)
    "15/11/2023",  # Republic Day (Proclamação da República)
    "25/12/2023",  # Christmas (Natal)
]

rainy_season = ("April", "July") #Increased hiring of temporary workers around this time

start_up_hires = {
    ("2023-01-23", "2023-01-23"): {
        "Roles": ["Founder", "Human Resources Manager", "Chief Scientist"],
        "Description": "Key initial hires to set up the company, begin recruitment, and establish scientific foundations."
    },
    ("2023-02-01", "2023-02-07"): {
        "Roles": ["Operations Manager"],
        "Description": "Operations Manager hired to oversee day-to-day operations and begin preparing the company for large-scale production."
    },
    ("2023-02-15", "2023-03-01"): {
        "Roles": ["Supply Chain Manager"],
        "Description": "Ensures logistics are in place for transporting leaves from rain forests to production facilities."
    },
    ("2023-03-01", "2023-03-31"): {
        "Roles": ["Field Operations Manager", "Production Manager", "Quality Control Specialist"],
        "Description": "Field and production leadership roles are filled to prepare for large-scale harvesting and processing of leaves during the rainy season."
    },
    ("2023-03-20", "2023-04-01"): {
        "Roles": ["Sustainable Harvesting Specialist"],
        "Description": "Large-scale hiring of harvesters to gather leaves during the rainy season in April."
    }
}

# Helper function to check if a date falls on a holiday or weekend
def is_holiday_or_weekend(date):
    weekday = date.weekday()  # Monday is 0, Sunday is 6
    date_str = date.strftime('%d/%m/%Y')
    return date_str in brazil_holidays or weekday in (5, 6)  # 5 = Saturday, 6 = Sunday

# Function to generate a sequential employee ID
def generate_employee_id(current_id):
    num = int(current_id.split('-')[1]) + 1
    return f"PO-{num:06d}"

# Function to generate a random hire date within a date range
def generate_hire_date(start_range, end_range, last_hire_date):
    start_date = datetime.strptime(start_range, "%Y-%m-%d")
    end_date = datetime.strptime(end_range, "%Y-%m-%d")
    hire_date = start_date
    
    while hire_date <= end_date:
        hire_date += timedelta(days=random.randint(0, (end_date - hire_date).days))
        if not is_holiday_or_weekend(hire_date):
            break
    
    return hire_date.strftime('%d/%m/%Y')

# Main function to generate employee data based on the startup hiring phases
def generate_startup_employees(start_up_hires, start_hire_date, initial_employee_id):
    employees = []
    current_id = initial_employee_id
    
    for date_range, phase in start_up_hires.items():
        start_range, end_range = date_range
        roles = phase["Roles"]
        
        # For each role in the phase, generate employees
        for role in roles:
            # Number of employees to hire for the role
            num_employees = pure_oils_roles[role]["Number_of_Employees"]
            for _ in range(num_employees):
                # Generate hire date
                hire_date = generate_hire_date(start_range, end_range, start_hire_date)
                
                # Generate random first and last names
                first_name, gender = random.choice(list(brazilian_names.items()))
                last_name = random.choice(brazilian_last_names)
                middle_name = random.choice(brazilian_last_names)
                middle_initial = middle_name[0].upper()  # First letter of a second last name
                
                # Determine the department and salary
                department = pure_oils_roles[role]["Department"]
                salary_range = pure_oils_roles[role]["Salary_Range"]
                salary = random.randint(*salary_range)
                
                # Create the employee record
                employee = {
                    "UniqueID": current_id,
                    "FirstName": first_name,
                    "MiddleInitial": middle_initial,
                    "LastName": last_name,
                    "Gender": gender,
                    "JobTitle": role,
                    "Department": department,
                    "HireDate": hire_date,
                    "TerminationDate": None,  # Active employees
                    "AnnualSalary": salary
                }
                
                # Append to employee list
                employees.append(employee)
                
                # Increment the employee ID
                current_id = generate_employee_id(current_id)
    
    return employees

# Write the employee data to a CSV file
def save_to_csv(employees, filename='employees.csv'):
    with open(filename, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=employees[0].keys())
        writer.writeheader()
        writer.writerows(employees)

# Example usage
start_hire_date = "2023-01-23"
initial_employee_id = "PO-100001"
employees = generate_startup_employees(start_up_hires, start_hire_date, initial_employee_id)
save_to_csv(employees, 'prompt3.csv')



print("Employee data has been generated and saved to prompt3.csv.")
