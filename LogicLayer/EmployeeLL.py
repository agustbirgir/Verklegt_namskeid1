from Models.Employee import Employee

class EmployeeLL:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def add_employee(self, employee):
        """Takes in a customer object and forwards it to the data layer"""

        self.data_wrapper.add_employee(employee)

    def get_all_employees(self):
        """Returns all employees"""

        return self.data_wrapper.get_all_employees()
    
    def get_all_pilots(self):
        """Returns all pilots"""

        return self.data_wrapper.get_all_pilots()
    
    def get_all_attendants(self):
        """Returns all attendants"""

        return self.data_wrapper.get_all_attendants()
    
    def find_employee_by_ssn(self, ssn):
        return self.data_wrapper.find_employee_by_ssn(ssn)
    
    def get_employee_by_name(self, name):
        return self.data_wrapper.get_employee_by_name(name)

    def update_employee(self, employee):
        self.data_wrapper.update_employee(employee)