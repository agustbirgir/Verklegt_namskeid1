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



    def employee_schedule_checker(self, date, working): #working is meant to say if we are checking for non working and working employees
        employee = self.data_wrapper.get_all_employees_schedule() #this should help tell the differance
        ret_list = []
        if working == True:                                 #if you are searching for those who are working on a specific date
            for row in employee:
                schedule = Employee(row["sceduled"])

                for booking in employee.scheduled:          #takes in schedule list size to run through
                    if date == schedule[booking][1]:        #assuming scheduled is a touple (destination, date)
                        ret_list.append(Employee(row["name"], row["profession"]))   #we already have date in ui layer, no need to return it

        elif working == False:                              #if you are searching for those who are not working
            for row in employee:

                schedule = Employee(row["sceduled"])
                found_date = False

                for booking in employee.scheduled:          #goes through entire list for a match
                    if date == schedule[booking][1]:
                        found_date = True                   #this means the date exists in it

                if found_date == True:
                    ret_list.append(Employee(row["name"], row["profession"]))       #we already have date in ui layer, no need to return it
                    
        return ret_list