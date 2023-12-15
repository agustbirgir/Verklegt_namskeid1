import csv
from Models.Flight import Flight

class FlightIO:
    def __init__(self):
        self.file_name = "files/flights.csv"

    def add_flight(self, flight):
        """
        Add new flight to the flights.csv file

        Args:
            flight (Flight): Flight to be written to the file

        Examples:
            >>> add_flight(Flight)
            This call writes all the attributes of the Flight object to the flights.csv file
        """
        with open(self.file_name, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["startingPoint", "departureTime", "arrivalTime", "destination", "id"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow({'startingPoint': flight.startingPoint, 'departureTime': flight.departureTime,
                             'arrivalTime': flight.arrivalTime, 'destination': flight.destination,
                             'id': flight.id})

    def get_flight(self, id):
        """
        Returns a specific flight from flights.csv based on id

        Args:
            id (string): The id of the flight

        Returns:
            Flight: Returns a flight

        Examples:
            >>> get_flight(1891)
            Flight(Keflavik, 1010-11-10 10:20:00, 1010-11-10 13:10:00, Nuuk, 1891, NA021)
            >>> get_flight(1891)
            Flight(Keflavik, 1990-10-12 10:11:00, 1990-10-12 12:51:00, Nuuk, 2067, NA034)
        """
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                if (int(row["id"]) == int(id)):
                    return Flight(row["startingPoint"], row["departureTime"], row["arrivalTime"], row["destination"], row["id"], row["flightNumber"])
        return ("Flight not found")

    def get_all_flights(self):
        """
        Returns all flights from flights.csv

        Returns:
            list of Flight: A list containing all flights

        Examples:
            >>> get_all_flights()
            [Flight(Keflavik, 1010-11-10 10:20:00, 1010-11-10 13:10:00, Nuuk, 1891, NA021), Flight(Keflavik, 1990-10-12 10:11:00, 1990-10-12 12:51:00, Nuuk, 2067, NA034)]
        """
        ret_list = []
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                ret_list.append(Flight(row["startingPoint"], row["departureTime"], row["arrivalTime"], row["destination"], row["id"], row["flightNumber"]))
        return ret_list
    
    def get_voyage_flights(self, id):
        """
        Return the two flights that are in a voygae

        Returns:
            list of Flight: A list containing two flights

        Examples:
            >>> get_all_flights()
            [Flight(Keflavik, 1010-11-10 10:20:00, 1010-11-10 13:10:00, Nuuk, 1891, NA021), Flight(Keflavik, 1990-10-12 10:11:00, 1990-10-12 12:51:00, Nuuk, 2067, NA022)]
        """
        ret_list = []
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                if (int(row["id"]) == int(id)):
                    ret_list.append(Flight(row["startingPoint"], row["departureTime"], row["arrivalTime"], row["destination"], row["id"]))
        return ret_list