import csv
from Models.Employee import Employee

class EmployeeIO:
    def __init__(self):
        self.file_name = "files/employees.csv"

    def get_all_employees(self):
        """
        Returns all employees from employees.csv

        Returns:
            list of Employee: A list containing all employees

        Examples:
            >>> get_all_employees()
            [Employee(Siggi,Pilot,1214742314,2,3,a@g.is,4,['1010-11-10', '9999-11-11'],Boeing 737), Employee(Tommy Lee,Head Pilot,12345678,noatun 8,5812345,tommy@lee.com,1245678,[],Boeing 737)]
        """
        ret_list = []
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                ret_list.append(Employee(row["name"], row["profession"]))
        return ret_list
    
    def add_employee(self, employee):
        """
        Add new employee to the employee.csv file

        Args:
            employee (Employee): Employee to be written to the file

        Examples:
            >>> add_employee(Employee)
            This call writes all the attributes of the Employee object to the employee.csv file
        """
        with open(self.file_name, 'a', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["name", "profession", "ssn","homeAddress", "gsmNumber", "email", "homePhone", "scheduled", "aircraftLicense"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
            if csvfile.tell() == 0:
                writer.writeheader()

            writer.writerow({'name': employee.name, 'profession': employee.profession, 
                             'ssn': employee.ssn, 'homeAddress': employee.homeAddress, 
                             'gsmNumber': employee.gsmNumber, 'email': employee.email, 
                             'homePhone': employee.homePhone, 'scheduled': employee.scheduled,
                             'aircraftLicense': employee.aircraftLicense})


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
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                if row["ssn"] == ssn:
                    return Employee(row["name"], row["profession"], row["ssn"], row["homeAddress"], row["gsmNumber"], row["email"], row["homePhone"], row["scheduled"], row["aircraftLicense"])
        return None
    
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
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                if row["name"] == name:
                    return Employee(row["name"], row["profession"], row["ssn"], row["homeAddress"], row["gsmNumber"], row["email"], row["homePhone"], row["scheduled"], row["aircraftLicense"])
        return None
    
    def get_pilots_by_license(self, license):
        """
        Get pilots in the employees.csv file by their aircraft license

        Args:
            license (string): Name of aircraft
        
        Returns:
            list of Employee: Returns a list of pilots

        Examples:
            >>> get_pilots_by_license(Boeing 737)
            Employee(Siggi,Pilot,1214742314,2,3,a@g.is,4,['1010-11-10', '9999-11-11'],Boeing 737)
            
        """
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            ret_list = []
            for row in reader:
                if row["aircraftLicense"] == license:
                    ret_list.append(Employee(row["name"], row["profession"], row["ssn"], row["homeAddress"], row["gsmNumber"], row["email"], row["homePhone"], row["scheduled"], row["aircraftLicense"]))
        return ret_list

    def update_employee(self, updated_employee):
        """
        Take in an updated employee and update the employee in the employees.csv file

        Args:
            updated_employee (string): Employee to be updated in the csv file

        Examples:
            >>> update_employee(Employee())
            Updates the updated attributes of the employee to the csv file
            
        """
        employees = []

        with open(self.file_name, 'r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                if row["ssn"] == updated_employee.ssn:
                # Update the employee's information
                    employees.append({
                    'name': updated_employee.name, 
                    'profession': updated_employee.profession, 
                    'ssn': updated_employee.ssn, 
                    'homeAddress': updated_employee.homeAddress, 
                    'gsmNumber': updated_employee.gsmNumber, 
                    'email': updated_employee.email, 
                    'homePhone': updated_employee.homePhone, 
                    'scheduled': updated_employee.scheduled,
                    'aircraftLicense': updated_employee.aircraftLicense
                    })
                else:
                    employees.append(row)

        with open(self.file_name, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ["name", "profession", "ssn", "homeAddress", "gsmNumber", "email", "homePhone", "scheduled", "aircraftLicense"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=";")
            writer.writeheader()
            for emp in employees:
                writer.writerow(emp)

    def get_all_pilots(self):
        """
        Get all employees that are pilots in the employees.csv file

        Returns:
            list of Employee: Returns a list of all employees that are pilots

        Examples:
            >>> get_all_pilots()
            [Employee(Siggi,Pilot,1214742314,as 5,1247402,a@g.is,4,['1010-11-10', '9999-11-11'];Boeing 737), Employee(Tommy Lee;Head Pilot;12345678;noatun 8;5812345;tommy@lee.com;1245678;[];Boeing 737)]
            
        """
        ret_list = []
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                if row["profession"] == "Pilot" or row["profession"] == "Head Pilot":
                    ret_list.append(Employee(row["name"], row["profession"], row["ssn"], row["homeAddress"], row["gsmNumber"], row["email"], row["homePhone"], row["scheduled"], row["aircraftLicense"]))
        return ret_list

    def get_all_attendants(self):
        """
        Get all employees that are attendants in the employees.csv file

        Returns:
            list of Employee: Returns a list of all employees that are attendants

        Examples:
            >>> get_all_pilots()
            [Employee(Sigurjon,Head Flight Attendant,9374061953,Sævangur 8,5812345,agust@gmail.com,1234567,[],), Employee(Halli,Attendant,1047283940,Skaggaturn 12,5812345,Halli@gmail.com,8401640,[],)]
            
        """
        ret_list = []
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            for row in reader:
                if row["profession"] == "Attendant" or row["profession"] == "Head Flight Attendant":
                    ret_list.append(Employee(row["name"], row["profession"]))
        return ret_list
    
    def employee_schedule_checker(self, date, working):
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
        ret_list = []
        with open(self.file_name, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=";")
            if working:
                for row in reader:
                    schedule_list = [item.strip("'") for item in row["scheduled"][1:-1].split(", ")]
                    for emp_sched in schedule_list:
                        if str(emp_sched) == str(date):
                            ret_list.append(Employee(row["name"], row["profession"]))
            else:
                for row in reader:
                    schedule_list = [item.strip("'") for item in row["scheduled"][1:-1].split(", ")]
                    is_working_at_date = False
                    for emp_sched in schedule_list:
                        if emp_sched == date:
                            is_working_at_date = True
                        if not is_working_at_date:
                            ret_list.append(Employee(row["name"]))
        return ret_list