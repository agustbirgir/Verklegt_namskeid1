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
        self.employee_logic = EmployeeLL(self.data_wrapper)

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
        return self.employee_logic.find_employee_by_ssn(ssn)
    
    def update_employee(self, ssn):
        pass
    
    # ------- VOYAGE ------------

    def add_voyage(self, voyage):
        return self.VoyageLL.add_voyage(voyage)

    def get_voyage(self, departure, arrival):
        return self.VoyageLL.get_voyage(departure, arrival)
    
    def get_all_voyages(self):
        return self.VoyageLL.get_all_voyages()
    
    def voyage_add_pilot(self, voyage, pilot):
        """Add a pilot to a voyage"""
        return self.VoyageLL.voyage_add_pilot(voyage, pilot)

    def voyage_add_attendant(self, voyage):
        """Add an attendant to a voyage"""
        return self.VoyageLL.voyage_add_attendant(voyage)
    

    # ----- DESTINATION -----------

    def add_destination(self, destination):
        return self.DestinationLL.add_destination()

    def get_destination(self, country):
        return self.DestinationLL.get_destination(country)

    def get_all_destinations(self):
        return self.DestinationLL.get_all_destinations()