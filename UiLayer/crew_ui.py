from Models.Employee import Employee
from UiLayer.input_validators import *

class Crew_UI:
    def __init__(self, logic_connection):
        """
        Constructor that establishes a connection to the logic wrapper
        """
        self.logic_wrapper = logic_connection

    def display_pilot_list(self):

        """
        Displays a list of all pilots.
            
        Returns: 
            Printed list of pilot names and professions

        Examples:  
            >>> display_pilot_list() 
            name: Tommy Lee | profession: Head Pilot
            name: Helgi | profession: Head Pilot
        """


        result = self.logic_wrapper.get_all_pilots()
        sorted_result = sorted(result, key=lambda employee: employee.profession)

        print("===================================================================================")
        for elem in sorted_result:
            print(f""" name: {elem.name} | profession: {elem.profession}  """)
        print("""
===================================================================================
                    [B]ack          [Q]uit   
===================================================================================
            """)

    def display_attendant_list(self):

        """
        Displays a list of all attendants.
            
        Returns: Printed list of attendant names and professions

        Examples: 
            >>> display_attendant_list()
            name: Halli | profession: Attendant
            name: Joi | profession: Head Flight Attendant
        """

        result = self.logic_wrapper.get_all_attendants()
        sorted_result = sorted(result, key=lambda employee: employee.profession)

        print("===================================================================================")
        for elem in sorted_result:
            print(f""" name: {elem.name} | profession: {elem.profession}  """)
        print("""
===================================================================================
                    [B]ack          [Q]uit   
===================================================================================
            """)
    def display_employee_list(self):

        """
            Displays a list of all employees.
                
            Returns: 
                Printed list of employee names and professions

            Examples:   
                >>> display_employee_list()
                name: Halli | profession: Attendant
                name: Joi | profession: Head Flight Attendant
                name: Sigurjon | profession: Head Flight Attendant
                name: Tommy Lee | profession: Head Pilot
            """

        result = self.logic_wrapper.get_all_employees()
        sorted_result = sorted(result, key=lambda employee: employee.profession)

        print("===================================================================================")
        for elem in sorted_result:
            print(f""" name: {elem.name} | profession: {elem.profession}  """)
        print("""
===================================================================================
                    [B]ack          [Q]uit   
===================================================================================
            """)


    def display_employees_not_working_list(self, date, working):

        """
        Displays a list of employees not working on a specific date.

        Args:
            date (string): date to be checked
            working (boolean): If employee is working or not
                
        Returns: 
            Printed list of employees that are not working on the date

        Examples:   
            >>> display_employees_not_working_list(1111-11-11)
            name: Siggi
            name: Tommy Lee   
        """
        result = self.logic_wrapper.employee_schedule_checker(date, working)
        if result == None:
            print("No employees found")
        else:
            print(f"""
===================================================================================
                      List of non-working Employees
===================================================================================""")
            for elem in result:
                print(f"""
                      name: {elem.name}""")
            print("""===================================================================================
                  [B]ack            [Q]uit
===================================================================================
            """)
    
    def display_employees_working_list(self, date, working):
        """
        Displays a list of employees working on a specific date.

        Args:
            date (string): date to be checked
            working (boolean): If employee is working or not
                
        Returns: 
            Printed list of employees that are working on the date

        Examples:   
            >>> display_employees_not_working_list(1111-11-11)
            name: Siggi, destination: Nuuk
            name: Tommy Lee, destination: Kulusuk
        """

        result = self.logic_wrapper.employee_schedule_checker(date, working)
        voyages = self.logic_wrapper.get_all_voyages()
        if result == None:
            print("No employees found")
        ret_list = []
        name_list = []
        for elem in result: # Find the voyages of all the working employees
            for v in voyages:
                v_crew = self.logic_wrapper.get_crew_of_voyage(v)
                if elem.name in v_crew and elem.name not in name_list:
                    name_list.append(elem.name)
                    ret_list.append([elem.name, v.id])

        print("""
===================================================================================
                    Working list of all employees
===================================================================================
        """)
        for elem in ret_list:
            print(f"Name: {elem[0]}")
            print(f"Voyage destination: {self.logic_wrapper.get_flight(elem[1]).destination}")
        print("""
===================================================================================
                  [B]ack            [Q]uit
===================================================================================""")


    def display_employees_working_status_UI(self):

        """
        Displays the menu for picking to list working or non working employees

        Example:
            >>> display_employees_working_status_UI()
            ===================================================================================
            ===================================================================================
                            
                            1. List working employees at date
                            2. List non working employees at date

            ===================================================================================
                            [B]ack            [Q]uit
            ===================================================================================
        """

        while True:
            print(f"""
===================================================================================
===================================================================================
                  
                1. List working employees at date
                2. List non working employees at date

===================================================================================
                  [B]ack            [Q]uit
===================================================================================
            """)

            working = input("Please enter an option: ")
            if working.lower() == "b":
                break
            elif working.lower() == "q":
                exit(0)
            elif working == "1":
                while True:

                    date = input("Please enter date (YYYY-MM-DD) (b to go back): ")
                    if date.lower() == "b":
                        break
                    if date.lower() == "q":
                        exit(0)
                    elif not validate_date_2(date):
                        print("Invalid date format. Please enter a date in YYYY-MM-DD format, try again")
                    else:
                        working = True
                        self.display_employees_working_list(date, working)
            elif working == "2":
                while True:
                    date = input("Please enter date (YYYY-MM-DD) (b to go back): ")
                    if date == "b":
                        break
                    elif date.lower() == "q":
                        exit(0)
                    elif not validate_date_2(date):
                        print("Invalid date format. Please enter a date in YYYY-MM-DD format, try again")
                    else:
                        working = False
                        self.display_employees_not_working_list(date, working)
            else:
                print("invalid command")

    def display_update_employee_UI(self):
        """
        Displays the UI for updating an employee

        Example:
            >>> display_update_employee_UI()
            Enter the ssn of the employee to update or 'b' to quit:
        """
        while True:
            ssn = input("Enter the ssn of the employee to update or 'b' to quit: ")
            if ssn.lower() == 'b':
                break

            employee = self.logic_wrapper.find_employee_by_ssn(ssn)
            if employee:
                while True:
                    print(f"""
===================================================================================
        Current Employee Details of {employee.name} 
===================================================================================

            1. Profession: {employee.profession}
            2. Home Address: {employee.homeAddress}
            3. GSM Number: {employee.gsmNumber}
            4. Email: {employee.email}
            5. Home Phone: {employee.homePhone}
                
===================================================================================
            [B]ack          [Q]uit    
===================================================================================

        """)

                    choice = input("Select the field to update (1-5): ")
                    if choice.lower() == 'q':
                        exit(0)
                    elif choice.lower() == 'b':
                        break
                    if choice == "1":
                        profession_menu = {#Profession
                            "1": "Pilot",
                            "2": "Head Pilot",
                            "3": "Flight Attendant",
                            "4": "Head Flight Attendant"
                        }
                        print()
                        print("Professions:")
                        for key, value in profession_menu.items():
                            print(f"{key}. {value}")

                        while True:
                            profession_choice = input("Enter the profession of the employee: ")
                            if profession_choice in profession_menu:
                                employee.profession = profession_menu[profession_choice]
                                break
                            else:
                                print("Wrong input, try again")

                        if employee.aircraftLicense == '':
                            if profession_menu[profession_choice] == "Pilot" or profession_menu[profession_choice] == "Head Pilot":
                                aircraft_menu = {
                                    "1": "Boeing 737",
                                    "2": "Airbus A330",
                                }
                                print()
                                print("Aircraft types:")
                                for key, value in aircraft_menu.items():
                                    print(f"{key}. {value}")
                                while True:
                                    aircraft_choice = input(f"Select the aircraft license of the pilot: ")
                                    if aircraft_choice in aircraft_menu:
                                        e.aircraftLicense = aircraft_menu[aircraft_choice]
                                        break
                                    else:
                                        print("Wrong input, try again")
                        
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
        
                    employee.scheduled = []
            

                    self.logic_wrapper.update_employee(employee)
                    print("Employee information updated successfully.")
            else:
                print("Employee not found with the provided SSN.")

    def display_pilots_specific_license_UI(self):
        """
        Displays the UI for listing pilots with a specific license

        Example:
            >>> display_specific_employee_UI()
            Select the name of the aircraft (b to go back)
        """
        aircraft_list = self.logic_wrapper.get_all_aircraft()
        for elem in aircraft_list:
            print(f"name: {elem.name}, type: {elem.type}")
        while True:
            aircraft_name = input(f"Select the name of the aircraft (b to go back): ")
            aircraft = self.logic_wrapper.get_aircraft(aircraft_name)
            if aircraft_name.lower() == "b":
                break
            elif aircraft != None:
                print(f"You picked: {aircraft.name}")
                break
            else:
                print("Wrong input, try again")
        if aircraft_name.lower() != "b":
            pilots = self.logic_wrapper.get_pilots_by_license(aircraft.name)
            for elem in pilots:
                print(f"name: {elem.name}, profession: {elem.profession}, license: {elem.aircraftLicense}")

    def display_specific_employee_UI(self):

        """
        Displays the UI for searching for an employee
            
        Example:
            >>> display_specific_employee_UI()
            Search by [name] or [ssn] (b to go back): 
        """

        while True:
            command = input("Search by [name] or [ssn] (b to go back): ").lower()

            if command in ["name", "n"]:
                name = input("Input the name of the employee: ")
                if name.lower() in ['q', 'b']:
                    if name.lower() == 'q':
                        exit(0)
                    break
                employee = self.logic_wrapper.get_employee_by_name(name)
                if employee:
                    print(f"""
===================================================================================
                            Database of employee
===================================================================================

                          Name: {employee.name}
                          Profession: {employee.profession}
                          SSN: {employee.ssn}
                          Home address: {employee.homeAddress}
                          Gsm number: {employee.gsmNumber}
                          Email: {employee.email}
                          HomePhone: {employee.homePhone}

===================================================================================
                            [B]ack          [Q]uit
===================================================================================
                    """)
                else:
                    print("Name invalid")

            elif command in ["ssn", "s"]:
                ssn = input("Input the ssn of the employee: ")
                if ssn.lower() in ['q', 'b']:
                    if ssn.lower() == 'q':
                        exit(0)
                    break
                employee = self.logic_wrapper.find_employee_by_ssn(ssn)
                if employee:
                    print(f"""
===================================================================================
                            Database of employee
===================================================================================

                          Name: {employee.name}
                          Profession: {employee.profession}
                          SSN: {employee.ssn}
                          Home address: {employee.homeAddress}
                          Gsm number: {employee.gsmNumber}
                          Email: {employee.email}
                          HomePhone: {employee.homePhone}

===================================================================================
                            [B]ack          [Q]uit
===================================================================================
                    """)
                else:
                    print("SSN invalid")

            elif command in ["back", "b"]:
                break

            else:
                print("Invalid command")



    def display_employee_database_UI(self):

        """
        Displays the UI and handles the menu for listing various employees

        Example:
            >>> display_employee_database_UI()
            ===================================================================================
                        Employee Database
            ===================================================================================

                            1. List all employees
                            2. List all pilots
                            3. List all attendants
                            4. List specific employee
                            5. List pilots with specific aircraft license
                            6. List pilots sorted by license
            ===================================================================================
                                [B]ack          [Q]uit
            ===================================================================================

            """

        while True:
            print(f"""
===================================================================================
                        Employee Database
===================================================================================

                  1. List all employees
                  2. List all pilots
                  3. List all attendants
                  4. List specific employee
                  5. List pilots with specific aircraft license
                  6. List pilots sorted by license
===================================================================================
                    [B]ack          [Q]uit
===================================================================================

            """)

            command = input("Please pick an option: ")
            if command == "1":
                self.display_employee_list()
            elif command == "2":
                self.display_pilot_list()
            elif command == "3":
                self.display_attendant_list()
            elif command == "4":
                self.display_specific_employee_UI()
            elif command == "5":
                self.display_pilots_specific_license_UI()
            elif command == "6":
                result = self.logic_wrapper.sort_pilots_by_license()
                for elem in result:
                    print(f"name: {elem.name}, license: {elem.aircraftLicense}")
            elif command.lower() == "b":
                break
            elif command.lower() == "q":
                exit(0)
            else:
                print("Invalid input")

    def display_add_crew_to_voyage_UI(self): 
        """
        Displays the UI for adding crew to a voyage.

        Example:
            >>> display_add_crew_to_voyage_UI()
            please enter voyage ID (b to go back)
        """

        while True:
            id = input("please enter voyage ID (b to go back): ")
            if id.lower()== "b":
                break
            try:
                id = int(id)
                break
            except ValueError:
                print("Invalid ID, please enter a number.")

        if id == "b":
            print()
        else:
            # Voyage Found
            voyage = self.logic_wrapper.get_voyage(id)

            voyages = self.logic_wrapper.get_all_voyages()
            crew_list = self.logic_wrapper.get_crew_of_voyage(voyage)
            aircraft_list = self.logic_wrapper.get_all_aircraft()
            selected_voyage_departure = self.logic_wrapper.get_flight(voyage.id).departureTime
            print("You picked voyage", voyage.id,"which departs at", selected_voyage_departure)
            print("Voyage", id,"crew:", crew_list)

            # Register flight
            print()
            print("Aircraft types:")
            for elem in aircraft_list:
                print(f"name: {elem.name}, type: {elem.type}")
            while True:
                aircraft_name = input(f"Select the name of the aircraft: ")
                aircraft = self.logic_wrapper.get_aircraft(aircraft_name)
                if aircraft != None:
                    voyage.aircraft = aircraft_name
                    print(f"You picked: {aircraft.name}")
                    break
                else:
                    print("Wrong input, try again")

            # Register employees
            print("All NaN Air employees:")
            self.display_employee_list()
            new_crew_list = [] # Make sure only newly registered crew gets their schedule updated with the voyage departure date
            
            while True:
                name = input("Enter the name of an employee to add (q to finish adding to voyage): ")
                employee = self.logic_wrapper.get_employee_by_name(name) # Get selected employee

                if name == "q":
                    #if validate_voyage_crew(crew_list, all_employees): # Crew has to be valid for user to be able to quit
                        # Update the schedule of all assigned employees
                    for name in new_crew_list:
                        employee = self.logic_wrapper.get_employee_by_name(name)
                        if employee is not None:
                            employee = self.logic_wrapper.get_employee_by_name(name)
                            schedule = self.logic_wrapper.get_schedule_of_employee(employee)
                            voyage_date = selected_voyage_departure.split(" ")[0]
                            schedule.append(voyage_date)
                            employee.scheduled = schedule
                            self.logic_wrapper.update_employee(employee)
                        else:
                            print("Employeee {name} not found")
                    # Add the list of employees to the voyage
                    crew_list += new_crew_list
                    self.logic_wrapper.voyage_add_employees(crew_list, id)
                    print(f"Successfully registered crew to voyage {id}")
                    break
                else:
                    if employee != None:
                        if employee.name in crew_list: # Check if employee is already assigned to the selected voyage
                            print(f"{name}, is already in currently selected voyage {id}, try again")
                        elif not validate_pilot(employee, voyage.aircraft):
                            print(f"The pilot {name} doesn't have the license for the voyage aircraft {voyage.aircraft}, try again")
                        else:
                            # Check if employee is already registered on a voyage on same date as selected voyage
                            in_voyage = False
                            for v in voyages:
                                v_departure = self.logic_wrapper.get_flight(v.id).departureTime
                                v_crew = self.logic_wrapper.get_crew_of_voyage(v)
                                if name in v_crew and in_voyage == False:
                                    if validate_if_registered_at_date_voyage(selected_voyage_departure, v_departure):
                                        print(f"{name}, is already in voyage {v.id}, at the same date {v_departure}, try again")
                                        in_voyage = True
                                if name in new_crew_list and in_voyage == False:
                                    print("crew member already assigned")
                                    in_voyage = True
                            # Otherwise add the employee to the voyage
                            if not in_voyage:
                                new_crew_list.append(employee.name)
                    else:
                        print(f"Employee {name} does not exist, try again")

    def display_register_employee_UI(self):
        """
        Displays the UI for registering an employee

        Example:
            >>> display_register_employee_UI()
            Enter the name of the employyee:
        """
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
            "2": "Head Pilot",
            "3": "Flight Attendant",
            "4": "Head Flight Attendant"
        }
        print()
        print("Professions:")
        for key, value in profession_menu.items():
            print(f"{key}. {value}")

        while True:
            profession_choice = input("Enter the profession of the employee: ")
            if profession_choice in profession_menu:
                e.profession = profession_menu[profession_choice]
                break
            else:
                print("Wrong input, try again")
        if profession_menu[profession_choice] == "Pilot" or profession_menu[profession_choice] == "Head Pilot":
            aircraft_menu = {
                "1": "Boeing 737",
                "2": "Airbus A330",
            }
            print()
            print("Aircraft types:")
            for key, value in aircraft_menu.items():
                print(f"{key}. {value}")
            while True:
                aircraft_choice = input(f"Select the aircraft license of the pilot: ")
                if aircraft_choice in aircraft_menu:
                    e.aircraftLicense = aircraft_menu[aircraft_choice]
                    break
                else:
                    print("Wrong input, try again")
        else:
            e.aircraftLicense = '' 

        #SSN
        e.ssn = input("Enter the Social security number: ")
        while not validate_ssn(e.ssn):
            print("Invalid ssn, it must be 10 digits")
            e.ssn = input("Enter the Social security number: ")

        #Homeaddress
        e.homeAddress = input("Enter the home address of the employee: ")

        #GSM 
        e.gsmNumber = input("Enter the phone number: ")
        while not validate_phone(e.gsmNumber):
            print("Wrong input has been chosen")
            e.gsmNumber = input("Enter the Phone number: ")

        #Email
        e.email = input("Enter the email of the employee: ")
        while not validate_email(e.email):
            print("wrong input need a @ or wrong input")
            e.email = input("Enter the Email of the employee: ")

        #Homephone
        e.homePhone = input("input the homephone of the employee (optional): ")
        if e.homePhone and not validate_phone(e.homePhone):
            print("Homephone not registered.")
            e.homePhone = ''

        #Schedule 
        e.scheduled = []

        # Add employee
        self.logic_wrapper.add_employee(e)

    def crew_manager_output(self):

        """
        Displays the UI element for the main menu of the crew manager   

        Example:
            >>> crew_manager_output()
            ===================================================================================
                        Crew Manager Menu
            ===================================================================================
                        
                                1. Assign crew to voyage
                                2. Employee database
                                3. Update employee
                                4. Register employee
                                5. Crew schedules

            ===================================================================================
                                            [B]ack      
            ===================================================================================
        """

        print("""\n
===================================================================================
                        Crew Manager Menu
===================================================================================
            
                    1. Assign crew to voyage
                    2. Employee database
                    3. Update employee
                    4. Register employee
                    5. Crew schedules

===================================================================================
                                [B]ack      
===================================================================================
        """)

    def input_prompt(self):

        """
        Displays the main menu input prompt for the crew manager

        Example:
            >>> input_prompt()
            ===================================================================================
                        Crew Manager Menu
            ===================================================================================
                        
                                1. Assign crew to voyage
                                2. Employee database
                                3. Update employee
                                4. Register employee
                                5. Crew schedules

            ===================================================================================
                                            [B]ack      
            ===================================================================================
            Enter an option:
        """

        while True:
            self.crew_manager_output()
            command = input("Enter an option: ")
            command = command.lower()
            if command == "b":
                break
            elif command == "1":
                self.display_add_crew_to_voyage_UI()    
            elif command == "2":
                self.display_employee_database_UI() 
            elif command == "3":
                self.display_update_employee_UI()
            elif command == "4":
                self.display_register_employee_UI()
            elif command == "5":
                self.display_employees_working_status_UI()
            else:
                print("Invalid input try again")

        
