import ast

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

    def employee_schedule_checker(self, date, working): #working is meant to say if we are checking for non working and working employees
        return self.data_wrapper.employee_schedule_checker(date, working)

    def get_schedule_of_employee(self, employee):
        """Get the schedule of a given employee"""
        if employee is None:
            return []
        schedule_list = [item.strip("'") for item in employee.scheduled[1:-1].split(", ")]
        return schedule_list