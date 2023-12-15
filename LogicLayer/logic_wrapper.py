from LogicLayer.EmployeeLL import EmployeeLL
from LogicLayer.DestinationLL import DestinationLL
from LogicLayer.VoyageLL import VoyageLL
from LogicLayer.FlightLL import FlightLL
from LogicLayer.AircraftLL import AircraftLL
from DataLayer.data_wrapper import Data_Wrapper

class Logic_Wrapper:
    def __init__(self):
        """
        Constructor that establishes a connection to the data wrapper
        """
        self.data_wrapper = Data_Wrapper()
        self.EmployeeLL = EmployeeLL(self.data_wrapper)
        self.VoyageLL = VoyageLL(self.data_wrapper)
        self.DestinationLL = DestinationLL(self.data_wrapper)
        self.AircraftLL = AircraftLL(self.data_wrapper)
        self.FlightLL = FlightLL(self.data_wrapper)

    # ------ EMPLOYEE ----------

    def add_employee(self, employee):
        """
        Add new employee to the employee.csv file

        Args:
            employee (Employee): Employee to be written to the file

        Examples:
            >>> add_employee(Employee)
            This call writes all the attributes of the Employee object to the employee.csv file
        """


        return self.EmployeeLL.add_employee(employee)
    
    def get_all_employees(self):
        """
        Returns all employees from employees.csv

        Returns:
            list of Employee: A list containing all employees

        Examples:
            >>> get_all_employees()
            [Employee(Siggi,Pilot,1214742314,2,3,a@g.is,4,['1010-11-10', '9999-11-11'],Boeing 737), Employee(Tommy Lee,Head Pilot,12345678,noatun 8,5812345,tommy@lee.com,1245678,[],Boeing 737)]
        """

        return self.EmployeeLL.get_all_employees()
    
    def get_all_pilots(self):
        """
        Get all employees that are pilots in the employees.csv file

        Returns:
            list of Employee: Returns a list of all employees that are pilots

        Examples:
            >>> get_all_pilots()
            [Employee(Siggi,Pilot,1214742314,as 5,1247402,a@g.is,4,['1010-11-10', '9999-11-11'];Boeing 737), Employee(Tommy Lee;Head Pilot;12345678;noatun 8;5812345;tommy@lee.com;1245678;[];Boeing 737)]
            
        """

        return self.EmployeeLL.get_all_pilots()
    
    def get_all_attendants(self):
        """
        Get all employees that are attendants in the employees.csv file

        Returns:
            list of Employee: Returns a list of all employees that are attendants

        Examples:
            >>> get_all_pilots()
            [Employee(Sigurjon,Head Flight Attendant,9374061953,Sævangur 8,5812345,agust@gmail.com,1234567,[],), Employee(Halli,Attendant,1047283940,Skaggaturn 12,5812345,Halli@gmail.com,8401640,[],)]
            
        """

        return self.EmployeeLL.get_all_attendants()
    
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

        return self.EmployeeLL.find_employee_by_ssn(ssn)
    
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

        return self.EmployeeLL.get_employee_by_name(name)
    
    def update_employee(self, employee):
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

        return self.EmployeeLL.update_employee(employee)
    
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

        return self.EmployeeLL.employee_schedule_checker(date, working)
    
    def get_schedule_of_employee(self, employee):
        """
        Gets schedule of employee

        Args: 
            employee (Employee): Get shedule of this employee
        
        Returns:
            Gets shcedule of employee

        Examples:
            >>> get_schedule_of_employee("Siggi")
            ['1010-11-10', '2023-12-15']

        """

        return self.EmployeeLL.get_schedule_of_employee(employee)
    
    def sort_pilots_by_license(self):
        """
        Sorts the pilot list by aircraft license
        
        Returns:
            A list of pilots sorted by their aircraft types
        
        Examples:
            >>> sort_pilots_by_license()
            name: Siggi, license: Boeing 737
            name: Tommy Lee, license: Boeing 737
            name: Agust, license: Airbus A330
            name: Jonas, license: Airbus A330

        """

        return self.EmployeeLL.sort_pilots_by_license()
    
    def get_pilots_by_license(self, license):
        """
        Sorts the pilot list by aircraft license
        
        Returns:
            A list of pilots sorted by their aircraft types
        
        Examples:
            >>> sort_pilots_by_license()
            name: Siggi, license: Boeing 737
            name: Tommy Lee, license: Boeing 737
            name: Agust, license: Airbus A330
            name: Jonas, license: Airbus A330

        """

        return self.EmployeeLL.get_pilots_by_license(license)
    
    # ------- VOYAGE ------------

    def add_voyage(self, voyage):
        """
        Add new voyage to the voyage.csv file

        Args:
            voyage (Voyage): Voyage to be written to the file

        Examples:
            >>> add_voyage(Voyage)
            This call writes all the attributes of the Voyage object to the voyages.csv file
        """
        return self.VoyageLL.add_voyage(voyage)

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

        return self.VoyageLL.get_voyage(id)
    
    def get_all_voyages(self):
        """
        Returns all voyages from voyages.csv

        Returns:
            list of Voyage: A list containing all voyages

        Examples:
            >>> get_all_voyages()
            [Voyage(2, 2, ['Siggi', 'Helgi', 'Jonas', 'Halli'], 2, Airbus A330), Voyage(3891, 3891, [], 3891, Boeing 737)]
        """

        return self.VoyageLL.get_all_voyages()
    
    def voyage_add_employees(self, employeeList, id):
        """
        Add employees to a voyages crew

        Args:
            employeeList (list): List of employees to be added
            id (string): Id of the voyage for the employees to be added

        Examples:
            >>> voyage_add_employees(['John', 'Chad'], "2")
            This call adds John and Chad to the crew of the voyage with ID 2 
            
        """

        return self.VoyageLL.voyage_add_employees(employeeList, id)
    
    def get_crew_of_voyage(self, voyage):
        """
        Gets the crew of a specific voyage

        Args: 
            voyage (Voyage): Get the crew of this voyage
        
        Returns: 
            A list of names of employees in a voyage

        Examples:
            >>> get_crew_of_voyage(2)
            ['Siggi', 'Agust']
        """
        return self.VoyageLL.get_crew_of_voyage(voyage)
    
    def get_week_dates(self, date):

        """
        Gets dates across a week

        Args: 
            date (string): Date to be used
        
        Returns:   
            A list with the week the date is in

        Examples:
            >>> get_week_dates(2023-12-15)
            ['2023-12-11', '2023-12-12', 2023-12-13', 2023-12-14', 2023-12-15', 2023-12-16', 2023-12-17']
        """

        return self.VoyageLL.get_week_dates(date)
    
    def get_voyages_of_day(self, date_looking):                         #this for flight or crew?
        """
        Gets a voyage for a specific day

        Args: 
            date_looking (string): The date to be searched
        
        Returns: 
            All voyages that have the matching date
        
        Examples:
            >>> get_voyages_of_day(2023-10-18)
            [Voyage(1538,1538,['', 'Halli', 'Joi', 'Tommy Lee', 'Siggi'],1538,Boeing 737)]
        """

        return self.VoyageLL.get_voyages_of_day(date_looking)
    

    # ----- DESTINATION -----------

    def add_destination(self, destination):
        """
        Add new flight to the destinations.csv file

        Args:
            destination (Destination): Destination to be written to the file

        Examples:
            >>> add_destination(Destination)
            This call writes all the attributes of the Destination object to the destinations.csv file
        """

        return self.DestinationLL.add_destination(destination)

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

        return self.DestinationLL.get_destination(country)

    def get_all_destinations(self):
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

        return self.DestinationLL.get_all_destinations()
    
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

        return self.FlightLL.add_flight(flight)
    
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

        return self.FlightLL.get_flight(id)
    
    def get_all_flights(self):
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

        return self.FlightLL.get_all_flights()
    
    def get_voyage_flights(self, id):
        """
        Return the two flights that are in a voygae

        Returns:
            list of Flight: A list containing two flights

        Examples:
            >>> get_all_flights()
            [Flight(Keflavik, 1010-11-10 10:20:00, 1010-11-10 13:10:00, Nuuk, 1891, NA021), Flight(Keflavik, 1990-10-12 10:11:00, 1990-10-12 12:51:00, Nuuk, 2067, NA022)]
        """

        return self.FlightLL.get_voyage_flights(id)

    def calculate_arrival_time(self, date, time):
        """
        Adds given time to a date.

            Args: 
                date (Date): The date to add the time to
                time (Date): The hours and minutrs to add to the date
        
        Returns: The time added to the date

        Examples:
            >>> calculate_arrival_time(2023-12-15 10:00, 3:00)
            2023-12-15 13:00
 
        """

        return self.FlightLL.calculate_arrival_time(date, time)
    
    def create_unique_id(self):

        """
        Creates a random id.
        
        Returns: 
            Returns a random number between 0 and 5000

        Examples:
            >>> create_unique_id()
            3028

        """

        return self.FlightLL.create_unique_id()

    # ------- Aircraft ----------
    def add_aircraft(self, flight):
        """
        Add new aircraft to the aircrafts.csv file

        Args:
            aircraft (Aircraft): Aircraft to be written to the file

        Examples:
            >>> add_aircraft(Aircraft)
            This call writes all the attributes of the Aircraft object to the aircrafts.csv file
        """
        self.AircraftLL.add_aircraft(flight)
    
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
        return self.AircraftLL.get_aircraft(name)
    
    def get_all_aircraft(self):
        """
        Returns all aircraft from aircraft.csv

        Returns:
            list of Aircraft: A list containing all aircrafty

        Examples:
            >>> get_all_aircraft()
            [Aircraft(Airbus A330,A330,Airbus SE,250), Aircraft(Boeing 737,747,Boeing Co,366)]
        """
        return self.AircraftLL.get_all_aircraft()