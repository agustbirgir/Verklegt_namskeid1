from Models.Voyage import Voyage
from Models.Employee import Employee
from UiLayer.input_validators import *

class Flight_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def flight_manager_output(self):
        print("1. Create voyage")
        print("2. List all Flight info")
        print("3. Show flight info per week")
        print("b to go back")

    def create_voyage(self):
        print("Creating a new voyage...")
        departure_flight = input("Enter departure flight: ")
        arrival_flight = input("Enter arrival flight: ")
        pilots = input("Enter pilots (comma separated): ").split(',')
        attendants = input("Enter attendants (comma separated): ").split(',')

        # Create Voyage object
        voyage = Voyage(departure_flight, arrival_flight, pilots, attendants)

        # Add voyage through Logic_Wrapper
        self.logic_wrapper.add_voyage(voyage)
        print("Voyage created successfully.")


    def input_prompt(self):
        while True:
            self.flight_manager_output()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "b":
                break
            elif command == "1":
                self.create_voyage()
            elif command == "2":
                pass
            elif command == "3":
                pass
            else:
                print("Invalid input, try again")
