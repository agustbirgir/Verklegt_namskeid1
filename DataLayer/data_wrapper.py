from DataLayer.EmployeeIO import EmployeeIO
from DataLayer.DestinationIO import DestinationIO
from DataLayer.VoyageIO import VoyageIO


class Data_Wrapper:
    def __init__(self):
        self.EmployeeIO = EmployeeIO()
        self.DestinationIO = DestinationIO()
        self.VoyageIO = VoyageIO()

    def get_all_employees(self):
        return self.EmployeeIO.get_all_employees()

    def add_employee(self, employee):
        return self.EmployeeIO.add_employee(employee)