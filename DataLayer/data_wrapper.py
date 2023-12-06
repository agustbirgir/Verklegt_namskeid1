from DataLayer.EmployeeIO import EmployeeIO
from DataLayer.DestinationIO import DestinationIO
from DataLayer.VoyageIO import VoyageIO


class Data_Wrapper:
    def __init__(self):
        self.EmployeeIO = EmployeeIO()
        self.DestinationIO = DestinationIO()
        self.VoyageIO = VoyageIO()

    # ------ Employees -----------

    def get_all_employees(self):
        return self.EmployeeIO.get_all_employees()

    def add_employee(self, employee):
        return self.EmployeeIO.add_employee(employee)
    
    def get_all_pilots(self):
        return self.EmployeeIO.get_all_pilots()

    def get_all_attendants(self):
        return self.EmployeeIO.get_all_attendants()
    
    def find_employee_by_ssn(self, ssn):
        return self.EmployeeIO.find_employee_by_ssn(ssn)

    def update_employee(self, employee):
        self.EmployeeIO.update_employee(employee)


    
    # ------ Destination ---------

    def add_destination(self, destination):
        return self.DestinationIO.add_destination()
    
    def get_destination(self, country):
        return self.DestinationIO.get_destination(country)
    
    def get_all_destinations(self):
        return self.DestinationIO.get_all_destinations()
    

    # ------ Voyage -------------

    def add_voyage(self, voyage):
        return self.VoyageIO.add_voyage(voyage)
    
    def get_voyage(self, departure, arrival):
        return self.VoyageIO.get_voyage(departure, arrival)
    
    def get_all_voyages(self):
        return self.VoyageIO.get_all_voyages()
