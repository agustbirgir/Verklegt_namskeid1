class EmployeeLL:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def add_employee(self, employee):

        """
        	adds employee.

            Args: employee

            Returns: sends employee into datalayer/database

    """

        """Takes in a customer object and forwards it to the data layer"""

        self.data_wrapper.add_employee(employee)

    def get_all_employees(self):

        """
        	gets all employees.

            Args: none
        
            Returns: list of employees

        """

        """Returns all employees"""

        return self.data_wrapper.get_all_employees()
    
    def get_all_pilots(self):

        """
        	gets all pilots.

            Args: none
        
            Returns: list of pilots

        """

        """Returns all pilots"""

        return self.data_wrapper.get_all_pilots()
    
    def get_all_attendants(self):

        """
        	gets all attendants.

            Args: none
        
            Returns: list of attendants

        """

        """Returns all attendants"""

        return self.data_wrapper.get_all_attendants()
    
    def find_employee_by_ssn(self, ssn):

        """
        	gets employee

            Args: ssn
        
            Returns: gets employee with matching ssn from datalayer

        """

        return self.data_wrapper.find_employee_by_ssn(ssn)
    
    def get_employee_by_name(self, name):

        """
        	gets employee

            Args: name
        
            Returns: gets employee with matching name from datalayer

        """

        return self.data_wrapper.get_employee_by_name(name)

    def update_employee(self, employee):

        """
        	updates employee

            Args: employee
        
            Returns: sends updated employee information into datalayer

        """

        self.data_wrapper.update_employee(employee)

    def employee_schedule_checker(self, date, working): #working is meant to say if we are checking for non working and working employees

        """
        	checks the schedule of employees on a specific date

            Args: date, working
        
            Returns: the working or non-working employess from data layer sent to ui layer

        """

        return self.data_wrapper.employee_schedule_checker(date, working)

    def get_schedule_of_employee(self, employee):

        """
        	gets schedule pf employee

            Args: employee, schedule_list
        
            Returns: gets employee schedule from the datalayer and sends it back to the ui layer in a suitable format

        """

        """Get the schedule of a given employee"""
        if employee is None:
            return []
        schedule_list = [item.strip("'") for item in employee.scheduled[1:-1].split(", ")]
        return schedule_list
    
    def sort_pilots_by_license(self):

        """
        	sorts the pilot list by aircraft license

            Args: pilots, aircraft, ret_list, aircraftLicense
        
            Returns: a sorted list of pilots and sends it into the ui layer

        """

        pilots = self.data_wrapper.get_all_pilots()
        aircraft = self.data_wrapper.get_all_aircrafts()
        ret_list = []
        for a in aircraft:
            for p in pilots:
                if p.aircraftLicense == a.name:
                    ret_list.append(p)
        return ret_list
    
    def get_pilots_by_license(self, license):

        """
        	gets pilots who have a matching license

            Args: license
        
            Returns: list of pilots who have the license that was provided as input, sent to the ui layer.

        """

        return self.data_wrapper.get_pilots_by_license(license)