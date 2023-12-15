import random
from datetime import timedelta

class FlightLL:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def add_flight(self, destination):

        """
        	adds flight.

            Args: destination
        
            Returns: moves from destination into datalayer to add a flight

    """

        """Add flight"""
        self.data_wrapper.add_flight(destination)

    def get_flight(self, country):

        """
        	gets flight.

            Args: destination
        
            Returns: uses country/destination to get flights from data layer

    """

        """Return a specific flight"""
        return self.data_wrapper.get_flight(country)
    
    def get_all_flights(self):

        """
        	gets all flights.

            Args: none
        
            Returns: gets all flights ongoing from datalayer

    """

        """Return all of the flights"""
        return self.data_wrapper.get_all_flights()
    
    def get_voyage_flights(self, id):

        """
        	gets voyage flights

            Args: id
        
            Returns: voyage flight from data layer

    """

        return self.data_wrapper.get_voyage_flights(id)
    
    def calculate_arrival_time(self, date, time):

        """
        	calculates the time it takes to arrive.

            Args: date, time
        
            Returns: the addition on the time and travel time for the arrival time

    """

        """Add together the departing time and the flytime to get arrival time"""

        calculate_arrival = date + timedelta(hours=time.hour, minutes=time.minute)
        return calculate_arrival

    def create_unique_id(self):

        """
        	creates a unique id.

            Args: none
        
            Returns: returns a random number between 0 and 5000

            note: we might want to check if an id already exists..., but we dont, so fingers crossed

    """

        """Use a random number as a unique id"""
        return random.randint(0, 5000)
