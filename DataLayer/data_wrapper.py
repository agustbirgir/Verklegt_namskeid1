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
        """
        Get all employees from the employees.csv file

        Returns:
            returns get_all_employees() from the EmployeeIO file

        Examples:
            >>> get_all_employees()
            [Employee(Siggi,Pilot,1214742314,2,3,a@g.is,4,['1010-11-10', '9999-11-11'],Boeing 737), Employee(Tommy Lee,Head Pilot,12345678,noatun 8,5812345,tommy@lee.com,1245678,[],Boeing 737)]
        """
        return self.EmployeeIO.get_all_employees()

    def add_employee(self, employee):
        """
        Add new employee to the employee.csv file

        Args:
            employee (Employee): Employee to be written to the csv file

        Examples:
            >>> add_employee(Employee)
            This call writes all the attributes of the Employee object to the employee.csv file
        """
        self.EmployeeIO.add_employee(employee)

    def get_all_pilots(self):
        """
        Get all employees that are pilots in the employees.csv file

        Returns:
            list of Employee: Returns a list of all employees that are pilots

        Examples:
            >>> get_all_pilots()
            [Employee(Siggi,Pilot,1214742314,as 5,1247402,a@g.is,4,['1010-11-10', '9999-11-11'];Boeing 737), Employee(Tommy Lee;Head Pilot;12345678;noatun 8;5812345;tommy@lee.com;1245678;[];Boeing 737)]
            
        """
        return self.EmployeeIO.get_all_pilots()

    def get_all_attendants(self):
        """
        Get all employees that are attendants in the employees.csv file

        Returns:
            list of Employee: Returns a list of all employees that are attendants

        Examples:
            >>> get_all_pilots()
            [Employee(Sigurjon,Head Flight Attendant,9374061953,Sævangur 8,5812345,agust@gmail.com,1234567,[],), Employee(Halli,Attendant,1047283940,Skaggaturn 12,5812345,Halli@gmail.com,8401640,[],)]
            
        """
        return self.EmployeeIO.get_all_attendants()
    
    def find_employee_by_ssn(self, ssn):
        """
        Returns a specific employee from employees.csv based on social security number

        Args:
            ssn (string): Social security number of the employee

        Returns:
            employee (Employee): Employee to be found

        Examples:
            >>> find_employee_by_ssn(1090452944)
            Employee(Joi,Head Flight Attendant,1090452944,Sævangur 8,5812345,agust@gmail.com,1234567,[],)
            >>> get_flight(Thorshavn)
            Employee(Siggi,Pilot,1214742314,2,3,a@g.is,4,['1010-11-10', '9999-11-11'],Boeing 737)
        """
        return self.EmployeeIO.find_employee_by_ssn(ssn)
    
    def get_employee_by_name(self, name):
        """
        Get employee in the employees.csv file by name

        Args:
            name (string): Employee name to be found
        
        Returns:
            employee (Employee): Returns an employee

        Examples:
            >>> get_employee_by_name(Siggi)
            Employee(Siggi,Pilot,1214742314,2,3,a@g.is,4,['1010-11-10', '9999-11-11'],Boeing 737)
            
        """
        return self.EmployeeIO.get_employee_by_name(name)

    def update_employee(self, employee):
        """
        Take in an updated employee and update the employee in the employees.csv file

        Args:
            updated_employee (string): Employee to be updated in the csv file

        Examples:
            >>> update_employee(Employee())
            Updates the updated attributes of the employee to the csv file
            
        """
        self.EmployeeIO.update_employee(employee)

    def employee_schedule_checker(self, date, working):
        """
        Return all employees that are not working or are working on a certain date.

        Args:
            date (string): The date to be checked
            working (boolean): If employee is working or not

        Returns:
            list of Employee: Returns a list of all employees that are attendants

        Examples:
            >>> get_all_pilots()
            [Employee(Sigurjon,Head Flight Attendant,9374061953,Sævangur 8,5812345,agust@gmail.com,1234567,[],), Employee(Halli,Attendant,1047283940,Skaggaturn 12,5812345,Halli@gmail.com,8401640,[],)]
            
        """
        return self.EmployeeIO.employee_schedule_checker(date, working)
    
    def get_pilots_by_license(self, license):
        """
        Get pilots in the employees.csv file by their aircraft license

        Args:
            license (string): Name of aircraft
        
        Returns:
            list of Employee: Returns a list of pilots

        Examples:
            >>> get_pilots_by_license(Boeing 737)
            Employee(Siggi,Pilot,1214742314,2,3,a@g.is,4,['1010-11-10', '9999-11-11'],Boeing 737)
            
        """
        return self.EmployeeIO.get_pilots_by_license(license)


    
    # ------ Destination ---------

    def add_destination(self, destination):
        """
        Add new flight to the destinations.csv file

        Args:
            destination (Destination): Destination to be written to the file

        Examples:
            >>> add_destination(Destination)
            This call writes all the attributes of the Destination object to the destinations.csv file
        """
        return self.DestinationIO.add_destination(destination)
    
    def get_destination(self, country):
        """
        Returns a specific destination from destinations.csv based on city

        Args:
            city (string): The city of the destination

        Returns:
            Destination: Returns a destination

        Examples:
            >>> get_flight(Nuuk)
            Destination(Greenland, Nuuk, Nuuk Airport, 2:40, 2000, john, 12345678, 01)
            >>> get_flight(Thorshavn)
            Destination(Faroe Islands, Thorshavn, Vagar Airport, 5:30, 4500, joe, 13579864, 01)
        """
        return self.DestinationIO.get_destination(country)
    
    def get_all_destinations(self):
        """
        Returns all destinations from destinations.csv

        Returns:
            list of Destination: A list containing all destinations

        Examples:
            >>> get_all_destinations()
            [Destination(Greenland, Nuuk, Nuuk Airport, 2:40, 2000, john, 12345678, 01), Destination(Faroe Islands, Thorshavn, Vagar Airport, 5:30, 4500, joe, 13579864, 01)]
        """
        return self.DestinationIO.get_all_destinations()
    

    # ------ Voyage -------------

    def add_voyage(self, voyage):
        """
        Add new voyage to the voyage.csv file

        Args:
            voyage (Voyage): Voyage to be written to the file

        Examples:
            >>> add_flight(Voyage)
            This call writes all the attributes of the Voyage object to the voyages.csv file
        """
        return self.VoyageIO.add_voyage(voyage)
    
    def get_voyage(self, id):
        """
        Returns a specific voyage from voyages.csv based on id

        Args:
            id (string): The id of the voyage

        Returns:
            Voyage: returns a voyage

        Examples:
            >>> get_voyage(2)
            Voyage(2, 2, ['Siggi', 'Helgi', 'Jonas', 'Halli'], 2, Airbus A330)
            >>> get_flight(3891)
            Voyage(3891, 3891, [], 3891, Boeing 737)
        """
        return self.VoyageIO.get_voyage(id)
    
    def get_all_voyages(self):
        """
        Returns all flights from flights.csv

        Returns:
            list of Voyage: A list containing all voyages

        Examples:
            >>> get_all_voyages()
            [Voyage(2, 2, ['Siggi', 'Helgi', 'Jonas', 'Halli'], 2, Airbus A330), Voyage(3891, 3891, [], 3891, Boeing 737)]
        """
        return self.VoyageIO.get_all_voyages()
    
    def voyage_add_employee(self, employeeList, id):
        """
        Add new aircraft to a voyage

        Args:
            aircraft (string): Name of the aircraft to be added
            id (string): Id of the voyage for the aircraft to be added

        Examples:
            >>> voyage_add_flight("Boeing 737", "2")
            This call writes the flight "Boeing 737" as the aircraft for the voyage with ID 2 
            
        """
        return self.VoyageIO.voyage_add_employee(employeeList, id)
    
    def voyage_add_flight(self, flight, id):
        """
        Add employees to a voyages crew

        Args:
            employeeList (list): List of employees to be added
            id (string): Id of the voyage for the employees to be added

        Examples:
            >>> voyage_add_employee(['John', 'Chad'], "2")
            This call adds John and Chad to the crew of the voyage with ID 2 
            
        """
        return self.VoyageIO.voyage_add_flight(flight, id)
        

    # ------- Flight ----------

    def add_flight(self, flight):
        """
        Add new flight to the flights.csv file

        Args:
            flight (Flight): Flight to be written to the file

        Examples:
            >>> add_flight(Flight)
            This call writes all the attributes of the Flight object to the flights.csv file
        """
        return self.FlightIO.add_flight(flight)
    
    def get_flight(self, id):
        """
        Returns a specific flight from flights.csv based on id

        Args:
            id (string): The id of the flight

        Returns:
            Flight: Returns a flight

        Examples:
            >>> get_flight(1891)
            Flight(Keflavik, 1010-11-10 10:20:00, 1010-11-10 13:10:00, Nuuk, 1891, NA021)
            >>> get_flight(1891)
            Flight(Keflavik, 1990-10-12 10:11:00, 1990-10-12 12:51:00, Nuuk, 2067, NA034)
        """
        return self.FlightIO.get_flight(id)
    
    def get_all_flights(self):
        """
        Returns all flights from flights.csv

        Returns:
            list of Flight: A list containing all flights

        Examples:
            >>> get_all_flights()
            [Flight(Keflavik, 1010-11-10 10:20:00, 1010-11-10 13:10:00, Nuuk, 1891, NA021), Flight(Keflavik, 1990-10-12 10:11:00, 1990-10-12 12:51:00, Nuuk, 2067, NA034)]
        """
        return self.FlightIO.get_all_flights()
    
    def get_voyage_flights(self, id):
        """
        Return the two flights that are in a voygae

        Returns:
            list of Flight: A list containing two flights

        Examples:
            >>> get_all_flights()
            [Flight(Keflavik, 1010-11-10 10:20:00, 1010-11-10 13:10:00, Nuuk, 1891, NA021), Flight(Keflavik, 1990-10-12 10:11:00, 1990-10-12 12:51:00, Nuuk, 2067, NA022)]
        """
        return self.FlightIO.get_voyage_flights(id)
    
    # ------ Aircraft ---------

    def add_aircraft(self, aircraft):
        """
        Add new aircraft to the aircrafts.csv file

        Args:
            aircraft (Aircraft): Aircraft to be written to the file

        Examples:
            >>> add_destination(Aircraft)
            This call writes all the attributes of the Aircraft object to the aircrafts.csv file
        """
        return self.AircraftIO.add_aircraft(aircraft)

    def get_aircraft(self, name):
        """
        Returns a specific aircraft from aircrafts.csv based on name

        Args:
            name (string): The name of the aircraft

        Returns:
            Flight: Returns an aircraft

        Examples:
            >>> get_aircraft(Boeing 737)
            Aircraft(Boeing 737,747,Boeing Co,366)
            >>> get_aircraft(Airbus A330)
            Aircraft(Airbus A330,A330,Airbus SE,250)
        """
        return self.AircraftIO.get_aircraft(name)
    
    def get_all_aircrafts(self):
        """
        Returns all aircraft from aircraft.csv

        Returns:
            list of Aircraft: A list containing all aircrafty

        Examples:
            >>> get_all_aircraft()
            [Aircraft(Airbus A330,A330,Airbus SE,250), Aircraft(Boeing 737,747,Boeing Co,366)]
        """
        return self.AircraftIO.get_all_aircrafts()