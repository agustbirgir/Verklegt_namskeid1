class DestinationLL:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def add_destination(self, destination):

        """
        	adds destination.

            Args: destination
        
            Returns: adds a destination into the datalayer

    """
        
        """Add destination based on location, distance and travel time"""
        self.data_wrapper.add_destination(destination)

    def get_destination(self, country):

        """
        	gets destination.

            Args: country
        
            Returns: gets destination from datalayer

    """

        """Return a specific destination"""
        return self.data_wrapper.get_destination(country)
    
    def get_all_destinations(self):

        """
        	gets all destinations.

            Args: none
        
            Returns: gets all existing destinations

    """

        """Return all of the destinations"""
        return self.data_wrapper.get_all_destinations()