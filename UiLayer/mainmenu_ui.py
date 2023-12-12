from LogicLayer.logic_wrapper import Logic_Wrapper
from UiLayer.crew_ui import Crew_UI
from UiLayer.flight_ui import Flight_UI


class MainMenuUI:
    def __init__(self):
        self.logic_wrapper = Logic_Wrapper()
        self.ascii_art = r"""
__|__
\___/                       
 | |
 | |
_|_|______________
        /|\           _   _                 _   _                _____    _____
      */ | \*        | \ | |      /\       | \ | |      /\      |_   _|  |  __ \              
      / -+- \        |  \| |     /  \      |  \| |     /  \       | |    | |__) |
  ---o--(_)--o---    | . ` |    / /\ \     | . ` |    / /\ \      | |    |  _  /
    /  0 " 0  \      | |\  |   / ____ \    | |\  |   / ____ \    _| |_   | | \ \
  */     |     \*    \_| \_|  /_/    \_\   \_| \_|  /_/    \_\  |_____|  |_|  \_\
  /      |      \         
*/       |       \*
===================================================================================
                        CHOOSE WHICH MANAGER TO USE
===================================================================================

                1. Flight manager
                2. Crew manager

===================================================================================
                                [Q]uit
===================================================================================
        """

    def manager_output(self):
        print(self.ascii_art)

    def input_prompt(self):
        while True:
            self.manager_output()
            command = input("Pick an option: ")
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
