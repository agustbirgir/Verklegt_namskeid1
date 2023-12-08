import csv
from Models.Destination import Destination

class DestinationIO:
    def __init__(self):
        self.file_name = "files/destinations.csv"

    def add_destination(self, destination):
        """Add destination based on location, distance and travel time"""
        with open(self.file_name, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["country", "city", "airport", "flytime", "distance", "contact", "contactNumber"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow({'country': destination.country, 'city': destination.city, 'airport': destination.airport, 'flytime': destination.flytime,
                             'distance': destination.distance, 'contact': destination.contact, 'contactNumber': destination.contactNumber})

    def get_destination(self, city):
        """Return a specific destination"""
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if (row["city"] == city):
                    return Destination(row["country"], row["city"], row["airport"], row["flytime"], row["distance"], row["contact"], row["contactNumber"])
        return None

    def get_all_destinations(self):
        ret_list = []
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Destination(row["country"], row["city"], row["airport"], row["flytime"], row["distance"], row["contact"], row["contactNumber"]))
        return ret_list