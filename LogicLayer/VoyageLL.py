from Models.Employee import Employee

class VoyageLL:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def add_voyage(self, voyage):
        """Create a new voyage"""
        self.data_wrapper.add_voyage(voyage)

    def get_voyage(self, id):
        """Return a specific voyage"""
        self.data_wrapper.get_voyage(id)

    def get_all_voyages(self):
        """Return all voyages"""
        self.data_wrapper.get_all_voyages()

    def voyage_add_employee(self, employeeList, id):
        """Add a pilot to a voyage"""
        self.data_wrapper.voyage_add_employee(employeeList, id)