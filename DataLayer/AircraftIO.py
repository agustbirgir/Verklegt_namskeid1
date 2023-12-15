import csv
from Models.Aircraft import Aircraft

class AircraftIO: 
    def __init__(self):
        self.file_name = "files/aircrafts.csv"

    def add_aircraft(self, aircraft):
        """Add new flight to the csv file"""
        with open(self.file_name, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["name", "type", "manufacturer", "noOfPassenger"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow({'startingPoint': aircraft.name, 'departureTime': aircraft.type,
                             'destination': aircraft.manufacturer, 'arrivalTime': aircraft.noOfPassengers})

    def get_aircraft(self, name):
        """Return a specific flight"""
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if (row["name"] == name):
                    return Aircraft(row["name"], row["type"], row["manufacturer"], row["noOfPassengers"])
        return ("Flight not found")

    def get_all_aircrafts(self):
        """Return all flights"""
        ret_list = []
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Aircraft(row["name"], row["type"], row["manufacturer"], row["noOfPassengers"]))
        return ret_list