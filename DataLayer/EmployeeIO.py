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

            writer.writerow({'name': employee.name, 'profession': employee.profession, 
                             'ssn': employee.ssn, 'homeAddress': employee.homeAddress, 
                             'gsmNumber': employee.gsmNumber, 'email': employee.email, 
                             'homePhone': employee.homePhone, 'status':employee.status, 
                             'scheduled':employee.scheduled})


    def find_employee_by_ssn(self, ssn):
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["ssn"] == ssn:
                    return Employee(row["name"], row["profession"], row["ssn"], row["homeAddress"], row["gsmNumber"], row["email"], row["homePhone"], row["status"], row["scheduled"])
        return None
    
    def get_employee_by_name(self, name):
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["name"] == name:
                    return Employee(row["name"], row["profession"], row["ssn"], row["homeAddress"], row["gsmNumber"], row["email"], row["homePhone"], row["status"], row["scheduled"])
        return None

    def update_employee(self, updated_employee):
        employees = []

        with open(self.file_name, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["ssn"] == updated_employee.ssn:
                # Update the employee's information
                    employees.append({
                    'name': updated_employee.name, 
                    'profession': updated_employee.profession, 
                    'ssn': updated_employee.ssn, 
                    'homeAddress': updated_employee.homeAddress, 
                    'gsmNumber': updated_employee.gsmNumber, 
                    'email': updated_employee.email, 
                    'homePhone': updated_employee.homePhone, 
                    'status': updated_employee.status, 
                    'scheduled': updated_employee.scheduled
                    })
                else:
                    employees.append(row)

        with open(self.file_name, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["name", "profession", "ssn", "homeAddress", "gsmNumber", "email", "homePhone", "status", "scheduled"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for emp in employees:
                writer.writerow(emp)

    def get_employee_voyage(self, employee):
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)


    def get_all_pilots(self):
        ret_list = []
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["profession"] == "Pilot" or row["profession"] == "Head pilot":
                    ret_list.append(Employee(row["name"], row["profession"]))
        return ret_list



    def get_all_attendants(self):
        ret_list = []
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row["profession"] == "Attendant" or row["profession"] == "Head attendant":
                    ret_list.append(Employee(row["name"], row["profession"]))
        return ret_list
    
    def get_all_employees_schedule(self):
        ret_list = []
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Employee(row["name"], row["profession"], row["scheduled"]))
        return ret_list