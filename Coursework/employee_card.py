# Employee Data Profile
employee = {
    "first_name": "John",
    "last_name": "Doe",
    "address": "123 Main Street, Apartment 4B",
    "age": 28,
    "experience_years": 5,
    "position": "Data Analyst",
    "salary": 75000,
    "code": "DEV-2026-JD-001"
}

# Derived Information
full_name = f"{employee['first_name']} {employee['last_name']}"

# Parsed Code Components
department = employee["code"][0:3]
year_code = employee["code"][4:8]
initials = employee["code"][9:11]
last_three = employee["code"][-3:]

# Printed Outputs
print(f"{full_name} is {employee['age']} years old")
print(f"Experience: {employee['experience_years']} years")
print(f"Employee: {full_name} | Age: {employee['age']} | Position: {employee['position']} | Salary: ${employee['salary']}")

print(department)
print(year_code)
print(initials)
print(last_three)
