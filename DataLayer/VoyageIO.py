import csv
from Models.Voyage import Voyage


class VoyageIO:
    def __init__(self):
        self.file_name = "files/voyages.csv"

    def add_voyage(self, voyage):
        """Create new voyage"""
        print(voyage)
        with open(self.file_name, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["departureFlight", "arrivalFlight", "crew", "id"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames,delimiter=";")
            if csvfile.tell() == 0:
                writer.writeheader()
                
            writer.writerow({'departureFlight': voyage.departureFlight, 'arrivalFlight': voyage.arrivalFlight, 
                             'crew': voyage.crew, 'id': voyage.id})

    def get_voyage(self, id):
        """Return a specific voyage"""
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                if int(row["id"]) == int(id):
                    return Voyage(row["departureFlight"], row["arrivalFlight"], row["crew"], row["id"])
        return None

    def get_all_voyages(self):
        ret_list = []
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                ret_list.append(Voyage(row["departureFlight"], row["arrivalFlight"], row["crew"], row["id"]))
        return ret_list
    
    def voyage_add_flight(self, flight, id):
        """Add employees to a voyage"""
        rows = []
        with open(self.file_name, mode='r') as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                rows.append(row)

        for row in rows:
            if int(row['id']) == id:
                row['aircraft'] = str(flight)

        with open(self.file_name, mode='w', newline='') as file:
            fieldnames = ["departureFlight", "arrivalFlight", "crew", "id", "aircraft"]
            writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=";")
            writer.writeheader()
            writer.writerows(rows)
    
    def voyage_add_employee(self, employeeList, id):
        """Add employees to a voyage"""
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
    
    def voyage_add_attendant(self, attendant):
        """Add attendant to a voyage"""
        attendantList = []

        with open(self.file_name, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                attendantList.append(row)

        for row in attendantList:
            if row['name'] == attendant.name:
                row['pilots'].append(attendant.name) 

        with open(self.file_name, mode='w', newline='') as file:
            fieldnames = ["departureFlight", "arrivalFlight", "pilots", "attendants", "aircraft"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write headers
            writer.writeheader()

            # Write updated data
            writer.writerows(attendantList)

    def get_all_flights(self):
        flights = []
        with open(self.file_name, mode='r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file, delimiter=';')
            for row in csv_reader:
                flights.append(row)
        return flights

    def get_flight_by_id(self, flight_id):
        all_flights = self.get_all_flights()
        for flight in all_flights:
            if flight['departureFlight'] == str(flight_id):
                return flight
        return flight