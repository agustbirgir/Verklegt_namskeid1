import csv
from Models.Voyage import Voyage

class VoyageIO:
    def __init__(self):
        self.file_name = "Verklegt_namskeid1/files/voyages.csv"

    def add_voyage(self, voyage):
        """Add destination based on location, distance and travel time"""
        with open(self.file_name, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["departureFlight", "arrivalFlight", "pilots", "attendants"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow()

    def get_voyage(self, departure, arrival):
        """Return a specific destination"""
        ret_list = []
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if (row["departureFlight"] == departure and row["arrivalFlight"] == arrival):
                    return Voyage(row["departureFlight"], row["arrivalFlight"], row["pilots"], row["attendants"])
        return ("Voyage not found")

    def get_all_voyages(self):
        ret_list = []
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                ret_list.append(Voyage(row["departureFlight"], row["arrivalFlight"]), row["pilots"], row["attendants"])
        return ret_list
    
<<<<<<< HEAD
    def voyage_add_pilot(self, ,voyage, pilot):
        """Add a pilot to a voyage"""
        ret_list = []
=======
    def voyage_add_pilot(self, voyage, pilot):
        """Add a pilot to a voyage"""
        pilots = []

<<<<<<< HEAD
>>>>>>> e603436 (test)
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            fieldnames = ["departureFlight", "arrivalFlight", "pilots", "attendants"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if csvfile.tell() == 0:
                writer.writeheader()
            
<<<<<<< HEAD
            
            writer.writerow({'departureFlight': voyage.departureFlight, 'arrivalFlight': voyage.arrivalFlight,
                             })
=======
            for row in writer:
                pilots.append(row)
            
            writer.writerow({'departureFlight': voyage.departureFlight, 'arrivalFlight': voyage.arrivalFlight,
                             'pilots': })
>>>>>>> e603436 (test)

    def voyage_add_attendant(self, voyage):
        """Add an attendant to a voyage"""
        ret_list = []
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
=======
        with open(self.file_name, mode='r') as file:
            reader = csv.DictReader(file)
>>>>>>> 748767d (Bætti add to voyage)
            for row in reader:
                pilots.append(row)

        for row in pilots:
            if row['name'] == pilot.name:
                row['pilots'].append(pilot.name) 

        with open(self.file_name, mode='w', newline='') as file:
            fieldnames = ["departureFlight", "arrivalFlight", "pilots", "attendants"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write headers
            writer.writeheader()

            # Write updated data
            writer.writerows(pilots)

    def voyage_add_attendant(self, attendant):
        """Add a pilot to a voyage"""
        attendants = []

        with open(self.file_name, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                attendants.append(row)

        for row in attendant:
            if row['name'] == attendant.name:
                row['pilots'].append(attendant.name) 

        with open(self.file_name, mode='w', newline='') as file:
            fieldnames = ["departureFlight", "arrivalFlight", "pilots", "attendants"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write headers
            writer.writeheader()

            # Write updated data
            writer.writerows(attendant)