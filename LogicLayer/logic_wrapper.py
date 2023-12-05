from LogicLayer.EmployeeLL import EmployeeLL
from LogicLayer.DestinationLL import DestinationLL
from LogicLayer.VoyageLL import VoyageLL
from DataLayer.data_wrapper import Data_Wrapper

class Logic_Wrapper:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()
        self.EmployeeLL = EmployeeLL(self.data_wrapper)

    def add_employee(self, employee):
        return self.EmployeeLL.add_employee(employee)
    
    def get_all_employees(self):
        return self.EmployeeLL.get_all_employees()