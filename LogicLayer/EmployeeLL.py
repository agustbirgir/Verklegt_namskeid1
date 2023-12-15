class EmployeeLL:
    def __init__(self, data_connection):
        """
        Constructor that establishes a connection to the data wrapper
        """
        self.data_wrapper = data_connection

    def add_employee(self, employee):
        """
        Add new employee to the employee.csv file

        Args:
            employee (Employee): Employee to be written to the file

        Examples:
            >>> add_employee(Employee)
            This call writes all the attributes of the Employee object to the employee.csv file
        """

        self.data_wrapper.add_employee(employee)

    def get_all_employees(self):
        """
        Returns all employees from employees.csv

        Returns:
            list of Employee: A list containing all employees

        Examples:
            >>> get_all_employees()
            [Employee(Siggi,Pilot,1214742314,2,3,a@g.is,4,['1010-11-10', '9999-11-11'],Boeing 737), Employee(Tommy Lee,Head Pilot,12345678,noatun 8,5812345,tommy@lee.com,1245678,[],Boeing 737)]
        """
        return self.data_wrapper.get_all_employees()
    
    def get_all_pilots(self):
        """
        Get all employees that are pilots in the employees.csv file

        Returns:
            list of Employee: Returns a list of all employees that are pilots

        Examples:
            >>> get_all_pilots()
            [Employee(Siggi,Pilot,1214742314,as 5,1247402,a@g.is,4,['1010-11-10', '9999-11-11'];Boeing 737), Employee(Tommy Lee;Head Pilot;12345678;noatun 8;5812345;tommy@lee.com;1245678;[];Boeing 737)]
            
        """

        return self.data_wrapper.get_all_pilots()
    
    def get_all_attendants(self):
        """
        Get all employees that are attendants in the employees.csv file

        Returns:
            list of Employee: Returns a list of all employees that are attendants

        Examples:
            >>> get_all_pilots()
            [Employee(Sigurjon,Head Flight Attendant,9374061953,Sævangur 8,5812345,agust@gmail.com,1234567,[],), Employee(Halli,Attendant,1047283940,Skaggaturn 12,5812345,Halli@gmail.com,8401640,[],)]
            
        """

        return self.data_wrapper.get_all_attendants()
    
    def find_employee_by_ssn(self, ssn):
        """
        Returns a specific employee from employees.csv based on social security number

        Args:
            ssn (string): Social security number of the employee

        Returns:
            employee (Employee): Employee to be found

        Examples:
            >>> find_employee_by_ssn(1090452944)
            Employee(Joi,Head Flight Attendant,1090452944,Sævangur 8,5812345,agust@gmail.com,1234567,[],)
            >>> get_flight(Thorshavn)
            Employee(Siggi,Pilot,1214742314,2,3,a@g.is,4,['1010-11-10', '9999-11-11'],Boeing 737)
        """

        return self.data_wrapper.find_employee_by_ssn(ssn)
    
    def get_employee_by_name(self, name):
        """
        Get employee in the employees.csv file by name

        Args:
            name (string): Employee name to be found
        
        Returns:
            employee (Employee): Returns an employee

        Examples:
            >>> get_employee_by_name(Siggi)
            Employee(Siggi,Pilot,1214742314,2,3,a@g.is,4,['1010-11-10', '9999-11-11'],Boeing 737)
            
        """

        return self.data_wrapper.get_employee_by_name(name)

    def update_employee(self, employee):
        """
        Take in an updated employee and update the employee in the employees.csv file

        Args:
            updated_employee (string): Employee to be updated in the csv file

        Examples:
            >>> update_employee(Employee())
            Updates the updated attributes of the employee to the csv file
            
        """

        self.data_wrapper.update_employee(employee)

    def employee_schedule_checker(self, date, working): #working is meant to say if we are checking for non working and working employees
        """
        Return all employees that are not working or are working on a certain date.

        Args:
            date (string): The date to be checked
            working (boolean): If employee is working or not

        Returns:
            list of Employee: Returns a list of all employees that are attendants

        Examples:
            >>> get_all_pilots()
            [Employee(Sigurjon,Head Flight Attendant,9374061953,Sævangur 8,5812345,agust@gmail.com,1234567,[],), Employee(Halli,Attendant,1047283940,Skaggaturn 12,5812345,Halli@gmail.com,8401640,[],)]
            
        """
        return self.data_wrapper.employee_schedule_checker(date, working)

    def get_schedule_of_employee(self, employee):

        """
        Gets schedule of employee

        Args: 
            employee (Employee): Get shedule of this employee
        
        Returns:
            Gets shcedule of employee

        Examples:
            >>> get_schedule_of_employee("Siggi")
            ['1010-11-10', '2023-12-15']

        """
        if employee is None:
            return []
        schedule_list = [item.strip("'") for item in employee.scheduled[1:-1].split(", ")]
        return schedule_list
    
    def sort_pilots_by_license(self):

        """
        Sorts the pilot list by aircraft license
        
        Returns:
            A list of pilots sorted by their aircraft types
        
        Examples:
            >>> sort_pilots_by_license()
            name: Siggi, license: Boeing 737
            name: Tommy Lee, license: Boeing 737
            name: Agust, license: Airbus A330
            name: Jonas, license: Airbus A330

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
        Gets pilots based on their license

        Args: 
            license (string): Name of the aircraft
        
            Returns: 
                List of pilots who have the license that was provided as input

            Examples:
                >>> get_pilots_by_license("Boeing 737")
                name: Siggi, profession: Pilot, license: Boeing 737
                name: Tommy Lee, profession: Head Pilot, license: Boeing 737
        """
        return self.data_wrapper.get_pilots_by_license(license)