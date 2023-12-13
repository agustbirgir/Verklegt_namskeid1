from LogicLayer.EmployeeLL import EmployeeLL
from LogicLayer.DestinationLL import DestinationLL
from LogicLayer.VoyageLL import VoyageLL
from DataLayer.data_wrapper import Data_Wrapper

class Logic_Wrapper:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()
        self.EmployeeLL = EmployeeLL(self.data_wrapper)
        self.VoyageLL = VoyageLL(self.data_wrapper)
        self.DestinationLL = DestinationLL(self.data_wrapper)

    # ------ EMPLOYEE ----------

    def add_employee(self, employee):
        return self.EmployeeLL.add_employee(employee)
    
    def get_all_employees(self):
        return self.EmployeeLL.get_all_employees()
    
    def get_all_pilots(self):
        return self.EmployeeLL.get_all_pilots()
    
    def get_all_attendants(self):
        return self.EmployeeLL.get_all_attendants()
    
    def find_employee_by_ssn(self, ssn):
        return self.EmployeeLL.find_employee_by_ssn(ssn)
    

    # ------- VOYAGE ------------

    def add_voyage(self, voyage):
        return self.VoyageLL.add_voyage(voyage)

    def get_voyage(self, departure, arrival):
        return self.VoyageLL.get_voyage(departure, arrival)
    
    def get_all_voyages(self):
        return self.VoyageLL.get_all_voyages()
    

    # ----- DESTINATION -----------

    def add_destination(self, destination):
        return self.DestinationLL.add_destination()

    def get_destination(self, country):
        return self.DestinationLL.get_destination(country)

    def get_all_destinations(self):
        return self.DestinationLL.get_all_destinations()