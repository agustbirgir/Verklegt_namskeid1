from datetime import datetime, timedelta
from UiLayer.input_validators import *

class VoyageLL:
    def __init__(self, data_connection):
        """
        Constructor that establishes a connection to the data wrapper
        """
        self.data_wrapper = data_connection

    def add_voyage(self, voyage):
        """
        Add new voyage to the voyage.csv file

        Args:
            voyage (Voyage): Voyage to be written to the file

        Examples:
            >>> add_voyage(Voyage)
            This call writes all the attributes of the Voyage object to the voyages.csv file
        """
        self.data_wrapper.add_voyage(voyage)

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
        return self.data_wrapper.get_voyage(id)

    def get_all_voyages(self):
        """
        Returns all voyages from flights.csv

        Returns:
            list of Voyage: A list containing all voyages

        Examples:
            >>> get_all_voyages()
            [Voyage(2, 2, ['Siggi', 'Helgi', 'Jonas', 'Halli'], 2, Airbus A330), Voyage(3891, 3891, [], 3891, Boeing 737)]
        """
        return self.data_wrapper.get_all_voyages()

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
        self.data_wrapper.voyage_add_employees(employeeList, id)
    
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
        crew_list = [item.strip("'") for item in voyage.crew[1:-1].split(", ")]
        return crew_list

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

        date = datetime.strptime(date, "%Y-%m-%d")

        start_date = date - timedelta(days=date.weekday())
        
        week_dates = [(start_date+timedelta(days=d)).date() for d in range(7)]

        return week_dates

    
    def get_voyages_of_day(self, date_looking):

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

        voyages = self.data_wrapper.get_all_voyages()
        ret_list = []
        for v in voyages:

            voyage_flight = self.data_wrapper.get_flight(v.id)
            date_of_voyage = voyage_flight.departureTime
            date_of_voyage = datetime.strptime(date_of_voyage, '%Y-%m-%d %H:%M:%S').date()

            if str(date_of_voyage) == str(date_looking):
                ret_list.append(v)

        return ret_list