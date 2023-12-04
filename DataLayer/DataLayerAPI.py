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
        #skoðar hvort seinasta í file er newline með þvi að nota binary 
        if os.path.exists(self.file_name) and os.path.getsize(self.file_name) > 0:
             #opna file i binary mode
             with open(self.file_name, 'rb+') as csvfile:
                 #fer til næst seinasta  byte i file
                 csvfile.seek(-2, os.SEEK_END)
                 #les seinasta byte og skoða hvort það er newline \n
                 if csvfile.read(1) != b'\n':
                     #ef ekki opna i append og hendi inn newline
                     with open(self.file_name, 'a', encoding='utf-8') as csvfile:
                         csvfile.write('\n')

        #opna file til að appenda new employee
        with open(self.file_name, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["name", "profession"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'name': employee.name, 'profession': employee.profession})
