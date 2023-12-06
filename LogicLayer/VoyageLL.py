from Models.Employee import Employee

class VoyageLL:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def add_voyage(self, voyage):
        """Create a new voyage"""
        self.data_wrapper.add_voyage(voyage)

    def get_voyage(self, departure, arrival):
        """Return a specific voyage"""
        self.data_wrapper.get_voyage(departure, arrival)

    def get_all_voyages(self):
        """Return all voyages"""
        self.data_wrapper.get_all_voyages()

    def voyage_add_pilot(self, voyage, pilot):
        """Add a pilot to a voyage"""
        self.data_wrapper.voyage_add_pilot(voyage, pilot)

    def voyage_add_attendant(self, voyage):
        """Add an attendant to a voyage"""
<<<<<<< HEAD
        self.data_wrapper.voyage_add_attendant(voyage)
=======
        self.data_wrapper.voyage_add_attendant(voyage)
        
>>>>>>> 08dfe28 (þarf að klara að bæta pilots i lista)
