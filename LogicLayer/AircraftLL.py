class AircraftLL:
    def __init__(self, data_connection):
        """
        Constructor that establishes a connection to the data wrapper
        """
        self.data_wrapper = data_connection

    def add_aircraft(self, aircraft):
        """
        Add new aircraft to the aircrafts.csv file

        Args:
            aircraft (Aircraft): Aircraft to be written to the file

        Examples:
            >>> add_aircraft(Aircraft)
            This call writes all the attributes of the Aircraft object to the aircrafts.csv file
        """
        self.data_wrapper.add_aircraft(aircraft)

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
        return self.data_wrapper.get_aircraft(name)
    
    def get_all_aircraft(self):
        """
        Returns all aircraft from aircraft.csv

        Returns:
            list of Aircraft: A list containing all aircrafty

        Examples:
            >>> get_all_aircraft()
            [Aircraft(Airbus A330,A330,Airbus SE,250), Aircraft(Boeing 737,747,Boeing Co,366)]
        """
        return self.data_wrapper.get_all_aircrafts()