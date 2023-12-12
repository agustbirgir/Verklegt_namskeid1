class VoyageLL:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def add_voyage(self, voyage):
        """Create a new voyage"""
        self.data_wrapper.add_voyage(voyage)

    def get_voyage(self, id):
        """Return a specific voyage"""
        return self.data_wrapper.get_voyage(id)

    def get_all_voyages(self):
        """Return all voyages"""
        return self.data_wrapper.get_all_voyages()

    def voyage_add_employee(self, employeeList, id):
        """Add an employee to a voyage"""
        self.data_wrapper.voyage_add_employee(employeeList, id)
    
    def get_crew_of_voyage(self, voyage):
        """Get the crew of a specific voyage"""
        crew_list = [item.strip("'") for item in voyage.crew[1:-1].split(", ")]
        return crew_list