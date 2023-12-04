import os
import csv
from Models.Employee import Employee

class DataLayerAPI:
    def __init__(self):
        #print(os.getcwd())
        self.file_name = "Verklegt_namskeid1/files/employees.csv"

    def get_all_employees(self):
        ret_list = []
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Employee(row["name"], row["profession"]))
        return ret_list

    def create_employee(self, employee):
        with open(self.file_name, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["name", "profession"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writerow({'name': employee.name, 'profession':employee.profession})
