from DataLayer.EmployeeIO import EmployeeIO
from DataLayer.DestinationIO import DestinationIO
from DataLayer.VoyageIO import VoyageIO
from DataLayer.FlightIO import FlightIO
from DataLayer.AircraftIO import AircraftIO


class Data_Wrapper:
    def __init__(self):
        self.EmployeeIO = EmployeeIO()
        self.DestinationIO = DestinationIO()
        self.VoyageIO = VoyageIO()
        self.FlightIO = FlightIO()
        self.AircraftIO = AircraftIO()

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
    
    def get_employee_by_name(self, name):
        return self.EmployeeIO.get_employee_by_name(name)

    def update_employee(self, employee):
        self.EmployeeIO.update_employee(employee)

    def get_all_employees_schedule(self):
        return self.EmployeeIO.get_all_employees_schedule()
    
    def employee_schedule_checker(self, date, working):
        return self.EmployeeIO.employee_schedule_checker(date, working)


    
    # ------ Destination ---------

    def add_destination(self, destination):
        return self.DestinationIO.add_destination(destination)
    
    def get_destination(self, country):
        return self.DestinationIO.get_destination(country)
    
    def get_all_destinations(self):
        return self.DestinationIO.get_all_destinations()
    

    # ------ Voyage -------------

    def add_voyage(self, voyage):
        return self.VoyageIO.add_voyage(voyage)
    
    def get_voyage(self, id):
        return self.VoyageIO.get_voyage(id)
    
    def get_all_voyages(self):
        return self.VoyageIO.get_all_voyages()
    
    def voyage_add_employee(self, employeeList, id):
        return self.VoyageIO.voyage_add_employee(employeeList, id)

    # ------- Flight ----------

    def add_flight(self, flight):
        return self.FlightIO.add_flight(flight)
    
    def get_flight(self, id):
        return self.FlightIO.get_flight(id)
    
    def get_all_flights(self):
        return self.FlightIO.get_all_flights()
    
    # ------ Aircraft ---------

    def add_aircraft(self, aircraft):
        """Add aircraft to the csv file"""
        return self.AircraftIO.add_aircraft(aircraft)

    def get_aircraft(self, name):
        """Return a specific aircraft"""
        return self.AircraftIO.get_aircraft(name)
    
    def get_all_aircrafts(self):
        """Return all of the aircrafts"""
        return self.AircraftIO.get_all_aircrafts()