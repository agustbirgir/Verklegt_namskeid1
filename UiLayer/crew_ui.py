from Models.Employee import Employee
from UiLayer.input_validators import *

class Crew_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def crew_manager_output(self):
        print("Crew Manager Menu")
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
            elif command == "1":
                pass
            elif command == "2":
                print("e")
                result = self.logic_wrapper.get_all_employees()
                for elem in result:
                    print(f"name: {elem.name}, profession: {elem.profession}")
            elif command == "3":
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
                    print(f"7. Scheduled: {employee.scheduled}")

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
                    elif choice == "7":
                        employee.scheduled = input("Enter new scheduled date (YYYY-MM-DD): ")
                        while not validate_date(employee.scheduled):
                            print("Invalid date format. Please enter a date in YYYY-MM-DD format.")
                            employee.scheduled = input("Enter new scheduled date (YYYY-MM-DD): ")

                    self.logic_wrapper.update_employee(employee)
                    print("Employee information updated successfully.")
                else:
                    print("Employee not found with the provided SSN.")

            elif command == "4":
                e = Employee()
                while True:
                    e.name = input("Enter the name of the employee: ")
                    try:
                        validate_name(e.name)
                        break
                    except NameLengthException:
                        print("Name was too long")
                
                profession_menu = {#Profession
                    "1": "Flugmaður",
                    "2": "Flugþjónn",
                    "3": "Flugstjóri",
                    "4": "Yfirflugstjóri"
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
                e.status = input("Enter the digit of the employee")
                while not e.status.isdigit():
                    print("Invalid status. Please enter an integer.")
                    e.status = input("Enter the digit of the employee ")
                    e.status = int(e.status)
                #End

                #Schedule 
                e.scheduled = input("Enter the scheduled date of the employee (YYYY-MM-DD): ")
                while not validate_date(e.scheduled):
                    print("Invalid date format. Please enter a date in YYYY-MM-DD format.")
                    e.scheduled = input("Enter the scheduled date of the employee (YYYY-MM-DD): ")
                #End
                self.logic_wrapper.add_employee(e)
            elif command == "5":
                pass
            else:
                print("Invalid input try again")

    # Inside Crew_UI class

    def update_employee(self):
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

            if choice == "6":
                new_Status = input("Enter new Status: ")
                employee.status = new_Status
            
            if choice == "7":
                new_schedule = input("Enter the new schedule: ")
                employee.scheduled

            self.logic_wrapper.update_employee(employee)
        else:
            print("Employee not found.")


    def list_pilots(self):
        print(self.logic_wrapper.get_all_pilots())

    def list_attendants(self):
        print(self.logic_wrapper.get_all_attendants())

    def add_crew_to_voyage(self): #this assumes you are inside the menu for it already, i spent too long trying to do both at the same time, so im simplifying it
        #this is for the process of selecting a specific voyage and then adding the crew
        #maybe we could split this?
        #this also assumes we are selecting a empty voyage
        command1 = input("please enter voyage departure: ")
        if command1 == "b":
            break
    	command2 = input("please enter voyage arrival: ")
        if command2 == "b":
            break
        voyage = self.logic_wrapper.get_voyage(self, command1, command2)
            
        if voyage == "Voyage not found":
            print("Invalid input")
            #break?
        else:
            #kominn með voyage, assignum þá inn í það
            in_manning = True
            pilots = []
            attendants = []
            first_run = True
            while in_manning == True:
                print("if you are finished, write done")
                crew = input("please insert crew (pilot or attendant) ssn: ") 
                
                if crew == "done":
                    if size(pilots) => 2 and size(attendants) =>1:
                        print("valid crew assignment, registering crew to flight")
                        in_manning == False
                        self.logic_wrapper.voyage_add_pilot(voyage, pilots)
                        self.logic_wrapper.voyage_add_attendant(voyage, attendants)
                        
                    else:
                        if first_run == True:
                            print("voyage assignment cancelled")
                            in_manning == False
                        else:
                            exit_prompt = input("invalid manning, would you like to [c]ontinue or [q]uit?")
                            if exit_prompt == "q":
                                in_manning == False

                first_run = False
                Employee = self.logic_wrapper.find_employee_by_ssn(crew)

                if Employee(row["profession"]) == "Pilot":
                    pilots.append(Employee["name"])

                elif Employee(row["profession"]) == "Attendant":
                    attendants.append(Employee["name"])
