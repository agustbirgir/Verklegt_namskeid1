class AircraftLL:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def add_aircraft(self, aircraft):

        """
        	adds an aircraft.

            Args: aircraft
        
            Returns: aircraft sent into datalayer

    """

        """Add aircraft to the csv file"""
        self.data_wrapper.add_aircraft(aircraft)

    def get_aircraft(self, name):

        """
        	gets aircraft

            Args: name
        
            Returns: uses aircraft name and pulls it from datalayer

    """

        """Return a specific aircraft"""
        return self.data_wrapper.get_aircraft(name)
    
    def get_all_aircraft(self):

        """
        	gets all aircraft.

            Args: none
        
            Returns: pulls all the aircraft in datalayer into ui layer

    """

        """Return all of the aircrafts"""
        return self.data_wrapper.get_all_aircrafts()