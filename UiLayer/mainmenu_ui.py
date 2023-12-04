from LogicLayer.LogicLayerAPI import LogicLayerAPI
from Models.Employee import Employee
from LogicLayer.logic_wrapper import Logic_Wrapper
from UiLayer.crew_ui import Crew_UI
from UiLayer.flight_ui import Flight_UI


class MainMenuUI:
    def __init__(self):
        self.logic_wrapper = Logic_Wrapper()
    
    def manager_output(self):
        print("main menu")
        print("1. Flight manager")
        print("2. Crew manager")
        print("q to exit")

    def input_prompt(self):
        while True:
            self.manager_output()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "q":
                break
            elif command == "1":
                flight = Flight_UI(self.logic_wrapper)
                flight.input_prompt()
            elif command == "2":
                crew = Crew_UI(self.logic_wrapper)
                crew.input_prompt()
            else:
                print("Invalid input, try again")