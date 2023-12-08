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

    def display_employee(self):
        while True:

            command = input("search by [name] or [ssn]?")
            command = command.lower()

            if command =="name" or command =="n":
                
                name = input("what is the name of the employee?")
                if name == "back" or name == "b":
                    break
                employee = self.logic_wrapper.get_employee_by_name(name)
                if employee:
                    print(f"name: {employee.name}, profession: {employee.profession}")
                else:
                    print("name invalid")

            elif command =="ssn" or command =="s":

                ssn = input("what is the ssn of the employee?")
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



    def display_add_crew_to_voyage_UI(self): 
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
            print("All employees:")
            result = self.logic_wrapper.get_all_employees()
            employee_list = []
            for elem in result:
                print(f"name: {elem.name}, profession: {elem.profession}")
            while True:
                name = input("Enter the name of an employee to add (q to finish adding to voyage): ")
                if name == "q":
                    break
                else:
                    employee = self.logic_wrapper.get_employee_by_name(name)
                    if employee != None:
                        employee_list.append([employee.name, employee.profession])
                    else:
                        print("Employee does not exist, try again")
            self.logic_wrapper.voyage_add_employee(employee_list, id)
                

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
                self.display_add_crew_to_voyage_UI()
            elif command == "2":
                self.display_employee_list()
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

            if choice == "6":
                new_Status = input("Enter new Status: ")
                employee.status = new_Status
            
            if choice == "7":
                new_schedule = input("Enter the new schedule: ")
                employee.scheduled = new_schedule

            self.logic_wrapper.update_employee(employee)
        else:
            print("Employee not found.")



    