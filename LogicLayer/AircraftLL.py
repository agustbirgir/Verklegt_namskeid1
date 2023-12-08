from Models.Aircraft import Aircraft

class AircraftLL:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def add_aircraft(self, aircraft):
        """Add aircraft to the csv file"""
        self.data_wrapper.add_aircraft(aircraft)

    def get_aircraft(self, name):
        """Return a specific aircraft"""
        return self.data_wrapper.get_aircraft(name)
    
    def get_all_aircraft(self):
        """Return all of the aircrafts"""
        return self.data_wrapper.get_all_aircrafts()