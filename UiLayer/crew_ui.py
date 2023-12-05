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
                    except NameLengthException:
                        print("Name was too long")
                    break
                e.profession = input("Enter the profession of the employee: ")
                #e.name = validate_name(input)
                self.logic_wrapper.add_employee(e)
            elif command == "5":
                pass
            else:
                print("Invalid input try again")


    def list_pilots(self)
        print(self.logic_wrapper.get_all_pilots())

    def list_attendants(self):
        print(self.logic_wrapper.get_all_attendants())