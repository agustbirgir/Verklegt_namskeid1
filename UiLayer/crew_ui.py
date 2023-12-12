from Models.Employee import Employee
from UiLayer.input_validators import *

class Crew_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def display_pilot_list(self):
        result = self.logic_wrapper.get_all_pilots()
        for elem in result:
            print(f"name: {elem.name}, profession: {elem.profession}")

    def display_attendant_list(self):
        result = self.logic_wrapper.get_all_attendants()
        for elem in result:
            print(f"name: {elem.name}, profession: {elem.profession}")
    
    def display_employee_list(self):
        result = self.logic_wrapper.get_all_employees()
        for elem in result:
            print(f"name: {elem.name}, profession: {elem.profession}")

    def display_employee_schedule_list(self, date, working):
        result = self.logic_wrapper.employee_schedule_checker(date, working)
        if result == None:
            print("No employees found")
        else:
            for elem in result:
                print(f"name: {elem.name}, profession: {elem.profession}")

    def display_employees_working_status_UI(self):
        while True:
            print("1. List working employees at date")
            print("2. List non working employees at date")
            print("b to go back")
            working = input("Please enter an option: ")
            if working == "b":
                break
            elif working == "1":
                while True:
                    date = input("Please enter date (YYY-MM-DD) (b to go back): ")
                    print(date, validate_date_2(date))
                    if date == "b":
                        break
                    elif not validate_date_2(date):
                        print("Invalid date format. Please enter a date in YYYY-MM-DD format, try again")
                    else:
                        working = True
                        self.display_employee_schedule_list(date, working)
            elif working == "2":
                while True:
                    date = input("Please enter date (DD-MM-YYYY) (b to go back): ")
                    if date == "b":
                        break
                    elif not validate_date_2(date):
                        print("Invalid date format. Please enter a date in YYYY-MM-DD format, try again")
                    else:
                        working = False
                        self.display_employee_schedule_list(date, working)
            else:
                print("invalid command")

            

    def display_employee(self):
        while True:

            command = input("Search by [name] or [ssn] (b to go back): ")
            command = command.lower()

            if command =="name" or command =="n":

                name = input("Input the name of the employee: ")
                if name == "back" or name == "b":
                    break
                employee = self.logic_wrapper.get_employee_by_name(name)
                if employee:
                    print(f"\n Name: {employee.name}\n Profession: {employee.profession}\n SSN: {employee.homeAddress}\n Gsm number: {employee.gsmNumber}\n Email: {employee.email}\n HomePhone: {employee.homePhone}\n Status: {employee.status}\n Scheduled: {employee.scheduled}\n")
                else:
                    print("name invalid")

            elif command =="ssn" or command =="s":

                ssn = input("Input the ssn of the employee: ")
                if ssn == "back" or ssn == "b":
                    break
                employee = self.logic_wrapper.find_employee_by_ssn(ssn)
                if employee:
                    print(f"name: {employee.name}, profession: {employee.profession}")
                else:
                    print("name invalid")

            elif command == "back" or command == "b":
                break

            else:
                print("invalid command")

    def display_employee_database_UI(self):
        while True:
            print("Employee Database")
            print("1. List all employees")
            print("2. List all pilots")
            print("3. List all attendants")
            print("4. List specific employee")
            print("b to go back")
            command = input("Please pick an option: ")
            if command == "1":
                self.display_employee_list()
            elif command == "2":
                self.display_pilot_list()
            elif command == "3":
                self.display_attendant_list()
            elif command == "4":
                self.display_employee()
            elif command == "b":
                break
            else:
                print("Invalid input")

    def display_add_crew_to_voyage_UI(self): 
        """Display the menu to add crew to voyage"""
        while True:
            id = input("please enter voyage ID: ")
            try:
                id = int(id)
                break
            except ValueError:
                print("Invalid ID, please enter a number.")
        voyage = self.logic_wrapper.get_voyage(id)
            
        if voyage == "Voyage not found":
            print("Invalid input")
        else:
            # Voyage Found
            print("All NaN Air employees:")
            self.display_employee_list()
            all_employees = self.logic_wrapper.get_all_employees()
            voyages = self.logic_wrapper.get_all_voyages()
            crew_list = self.logic_wrapper.get_crew_of_voyage(voyage)
            selected_voyage_departure = self.logic_wrapper.get_flight(voyage.id).departureTime
            print("You picked voyage", voyage.id,"which departs at", selected_voyage_departure)
            print("Voyage", id,"crew:", crew_list)
            new_crew_list = []
            
            while True:
                name = input("Enter the name of an employee to add (q to finish adding to voyage): ")
                employee = self.logic_wrapper.get_employee_by_name(name) # Get selected employee

                if name == "q":
                    #if validate_voyage_crew(crew_list, all_employees): # Crew has to be valid for user to be able to quit
                        # Update the schedule of all assigned employees
                    for name in crew_list:
                        employee = self.logic_wrapper.get_employee_by_name(name)
                        schedule = self.logic_wrapper.get_schedule_of_employee(employee)
                        voyage_date = selected_voyage_departure.split(" ")[0]
                        schedule.append(voyage_date)
                        employee.scheduled = schedule
                        self.logic_wrapper.update_employee(employee)
                    # Add the list of employees to the voyage
                    crew_list += new_crew_list
                    self.logic_wrapper.voyage_add_employee(crew_list, id)
                    print(f"Successfully registered crew to voyage {id}")
                    break
                else:
                    if employee != None:
                        # Check if employee is already assigned to the selected voyage
                        if employee.name in crew_list:
                            print(name,"is already in currently selected voyage,",id,", try again")
                        else:
                            # Check if employee is already registered on a voyage on same date as selected voyage
                            in_voyage = False
                            for v in voyages:
                                v_departure = self.logic_wrapper.get_flight(v.id).departureTime
                                v_crew = self.logic_wrapper.get_crew_of_voyage(v)
                                if name in v_crew:
                                    if validate_if_registered_at_date(selected_voyage_departure, v_departure):
                                        print(f"{name}, is already in voyage {v.id}, at the same date {v_departure}, try again")
                                        in_voyage = True
                            # Otherwise we add the employee to the voyage
                            if not in_voyage:
                                new_crew_list.append(employee.name)
                    else:
                        print(f"Employee {name} does not exist, try again")
                

    def crew_manager_output(self):
        print("\nCrew Manager Menu")
        print("1. Assign crew to voyage")
        print("2. Employee database")
        print("3. Update employee")
        print("4. Register employee")
        print("5. Crew schedules")
        print("b to go back")

    def input_prompt(self):
        while True:
            self.crew_manager_output()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "b":
                break
            elif command == "1":                        #adding crew to a voyage
                self.display_add_crew_to_voyage_UI()    
            elif command == "2":                        #showing the database to list peeps
                self.display_employee_database_UI() 
            elif command == "3":                        #updating employee (im doing this so i can understand this better)
                ssn = input("Enter the ssn of the employee to update: ")
                employee = self.logic_wrapper.find_employee_by_ssn(ssn)
                if employee:
                    print("Current Employee Details:")
                    print(f"1. Profession: {employee.profession}")
                    print(f"2. Home Address: {employee.homeAddress}")
                    print(f"3. GSM Number: {employee.gsmNumber}")
                    print(f"4. Email: {employee.email}")
                    print(f"5. Home Phone: {employee.homePhone}")
                    print(f"6. Status: {employee.status}")
                    

                    choice = input("Select the field to update (1-7): ")
                    if choice == "1":
                        employee.profession = input("Enter new profession: ")
                    elif choice == "2":
                        employee.homeAddress = input("Enter new home address: ")
                    elif choice == "3":
                        employee.gsmNumber = input("Enter new GSM number: ")
                        while not validate_phone(employee.gsmNumber):
                            print("Invalid GSM number. Please try again.")
                            employee.gsmNumber = input("Enter new GSM number: ")
                    elif choice == "4":
                        employee.email = input("Enter new email address: ")
                        while not validate_email(employee.email):
                            print("Invalid email. Please try again.")
                            employee.email = input("Enter new email address: ")
                    elif choice == "5":
                        employee.homePhone = input("Enter new home phone (optional): ")
                        if employee.homePhone and not validate_phone(employee.homePhone):
                            print("Invalid home phone number. Leaving it empty.")
                            employee.homePhone = ''
                    elif choice == "6":
                        employee.status = input("Enter new status: ")
                    
                    employee.scheduled = []
                        

                    self.logic_wrapper.update_employee(employee)
                    print("Employee information updated successfully.")
                else:
                    print("Employee not found with the provided SSN.")

            elif command == "4":                                            #making a new employee
                e = Employee()
                while True:
                    e.name = input("Enter the name of the employee: ")
                    try:
                        validate_name(e.name)
                        break
                    except NameLengthException:
                        print("Name was too long")
                
                profession_menu = {#Profession
                    "1": "Pilot",
                    "2": "Flight attendant",
                    "3": "Head pilot",
                    "4": "Head flight attendant"
                }
                print("Select the Profession of the employee")
                for key, value in profession_menu.items():
                    print(f"{key}. {value}")

                while True:
                    profession_choice = input("Enter the profession of the employee: ")
                    if profession_choice in profession_menu:
                        e.profession = profession_menu[profession_choice]
                        break
                    else:
                        print("Wrong input has been chosen")#End

                #SSN
                e.ssn = input("Enter the Social security number: ")
                while not validate_ssn(e.ssn):
                    print("Invalid ssn. it must be 8 digit!")
                    e.ssn = input("Enter the Social security number: ")
                #End

                #Homeaddress
                e.homeAddress = input("Enter the home address of the employee: ")
                #End

                #GSM 
                e.gsmNumber = input("Enter the Phone number: ")
                while not validate_phone(e.gsmNumber):
                    print("Wrong input has been chosen")
                    e.gsmNumber = input("Enter the Phone number: ")
                #End

                #Email
                e.email = input("Enter the Email of the employee: ")
                while not validate_email(e.email):
                    print("wrong input need a @ or wrong input")
                    e.email = input("Enter the Email of the employee: ")
                #End

                #Homephone
                e.homePhone = input("input the homephone of the employee(optinal): ")
                if e.homePhone and not validate_phone(e.homePhone):
                    print("Input has been left empty")
                    e.homePhone = ''
                #End

                #Status
                e.status = 0
                
                #End

                #Schedule 
                e.scheduled = []
                #End
                self.logic_wrapper.add_employee(e)
            elif command == "5":
                self.display_employees_working_status_UI()
            else:
                print("Invalid input try again")

    # Inside Crew_UI class

    def display_update_employee_UI(self):
        ssn = input("Enter the SSN of the employee to update: ")
        employee = self.logic_wrapper.find_employee_by_ssn(ssn)
        if employee:
            print("Select the field to update:")
            print("1. Profession\n2. Home Address\n3. GSM Number\n4. Email\n5. Home Phone\n6. Status\n7.    Scheduled")
            choice = input("Enter your choice [1-7]: ")

            if choice == "1":
                new_profession = input("Enter new profession: ")
                employee.profession = new_profession

            if choice == "2":
                new_home_address = input("Enter new Home Address: ")
                employee.homeaddress = new_home_address

            if choice == "3":
                new_gsm_number = input("Enter the new Gsm Number: ")
                employee.gsmNumber = new_gsm_number

            if choice == "4":
                new_email = input("Enter new the new Home address: ")
                employee.email = new_email
            
            if choice == "5":
                new_home_phone = input("Enter the new Home phone: ")
                employee.homePhone = new_home_phone
            
            self.logic_wrapper.update_employee(employee) #schedule should remain unchanged
        else:
            print("Employee not found.")


