import csv
from Models.Aircraft import Aircraft

class AircraftIO: 
    def __init__(self):
        self.file_name = "files/aircrafts.csv"

    def add_aircraft(self, aircraft):
        """
        Add new aircraft to the aircrafts.csv file

        Args:
            aircraft (Aircraft): Aircraft to be written to the file

        Examples:
            >>> add_destination(Aircraft)
            This call writes all the attributes of the Aircraft object to the aircrafts.csv file
        """
        with open(self.file_name, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["name", "type", "manufacturer", "noOfPassenger"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow({'startingPoint': aircraft.name, 'departureTime': aircraft.type,
                             'destination': aircraft.manufacturer, 'arrivalTime': aircraft.noOfPassengers})

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
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if (row["name"] == name):
                    return Aircraft(row["name"], row["type"], row["manufacturer"], row["noOfPassengers"])
        return ("Flight not found")

    def get_all_aircrafts(self):
        """
        Returns all aircraft from aircraft.csv

        Returns:
            list of Aircraft: A list containing all aircrafty

        Examples:
            >>> get_all_aircraft()
            [Aircraft(Airbus A330,A330,Airbus SE,250), Aircraft(Boeing 737,747,Boeing Co,366)]
        """
        ret_list = []
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Aircraft(row["name"], row["type"], row["manufacturer"], row["noOfPassengers"]))
        return ret_list