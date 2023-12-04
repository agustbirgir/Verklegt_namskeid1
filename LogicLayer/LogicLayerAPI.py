from Models.Employee import Employee
from DataLayer.DataLayerAPI import DataLayerAPI

class LogicLayerAPI:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def create_employee(self, employee):
        """Takes in a customer object and forwards it to the data layer"""

        self.data_wrapper.create_employee(employee)

    def get_all_employees(self):
        return self.data_wrapper.get_all_employees()