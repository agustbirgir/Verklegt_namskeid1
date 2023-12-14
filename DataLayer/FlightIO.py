import csv
from Models.Flight import Flight

class FlightIO:
    def __init__(self):
        self.file_name = "files/flights.csv"

    def add_flight(self, flight):
        """Add new flight to the csv file"""
        with open(self.file_name, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["startingPoint", "departureTime", "arrivalTime", "destination", "id"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow({'startingPoint': flight.startingPoint, 'departureTime': flight.departureTime,
                             'arrivalTime': flight.arrivalTime, 'destination': flight.destination,
                             'id': flight.id})

    def get_flight(self, id):
        """Return a specific flight"""
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                if (row["id"].strip() == str(id).strip()):
                    return Flight(row["startingPoint"].strip(), row["departureTime"].strip(), row["arrivalTime"].strip(), row["destination"].strip(), row["id"].strip())
        return ("Flight not found")

    def get_all_flights(self):
        """Return all flights"""
        ret_list = []
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                ret_list.append(Flight(row["startingPoint"], row["departureTime"], row["arrivalTime"], row["destination"], row["id"]))
        return ret_list
    
    def get_voyage_flights(self, id):
        """Return the two flights that are in a voyage"""
        ret_list = []
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                if (int(row["id"]) == int(id)):
                    ret_list.append(Flight(row["startingPoint"], row["departureTime"], row["arrivalTime"], row["destination"], row["id"]))
        return ret_list