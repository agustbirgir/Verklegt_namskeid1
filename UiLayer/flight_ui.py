from Models.Flight import Flight
from Models.Destination import Destination
from Models.Voyage import Voyage
from UiLayer.input_validators import *

class Flight_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection

    def flight_manager_UI(self):
        print("1. Create voyage")
        print("2. List all destinations")
        print("3. Show flight info per week")
        print("b to go back")

    def display_destination_list(self):
        destinations = self.logic_wrapper.get_all_destinations()
        for dest in destinations:
            print(f"country: {dest.country}, city: {dest.city}, airport: {dest.airport}, flytime: {dest.flytime}, distance: {dest.distance}, contact: {dest.contact}, contact number: {dest.contactNumber}")

    def display_add_voyage_UI(self):
        destination_menu = {
                    "1": "Nuuk",
                    "2": "Kulusuk",
                    "3": "Torshofn",
                    "4": "Tingwall",
                    "5": "Longyearbyen"
                }
        departure=""
        while True:
            print()
            print("Destinations:")
            for key, value in destination_menu.items():
                print(f"{key}. {value}")
            command = input("Please pick the arrival destination (q to quit): ")
            if command == "q":
                break
            elif int(command) < 0 or int(command) > 5:
                print("Invalid input, try again")
            else:
                print(destination_menu[command])
                destination = self.logic_wrapper.get_destination(destination_menu[command])
                if destination != None:
                    print(f"Selected destination: country: {destination.country}, city: {destination.city}, airport: {destination.airport}")
                    break
                else:
                    print("Destination does not exist, try again")
        if command != "q":
            id = self.logic_wrapper.create_unique_id()
            while True:
                print()
                departure = input(f"Please pick the departure time from Keflavik to {destination.city} (DD-MM-YYYY,HH:MM) (q to quit): ")
                validate, departureDate = validate_voyage_date(departure)
                if departure == "q":
                    break
                elif validate == False:
                    print("Wrong format for input, try again")
                elif validate == True:

                    flytime = datetime.strptime(destination.flytime,'%H:%M')
                    arrivalDate = self.logic_wrapper.calculate_arrival_time(departureDate, flytime)

                    #destinationInfo = [destination.country,destination.city,destination.airport,destination.flytime,
                                       #destination.distance,destination.contact,destination.contactNumber]
                    # ef ekki hægt að referenca Destination object úr csv skránni þá nota þennann lista, sjáum til
                    departureFlight = Flight()
                    departureFlight.startingPoint = "Keflavik" # Starting point is always keflavik for now in A requirements
                    departureFlight.departureTime = departureDate
                    departureFlight.arrivalTime = arrivalDate
                    departureFlight.destination = destination
                    departureFlight.id = id
                    print("Successfully registered")
                    # User could cancel, so we dont write the flight to the csv file until he has registered the second fligh as well.
                    break
        if departure != "q" and command != "q":
            while True:
                print()
                departure2 = input(f"Please pick the departure time from {destination.city} to Keflavik (DD-MM-YYYY,HH:MM) (q to quit): ")
                validate, departureDate2 = validate_voyage_date(departure2)
                validate_if_after = validate_if_date_after(departure2, departure) # Doesnt quite work
                if command == "q":
                    break
                elif validate == False:
                    print("Wrong format for input, try again")
                elif validate_if_after == False:
                    print("Arrival date must be set after the departure date, try again")
                elif validate == True:

                    flytime2 = datetime.strptime(destination.flytime,'%H:%M')
                    arrivalDate2 = self.logic_wrapper.calculate_arrival_time(departureDate2, flytime2)
                    #destinationInfo = [destination.country,destination.city,destination.airport,destination.flytime,
                                       #destination.distance,destination.contact,destination.contactNumber]
                    # ef ekki hægt að referenca Destination object úr csv skránni þá nota þennann lista, sjáum til
                    arrivalFlight = Flight()
                    arrivalFlight.startingPoint = destination.city 
                    arrivalFlight.departureTime = departureDate2
                    arrivalFlight.arrivalTime = arrivalDate2
                    arrivalFlight.destination = self.logic_wrapper.get_destination("Keflavik") # Keflavik is always the arrival destination in A requirements, change in B requirements
                    arrivalFlight.id = id

                    # Add the departure flight and arrival flight to the voyage
                    voyage = Voyage()
                    voyage.departureFlight = arrivalFlight
                    voyage.arrivalFlight = arrivalFlight
                    voyage.crew = ""
                    voyage.id = id

                    self.logic_wrapper.add_flight(arrivalFlight)
                    self.logic_wrapper.add_flight(departureFlight)
                    self.logic_wrapper.add_voyage(voyage)
                    
                    print(f"\nSuccessfully registered voyage, ID: {id}")
                    print(f"\nDeparture from Keflavik to {destination.city}:", departureDate)
                    print(f"Arrival date from Keflavik to {destination.city}:", arrivalDate)
                    print(f"\nDeparture from {destination.city} to Keflavik:", departureDate2)
                    print(f"Arrival date from {destination.city} to Keflavik:", arrivalDate2)
                    print()

                    break

    def display_repeat_voyage_UI(self):
        while True:
            while True:
                id = input("please enter voyage ID: ")
                try:
                    id = int(id)
                    break
                except ValueError:
                    print("Invalid ID, please enter a number.")
            get_voyage = self.logic_wrapper.get_voyage(id)
            print("get voyage:", get_voyage)
            if get_voyage != None:
                print(f"You picked voyage: {id}")
                repeat_date = input("Please input the date and time for when you want to repeat this voyage (DD-MM-YYYY,HH:MM) (q to quit): ")
                if repeat_date == "q":
                    break
                else:
                    id = self.logic_wrapper.create_unique_id()
                    new_voyage = Voyage()
                    new_voyage.departureFlight = get_voyage.departureFlight
                    new_voyage.arrivalFlight = get_voyage.arrivalFlight
                    new_voyage.crew = get_voyage.crew
                    new_voyage.id = id
                    self.logic_wrapper.add_voyage(new_voyage)
            else:
                print("Voyage not found")


    def input_prompt(self):
        while True:
            self.flight_manager_UI()
            command = input("Enter your command: ")
            command = command.lower()
            if command == "b":
                break
            elif command == "1":
                while True:
                    print("1. Create new voyage")
                    print("2. Repeat an existing voyage")
                    command = input("Please enter an option (b to go back): ")
                    if command == "b":
                        break
                    elif command == "1":
                        self.display_add_voyage_UI()
                    elif command == "2":
                        self.display_repeat_voyage_UI()
                    else:
                        print("Invalid input, try again")
            elif command == "2":
                self.display_destination_list()
            elif command == "3":
                pass
            else:
                print("Invalid input, try again")
        
        


