import csv
from Models.Employee import Employee
import ast

class EmployeeIO:
    def __init__(self):
        self.file_name = "files/employees.csv"

    def get_all_employees(self):
        ret_list = []
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                ret_list.append(Employee(row["name"], row["profession"]))
        return ret_list
    
    def add_employee(self, employee):
        with open(self.file_name, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["name", "profession", "ssn","homeAddress", "gsmNumber", "email", "homePhone", "scheduled", "aircraftLicense"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow({'name': employee.name, 'profession': employee.profession, 
                             'ssn': employee.ssn, 'homeAddress': employee.homeAddress, 
                             'gsmNumber': employee.gsmNumber, 'email': employee.email, 
                             'homePhone': employee.homePhone, 'scheduled': employee.scheduled,
                             'aircraftLicense': employee.aircraftLicense})


    def find_employee_by_ssn(self, ssn):
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                if row["ssn"] == ssn:
                    return Employee(row["name"], row["profession"], row["ssn"], row["homeAddress"], row["gsmNumber"], row["email"], row["homePhone"], row["scheduled"], row["aircraftLicense"])
        return None
    
    def get_employee_by_name(self, name):
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                if row["name"] == name:
                    return Employee(row["name"], row["profession"], row["ssn"], row["homeAddress"], row["gsmNumber"], row["email"], row["homePhone"], row["scheduled"], row["aircraftLicense"])
        return None
    
    def get_pilots_by_license(self, license):
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            ret_list = []
            for row in reader:
                if row["aircraftLicense"] == license:
                    ret_list.append(Employee(row["name"], row["profession"], row["ssn"], row["homeAddress"], row["gsmNumber"], row["email"], row["homePhone"], row["scheduled"], row["aircraftLicense"]))
        return ret_list

    def update_employee(self, updated_employee):
        employees = []

        with open(self.file_name, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
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
                    'scheduled': updated_employee.scheduled,
                    'aircraftLicense': updated_employee.aircraftLicense
                    })
                else:
                    employees.append(row)

        with open(self.file_name, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["name", "profession", "ssn", "homeAddress", "gsmNumber", "email", "homePhone", "scheduled", "aircraftLicense"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
            writer.writeheader()
            for emp in employees:
                writer.writerow(emp)

    def get_employee_voyage(self, employee):
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")

    def get_all_pilots(self):
        ret_list = []
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                if row["profession"] == "Pilot" or row["profession"] == "Head Pilot":
                    ret_list.append(Employee(row["name"], row["profession"], row["ssn"], row["homeAddress"], row["gsmNumber"], row["email"], row["homePhone"], row["scheduled"], row["aircraftLicense"]))
        return ret_list

    def get_all_attendants(self):
        ret_list = []
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                if row["profession"] == "Attendant" or row["profession"] == "Head Flight Attendant":
                    ret_list.append(Employee(row["name"], row["profession"]))
        return ret_list
    
    def get_all_employees_schedule(self):
        ret_list = []
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                ret_list.append(Employee(row["name"], row["profession"], row["scheduled"]))
        return ret_list
    
    def employee_schedule_checker(self, date, working):
        ret_list = []
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            if working:
                for row in reader:
                    schedule_list = [item.strip("'") for item in row["scheduled"][1:-1].split(", ")]
                    for emp_sched in schedule_list:
                        if str(emp_sched) == str(date):
                            ret_list.append(Employee(row["name"], row["profession"]))
            else:
                for row in reader:
                    schedule_list = [item.strip("'") for item in row["scheduled"][1:-1].split(", ")]
                    is_working_at_date = False
                    for emp_sched in schedule_list:
                        if emp_sched == date:
                            is_working_at_date = True
                    if not is_working_at_date:
                        ret_list.append(Employee(row["name"]))
        return ret_list
    """
    def employee_schedule_checker(self, date, working):
        ret_list = []
        added_employees = set()  # To keep track of employees already added
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                schedule_list = [item.strip("'") for item in row["scheduled"][1:-1].split(", ")]
                is_working_at_date = any(emp_sched == date for emp_sched in schedule_list)
                
                if working and is_working_at_date and row["name"] not in added_employees:
                    ret_list.append(Employee(row["name"], row["profession"]))
                    added_employees.add(row["name"])

                elif not working and not is_working_at_date and row["name"] not in added_employees:
                    ret_list.append(Employee(row["name"]))
                    added_employees.add(row["name"])
        return ret_list
            """