import csv
from Models.Employee import Employee

class EmployeeIO:
    def __init__(self):
        self.file_name = "Verklegt_namskeid1/files/employees.csv"

    def get_all_employees(self):
        ret_list = []
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Employee(row["name"], row["profession"]))
        return ret_list
    
    def add_employee(self, employee):
        with open(self.file_name, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["name", "profession"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow({'name': employee.name, 'profession': employee.profession})

    def get_employee_voyage(self, employee):
        ret_list = []
        with open(self.file_name, newline='', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)