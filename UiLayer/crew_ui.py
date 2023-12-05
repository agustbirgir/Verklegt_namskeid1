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
                pass
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