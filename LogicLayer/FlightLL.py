import random
from datetime import timedelta

class FlightLL:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def add_flight(self, destination):
        """
        Add new flight to the flights.csv file

        Args:
            flight (Flight): Flight to be written to the file

        Examples:
            >>> add_flight(Flight)
            This call writes all the attributes of the Flight object to the flights.csv file
        """
        self.data_wrapper.add_flight(destination)

    def get_flight(self, country):
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
        return self.data_wrapper.get_flight(country)
    
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
        return self.data_wrapper.get_all_flights()
    
    def get_voyage_flights(self, id):
        """
        Return the two flights that are in a voygae

        Returns:
            list of Flight: A list containing two flights

        Examples:
            >>> get_all_flights()
            [Flight(Keflavik, 1010-11-10 10:20:00, 1010-11-10 13:10:00, Nuuk, 1891, NA021), Flight(Keflavik, 1990-10-12 10:11:00, 1990-10-12 12:51:00, Nuuk, 2067, NA022)]
        """
        return self.data_wrapper.get_voyage_flights(id)
    
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
        calculate_arrival = date + timedelta(hours=time.hour, minutes=time.minute)
        return calculate_arrival

    def create_unique_id(self):

        """
        Creates a random id.
        
        Returns: 
            Returns a random number between 0 and 5000

        Examples:
            >>> create_unique_id()
            3028

        """
        return random.randint(0, 5000)
