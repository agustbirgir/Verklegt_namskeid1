from Models.Flight import Flight
import random
from datetime import datetime, timedelta

class FlightLL:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def add_flight(self, destination):
        """Add flight"""
        self.data_wrapper.add_flight(destination)

    def get_flight(self, country):
        """Return a specific flight"""
        return self.data_wrapper.get_flight(country)
    
    def get_all_flights(self):
        """Return all of the flights"""
        return self.data_wrapper.get_all_flights()
    
    def calculate_arrival_time(self, date, time):

        calculate_arrival = date + timedelta(hours=time.hour, minutes=time.minute)
        return calculate_arrival

    def create_unique_id(self):
        return random.randint(0, 5000)
