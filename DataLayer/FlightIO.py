import csv
from Models.Flight import Flight

class FlightIO:
    def __init__(self):
        self.file_name = "files/flights.csv"

    def add_flight(self, flight):
        """Add new flight to the csv file"""
        with open(self.file_name, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["startingPoint", "departureTime", "destination", "arrivalTime", "id"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow({'startingPoint': flight.startingPoint, 'departureTime': flight.departureTime,
                             'destination': flight.destination, 'arrivalTime': flight.arrivalTime,
                             'id': flight.id})

    def get_flight(self, id):
        """Return a specific flight"""
        ret_list = []
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                if (row["id"] == id):
                    return Flight(row["startingPoint"], row["departureTime"], row["arrivalDestination"], row["arrivalTime"], row["id"])
        return ("Flight not found")

    def get_all_flights(self):
        """Return all flights"""
        ret_list = []
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                ret_list.append(Flight(row["startingPoint"], row["departureTime"], row["destination"], row["arrivalTime"], row["id"]))
        return ret_list