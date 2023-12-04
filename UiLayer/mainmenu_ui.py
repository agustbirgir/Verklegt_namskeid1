from LogicLayer.LogicLayerAPI import LogicLayerAPI
from Models.Employee import Employee
from UiLayer.crew_ui import Crew_UI
from LogicLayer.logic_wrapper import Logic_Wrapper

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
                pass
            elif command == "2":
                menu = Crew_UI(self.logic_wrapper)
                menu.input_prompt()
                
            else:
                print("Invalid input try again")