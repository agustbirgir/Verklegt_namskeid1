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

        """
        	moves info between the logic and ui layer

            Args: employee
        
            Returns: the relevent function from the logic layer

        """

        return self.EmployeeLL.add_employee(employee)
    
    def get_all_employees(self):

        """
        	moves info between the logic and ui layer

            Args: none
        
            Returns: the relevent function from the logic layer

        """

        return self.EmployeeLL.get_all_employees()
    
    def get_all_pilots(self):

        """
        	moves info between the logic and ui layer

            Args: none
        
            Returns: the relevent function from the logic layer

        """

        return self.EmployeeLL.get_all_pilots()
    
    def get_all_attendants(self):

        """
        	moves info between the logic and ui layer

            Args: none
        
            Returns: the relevent function from the logic layer

        """

        return self.EmployeeLL.get_all_attendants()
    
    def find_employee_by_ssn(self, ssn):

        """
        	moves info between the logic and ui layer

            Args: ssn
        
            Returns: the relevent function from the logic layer

        """

        return self.EmployeeLL.find_employee_by_ssn(ssn)
    
    def get_employee_by_name(self, name):

        """
        	moves info between the logic and ui layer

            Args: name
        
            Returns: the relevent function from the logic layer

        """

        return self.EmployeeLL.get_employee_by_name(name)
    
    def update_employee(self, employee):

        """
        	moves info between the logic and ui layer

            Args: employee
        
            Returns: the relevent function from the logic layer

        """

        return self.EmployeeLL.update_employee(employee)
    
    def employee_schedule_checker(self, date, working):

        """
        	moves info between the logic and ui layer

            Args: date, working
        
            Returns: the relevent function from the logic layer

        """

        return self.EmployeeLL.employee_schedule_checker(date, working)
    
    def get_schedule_of_employee(self, employee):

        """
        	moves info between the logic and ui layer

            Args: employee
        
            Returns: the relevent function from the logic layer

        """

        return self.EmployeeLL.get_schedule_of_employee(employee)
    
    def sort_pilots_by_license(self):

        """
        	moves info between the logic and ui layer

            Args: none
        
            Returns: the relevent function from the logic layer

        """

        return self.EmployeeLL.sort_pilots_by_license()
    
    def get_pilots_by_license(self, license):

        """
        	moves info between the logic and ui layer

            Args: license
        
            Returns: the relevent function from the logic layer

        """

        return self.EmployeeLL.get_pilots_by_license(license)
    
    # ------- VOYAGE ------------

    def add_voyage(self, voyage):

        """
        	moves info between the logic and ui layer

            Args: voyage
        
            Returns: the relevent function from the logic layer

        """

        return self.VoyageLL.add_voyage(voyage)

    def get_voyage(self, id):

        """
        	moves info between the logic and ui layer

            Args: id
        
            Returns: the relevent function from the logic layer

        """

        return self.VoyageLL.get_voyage(id)
    
    def get_all_voyages(self):

        """
        	moves info between the logic and ui layer

            Args: none
        
            Returns: the relevent function from the logic layer

        """

        return self.VoyageLL.get_all_voyages()
    
    def voyage_add_employee(self, employeeList, id):

        """
        	moves info between the logic and ui layer

            Args: employee
        
            Returns: the relevent function from the logic layer

        """


        return self.VoyageLL.voyage_add_employee(employeeList, id)
    
    def voyage_add_flight(self, flight, id):

        """
        	moves info between the logic and ui layer

            Args: flight, id
        
            Returns: the relevent function from the logic layer

        """

        return self.VoyageLL.voyage_add_flight(flight, id)
    
    def get_crew_of_voyage(self, voyage):

        """
        	moves info between the logic and ui layer

            Args: voyage
        
            Returns: the relevent function from the logic layer

        """

        return self.VoyageLL.get_crew_of_voyage(voyage)
    
    def get_week_dates(self, date):

        """
        	moves info between the logic and ui layer

            Args: date
        
            Returns: the relevent function from the logic layer

        """

        return self.VoyageLL.get_week_dates(date)
    
    def get_voyages_of_day(self, date_looking):                         #this for flight or crew?

        """
        	moves info between the logic and ui layer

            Args: date_looking
        
            Returns: the relevent function from the logic layer

        """

        return self.VoyageLL.get_voyages_of_day(date_looking)
    
    def unmanned_voyage_fetcher(self, command, input):                  #this is like, 90% for crew manager, right?

        """
        	moves info between the logic and ui layer

            Args: command, input
        
            Returns: the relevent function from the logic layer

        """

        return self.VoyageLL.unmanned_voyage_fetcher(command, input)
    

    # ----- DESTINATION -----------

    def add_destination(self, destination):

        """
        	moves info between the logic and ui layer

            Args: destination
        
            Returns: the relevent function from the logic layer

        """

        return self.DestinationLL.add_destination(destination)

    def get_destination(self, country):

        """
        	moves info between the logic and ui layer

            Args: country
        
            Returns: the relevent function from the logic layer

        """

        return self.DestinationLL.get_destination(country)

    def get_all_destinations(self):

        """
        	moves info between the logic and ui layer

            Args: none
        
            Returns: the relevent function from the logic layer

        """

        return self.DestinationLL.get_all_destinations()
    
    # ------- Flight ----------

    def add_flight(self, flight):

        """
        	moves info between the logic and ui layer

            Args: flight
        
            Returns: the relevent function from the logic layer

        """

        return self.FlightLL.add_flight(flight)
    
    def get_flight(self, id):

        """
        	moves info between the logic and ui layer

            Args: id
        
            Returns: the relevent function from the logic layer

        """

        return self.FlightLL.get_flight(id)
    
    def get_all_flights(self):

        """
        	moves info between the logic and ui layer

            Args: none
        
            Returns: the relevent function from the logic layer

        """

        return self.FlightLL.get_all_flights()
    
    def get_voyage_flights(self, id):

        """
        	moves info between the logic and ui layer

            Args: id
        
            Returns: the relevent function from the logic layer

        """

        return self.FlightLL.get_voyage_flights(id)

    def calculate_arrival_time(self, date, time):

        """
        	moves info between the logic and ui layer

            Args: date, time
        
            Returns: the relevent function from the logic layer

        """

        return self.FlightLL.calculate_arrival_time(date, time)
    
    def create_unique_id(self):

        """
        	moves info between the logic and ui layer

            Args: none
        
            Returns: the relevent function from the logic layer

        """

        return self.FlightLL.create_unique_id()