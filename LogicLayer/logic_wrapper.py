from LogicLayer.EmployeeLL import EmployeeLL
from LogicLayer.DestinationLL import DestinationLL
from LogicLayer.VoyageLL import VoyageLL
from LogicLayer.FlightLL import FlightLL
from DataLayer.data_wrapper import Data_Wrapper

class Logic_Wrapper:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()
        self.EmployeeLL = EmployeeLL(self.data_wrapper)
        self.VoyageLL = VoyageLL(self.data_wrapper)
        self.DestinationLL = DestinationLL(self.data_wrapper)
        self.FlightLL = FlightLL(self.data_wrapper)

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
    
    def get_employee_by_name(self, name):
        return self.EmployeeLL.get_employee_by_name(name)
    
    def update_employee(self, employee):
        return self.EmployeeLL.update_employee(employee)
    
    def employee_schedule_checker(self, date, working):
        return self.EmployeeLL.employee_schedule_checker(date, working)
    
    def get_schedule_of_employee(self, employee):
        return self.EmployeeLL.get_schedule_of_employee(employee)
    
    # ------- VOYAGE ------------

    def add_voyage(self, voyage):
        return self.VoyageLL.add_voyage(voyage)

    def get_voyage(self, id):
        return self.VoyageLL.get_voyage(id)
    
    def get_all_voyages(self):
        return self.VoyageLL.get_all_voyages()
    
    def voyage_add_employee(self, employeeList, id):
        return self.VoyageLL.voyage_add_employee(employeeList, id)
    
    def get_crew_of_voyage(self, voyage):
        return self.VoyageLL.get_crew_of_voyage(voyage)
    
    def get_voyages_of_day(self, date_looking):                         #this for flight or crew?
        return self.VoyageLL.get_voyages_of_day(date_looking)
    
    def unmanned_voyage_fetcher(self, command, input):                  #this is like, 90% for crew manager, right?
        return self.VoyageLL.unmanned_voyage_fetcher(command, input)
    

    # ----- DESTINATION -----------

    def add_destination(self, destination):
        return self.DestinationLL.add_destination(destination)

    def get_destination(self, country):
        return self.DestinationLL.get_destination(country)

    def get_all_destinations(self):
        return self.DestinationLL.get_all_destinations()
    
    # ------- Flight ----------

    def add_flight(self, flight):
        return self.FlightLL.add_flight(flight)
    
    def get_flight(self, id):
        return self.FlightLL.get_flight(id)
    
    def get_all_flights(self):
        return self.FlightLL.get_all_flights()
    
    def calculate_arrival_time(self, date, time):
        return self.FlightLL.calculate_arrival_time(date, time)
    
    def create_unique_id(self):
        return self.FlightLL.create_unique_id()