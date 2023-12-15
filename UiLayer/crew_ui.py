from Models.Employee import Employee
from UiLayer.input_validators import *

class Crew_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def display_pilot_list(self):

        """
    Displays a list of pilots.

    Args: results, sorted_results
        
    Returns: printed list of pilots with proffessions

    Examples:   
        name: Tommy Lee | profession: Head Pilot
        name: Helgi | profession: Head Pilot

        Note: sorted by profession
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
    Displays a list of attendants.

    Args: results, sorted_results
        
    Returns: printed list of attendants with proffessions

    Examples:   
        name: Halli | profession: Attendant
        name: Joi | profession: Head Flight Attendant
   
        Note: sorted by profession
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
            Displays a list of employees.

            Args: results, sorted_results
                
            Returns: printed list of employees with proffessions

            Examples:   
                name: Halli | profession: Attendant
                name: Joi | profession: Head Flight Attendant
                name: Sigurjon | profession: Head Flight Attendant
                name: Tommy Lee | profession: Head Pilot

            Note: sorted by profession
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


    def display_employee_schedule_list(self, date, working):

        """
        Displays a list of employee schedules for a inserted date.

        Args:
            date (string): date to be checked
            working (boolean): If employee is working or not
                
        Returns: printed list of employees that are free on inserted day

        Raises: message if no employee found on date for specifications

        Examples:   
            >>> voyage_add_employee(1111-11-11, False)
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
            Displays a list of employee schedules for a inserted date.

            Args:
                date (string): Date to be searched
                
            Returns: 
                printed list of employees that are busy on inserted day

            Raises: 
                message if no employee found on date for specifications

            Examples:   
            voyage_add_employee(1111-11-11, True)
                name: Siggi, voyage destination: Nuuk
                name: Jonas, voyage destination: Nuuk
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
            Displays the UI and handles the menu for employee schedules.

            Args: working, date
                
            Returns: prints UI for the menu: 5.crew schedules

            Raises: goes back if b is pressed

            Note: q does nothing
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
                        self.display_employee_schedule_list(date, working)
            else:
                print("invalid command")

    def display_employee(self):

        """
            Displays the UI and takes in the ssn or name of employee to display.

            Args: command, name, employee, ssn, profession, homeAddress, gsmNumber, email, homePhone
                
            Returns: printed employee information

            Examples:   
===================================================================================
                            Database of employee
===================================================================================

                          Name: Siggi
                          Profession: Pilot
                          SSN: 1214742314
                          Home address: 2
                          Gsm number: 3
                          Email: a@g.is
                          HomePhone: 4

===================================================================================
                            [B]ack          [Q]uit
===================================================================================

            Note: 
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
            Displays the UI and handles the menu for the employee database.
            also functions as the listing function for list all pilots with specific aircraft license

            Args: command, aircraft_menu, aircraft_choice, pilots
        
            Raises: goes back if b is pressed and quits when q is pressed


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
                self.display_employee()
            elif command == "5":
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
            Displays the UI and handles the adding of crew to voyages.

            Args: mode, id, voyage, crew_list, voyages, selected_voyage_departure, aircraft_menu, aircraft_choice, new_crew_list, name, employee, schedule, voyage_date
                
            Returns: prints UI for the menu: 5.crew schedules

            Raises: value error if id is not int

            Note: mode 2 (fetching the next unmanned voyage) was redacted for: not working, and if you press it, you are forced to enter a correct ID
            """

        """Display the menu to add crew to voyage"""
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
                            print(employee.aircraftLicense)
                            self.logic_wrapper.update_employee(employee)
                        else:
                            print("Employeee {name} not found")
                    # Add the list of employees to the voyage
                    crew_list += new_crew_list
                    self.logic_wrapper.voyage_add_employee(crew_list, id)
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
                                    print("crewmember already assigned")
                                    in_voyage = True
                            # Otherwise we add the employee to the voyage
                            if not in_voyage:
                                new_crew_list.append(employee.name)
                    else:
                        print(f"Employee {name} does not exist, try again")
                
    

    def display_unmanned_voyages(self): # i dont know where to place the search and next operations of the unmanned puller
        """
            Displays a list of unmanned voyages.

            Args: subroutine, input
                
            Returns: list of unmanned voyages

            Example: marked for deletion or redaction, not used in any menu's
            """
        subroutine = "list"
        input = 0     #input is only for the search, to check if a voyage is empty, if we dont do that, we can remove it
        print(self.logic_wrapper.unmanned_voyage_fetcher(subroutine, input))
        #input("press any button to leave") # ok, so not sure how i am going to handle this part of the operation...
        

    def crew_manager_output(self):

        """
            Displays the UI element for the main menu of the crew manager   

            Note: this is just a single print command
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
            Acts as the main menu input prompt for the crew manager, also functions as the employee maker and updater

            Args: command, ssn, employee, profession, homeAddress, gsmNumber, email, homePhone, choice, scheduled, profession_menu, profession_choice, aircraft_menu, aircraft_choice, aircraftLicense
                
            Returns: employee information back into storage

            Raises: goes back if b is pressed, error if input is invalid

            Note: input prompt is heavy, command 3 and 4 have the code in them, command 1 and 2 do it in their own functions.
            """

        while True:
            self.crew_manager_output()
            command = input("Option: ")
            command = command.lower()
            if command == "b":
                break
            elif command == "1":                        #adding crew to a voyage
                self.display_add_crew_to_voyage_UI()    
            elif command == "2":                        #showing the database to list peeps
                self.display_employee_database_UI() 
            elif command == "3":                        #updating employee (im doing this so i can understand this better)
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
            elif command == "5":
                self.display_employees_working_status_UI()
            else:
                print("Invalid input try again")
                


    def display_update_employee_UI(self):

        """
            Displays the UI to update the employee

            Args: employee, choice, new_profession, new_home_address, new_gsm_number, new_email, new_home_phone
                
            Returns: updated epmloyee information into database

            Raises: error if employee not found

            Note: was this not done in the input_prompt function?
            """

        ssn = input("Enter the SSN of the employee to update: ")
        employee = self.logic_wrapper.find_employee_by_ssn(ssn)
        if employee:
            print("Select the field to update:")
            print("1. Profession\n2. Home Address\n3. GSM Number\n4. Email\n5. Home Phone \n6.    Scheduled")
            choice = input("Enter your choice [1-6]: ")

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

        
