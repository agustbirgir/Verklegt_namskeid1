from Models.Destination import Destination

class DestinationLL:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def add_destination(self, destination):
        """Add destination based on location, distance and travel time"""
        self.data_wrapper.add_destination(destination)

    def get_destination(self, country):
        """Return a specific destination"""
        return self.data_wrapper.get_destination(country)
    
    def get_all_destinations(self):
        """Return all of the destinations"""
        return self.data_wrapper.get_all_destinations()