import csv
from Models.Employee import Employee

class EmployeeIO:
    def __init__(self):
        self.file_name = "files/employees.csv"

    def get_all_employees(self):
        ret_list = []
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Employee(row["name"], row["profession"]))
        return ret_list
    
    def add_employee(self, employee):
        with open(self.file_name, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["name", "profession", "ssn","homeAddress", "gsmNumber", "email", "homePhone", "status", "scheduled"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow({'name': employee.name, 'profession': employee.profession, 'ssn': employee.ssn, 'homeAddress': employee.homeAddress, 'gsmNumber': employee.gsmNumber, 'email': employee.email, 'homePhone': employee.homePhone, 'status':employee.status, 'scheduled':employee.scheduled})

    def get_employee_voyage(self, employee):
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)