import csv
from Models.Voyage import Voyage


class VoyageIO:
    def __init__(self):
        """
        Constructor that establishes a connection to the csv file
        """
        self.file_name = "files/voyages.csv"

    def add_voyage(self, voyage):
        """
        Add new voyage to the voyage.csv file

        Args:
            voyage (Voyage): Voyage to be written to the file

        Examples:
            >>> add_voyage(Voyage)
            This call writes all the attributes of the Voyage object to the voyages.csv file
        """
        print(voyage)
        with open(self.file_name, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["departureFlight", "arrivalFlight", "crew", "id"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=";")
            if csvfile.tell() == 0:
                writer.writeheader()
                
            writer.writerow({'departureFlight': voyage.departureFlight, 'arrivalFlight': voyage.arrivalFlight, 
                             'crew': voyage.crew, 'id': voyage.id})

    def get_voyage(self, id):
        """
        Returns a specific voyage from voyages.csv based on id

        Args:
            id (string): The id of the voyage

        Returns:
            Voyage: returns a voyage

        Examples:
            >>> get_voyage(2)
            Voyage(2, 2, ['Siggi', 'Helgi', 'Jonas', 'Halli'], 2, Airbus A330)
            >>> get_flight(3891)
            Voyage(3891, 3891, [], 3891, Boeing 737)
        """
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                if int(row["id"]) == int(id):
                    return Voyage(row["departureFlight"], row["arrivalFlight"], row["crew"], row["id"])
        return None

    def get_all_voyages(self):
        """
        Returns all flights from flights.csv

        Returns:
            list of Voyage: A list containing all voyages

        Examples:
            >>> get_all_voyages()
            [Voyage(2, 2, ['Siggi', 'Helgi', 'Jonas', 'Halli'], 2, Airbus A330), Voyage(3891, 3891, [], 3891, Boeing 737)]
        """
        ret_list = []
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                ret_list.append(Voyage(row["departureFlight"], row["arrivalFlight"], row["crew"], row["id"]))
        return ret_list
    
    def voyage_add_flight(self, aircraft, id):
        """
        Add new aircraft to a voyage

        Args:
            aircraft (string): Name of the aircraft to be added
            id (string): Id of the voyage for the aircraft to be added

        Examples:
            >>> voyage_add_flight("Boeing 737", "2")
            This call writes the flight "Boeing 737" as the aircraft for the voyage with ID 2 
            
        """
        rows = []
        with open(self.file_name, mode='r') as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                rows.append(row)

        for row in rows:
            if int(row['id']) == id:
                row['aircraft'] = str(aircraft)

        with open(self.file_name, mode='w', newline='') as file:
            fieldnames = ["departureFlight", "arrivalFlight", "crew", "id", "aircraft"]
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=";")
            writer.writeheader()
            writer.writerows(rows)
    
    def voyage_add_employees(self, employeeList, id):
        """
        Add employees to a voyages crew

        Args:
            employeeList (list): List of employees to be added
            id (string): Id of the voyage for the employees to be added

        Examples:
            >>> voyage_add_employees(['John', 'Chad'], "2")
            This call adds John and Chad to the crew of the voyage with ID 2 
            
        """
        rows = []
        with open(self.file_name, mode='r') as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                rows.append(row)

        for row in rows:
            if int(row['id']) == id:
                row['crew'] = str(employeeList)

        with open(self.file_name, mode='w', newline='') as file:
            fieldnames = ["departureFlight", "arrivalFlight", "crew", "id", "aircraft"]
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=";")
            writer.writeheader()
            writer.writerows(rows)