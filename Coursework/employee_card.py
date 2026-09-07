employee = {
    "first_name": "John", "last_name": "Doe", "age" : 28, 
    "address" : "123 Main Street, Apartment 4B",
    "experience_years" : 5, "position": "Data Analyst", 
    "salary": 75000, "code": "DEV-2026-JD-001" 
}

full_name = f"{employee['first_name']} {employee['last_name']}"

dept, year, initials, id_num = employee["code"].split('-')
print(f"""
--- Employee Profile ---
Name:    {full_name} ({employee['age']} years old)
Role:    {employee['position']} (${employee['salary']:,})
Exp:     {employee['experience_years']} years
Code:    Dept: {dept} | Year: {year} | Initials: {initials} | ID: {id_num}
------------------------
""")