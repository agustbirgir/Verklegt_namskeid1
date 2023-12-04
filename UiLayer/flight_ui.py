from LogicLayer.LogicLayerAPI import LogicLayerAPI
from Models.Employee import Employee
from UiLayer.input_validators import *

class Flight_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def flight_manager_output(self):
        print("1. Create voyage")
        print("2. List all destinations")
        print("3. Show flight info per week")
        print("b to go back")

    def input_prompt(self):
        while True:
            self.flight_manager_output()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "b":
                break
            elif command == "1":
                pass
            elif command == "2":
                pass
            elif command == "3":
                pass
            else:
                print("Invalid input, try again")