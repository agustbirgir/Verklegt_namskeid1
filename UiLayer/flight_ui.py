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

    def add_voyage(self):
        
        destination = input("please enter voyage destination: ") #im not checking if its valid, ill have to add that later
        if destination == "b":
            break
        departure = input("please enter voyage departure: ")
        if departure == "b":
            break
    	arrival = input("please enter voyage arrival: ")
        if arrival == "b":
            break
        voyage = [] #this part should not be in the UI, but the rest of the stuff is either unfinished, or i dont understand how we add the voyages... 
        voyage.append({
                    'destination': destination, 
                    'departure': departure, 
                    'arrival': arrival, 
                    'pilots': [], 
                    'attendants': [], 
                    }) #im making this only for repeat voyage to theoretically work...
        self.logic_wrapper.add_voyage(voyage)


    def repeat_voyage(self):
        departure = input("please enter voyage departure: ")
        if departure == "b":
            break
    	arrival = input("please enter voyage arrival: ")
        if arrival == "b":
            break
        voyage = self.logic_wrapper.get_voyage(self, departure, arrival)
            
        if voyage == "Voyage not found":
            print("Invalid voyage")
            #break?
        
        repeat_time_frame = input("in how many days do you want to repeat this voyage?: ") #or whatever timeframe we are using, i will leave invalid due to conflicts for later i guess
        if repeat_time_frame == "b":
            break
        departure += repeat_time_frame
        arrival += repeat_time_frame
        voyage(1) = departure
        voyage(2) = arrival
        self.logic_wrapper.add_voyage(voyage)


        
        


