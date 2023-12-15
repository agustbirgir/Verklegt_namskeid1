import csv
from Models.Destination import Destination

class DestinationIO:
    def __init__(self):
        self.file_name = "files/destinations.csv"

    def add_destination(self, destination):
        """
        Add new flight to the destinations.csv file

        Args:
            destination (Destination): Destination to be written to the file

        Examples:
            >>> add_destination(Destination)
            This call writes all the attributes of the Destination object to the destinations.csv file
        """
        with open(self.file_name, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["country", "city", "airport", "flytime", "distance", "contact", "contactNumber"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow({'country': destination.country, 'city': destination.city, 'airport': destination.airport, 'flytime': destination.flytime,
                             'distance': destination.distance, 'contact': destination.contact, 'contactNumber': destination.contactNumber})

    def get_destination(self, city):
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
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if (row["city"] == city):
                    return Destination(row["country"], row["city"], row["airport"], row["flytime"], row["distance"], row["contact"], row["contactNumber"])
        return None

    def get_all_destinations(self):
        """
        Returns all destinations from destinations.csv

        Returns:
            list of Destination: A list containing all destinations

        Examples:
            >>> get_all_destinations()
            [Destination(Greenland, Nuuk, Nuuk Airport, 2:40, 2000, john, 12345678, 01), Destination(Faroe Islands, Thorshavn, Vagar Airport, 5:30, 4500, joe, 13579864, 01)]
        """
        ret_list = []
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Destination(row["country"], row["city"], row["airport"], row["flytime"], row["distance"], row["contact"], row["contactNumber"]))
        return ret_list