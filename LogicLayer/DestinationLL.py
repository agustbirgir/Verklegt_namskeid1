class DestinationLL:
    def __init__(self, data_connection):
        """
        Constructor that establishes a connection to the data wrapper
        """
        self.data_wrapper = data_connection

    def add_destination(self, destination):
        """
        Add new flight to the destinations.csv file

        Args:
            destination (Destination): Destination to be written to the file

        Examples:
            >>> add_destination(Destination)
            This call writes all the attributes of the Destination object to the destinations.csv file
        """
        self.data_wrapper.add_destination(destination)

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
        return self.data_wrapper.get_destination(country)
    
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
        return self.data_wrapper.get_all_destinations()