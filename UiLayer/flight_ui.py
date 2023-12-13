from Models.Flight import Flight
from Models.Destination import Destination
from Models.Voyage import Voyage
from UiLayer.input_validators import *

class Flight_UI:
    def __init__(self, logic_connection):
        self.logic_wrapper = logic_connection
        self.asciiart = r"""

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
                        CHOOSE YOUR OPTIONS
===================================================================================

                1. Create voyage
                2. Destination database
                3. Show flight info per week

===================================================================================
                    [B]ack                [Q]uit
===================================================================================
        """


    def display_flight_manager_UI(self):
        print(self.asciiart)

    def display_destination_database_UI(self):
        while True:
            print("""===================================================================================
                  
                    1. List all destinations
                    2. Add new destination
                  
===================================================================================
                        [B]ack
===================================================================================""")
            command = input("Please input an option: ")
            if command == "1":
                self.display_destination_list()
            elif command == "2":
                self.display_add_destination_UI()
            elif command == "b":
                break
            else:
                print("Invalid input, try again")

    def display_destination_list(self):
        destinations = self.logic_wrapper.get_all_destinations()

        seperator_line = '-' * 100

        print("{:<12} {:<13} {:<20} {:<10} {:<10} {:<15} {:<15}".format(
            'Country', 'City', 'Airport', 'Flytime', 'Distance', 'Contact', 'Contact Number'
        ))
        print(seperator_line)

        for dest in destinations:
            print("{:<15} {:<15} {:<20} {:<10} {:<10} {:<15} {:<15}".format(
                dest.country, dest.city, dest.airport, dest.flytime, dest.distance, dest.contact, dest.contactNumber
            ))
            print(seperator_line)

    def display_add_destination_UI(self):
        #print("Fill out the destination details")
        d = Destination()

        fields = [
            ("Enter the country: ", "country", validate_name),
            ("Enter the city: ", "city", validate_if_not_number),
            ("Enter the airport: ", "airport", validate_if_not_number),
            ("Enter the flytime (HH:MM): ", "flytime", validate_time),
            ("Enter the distance from Iceland (in km): ", "distance", lambda x: not validate_if_not_number(x)),
            ("Enter name of contact: ", "contact", validate_if_not_number),
            ("Enter the contact number: ", "contactNumber", validate_phone)
        ]

        for prompt, attribute, validation in fields:
            while True:
                self.print_destination_details(d)
                value = input(prompt)
                
                if value.lower() in ['b' or 'q']:
                    return

                try:
                    validation(value)
                    setattr(d, attribute, value)
                    break
                except NameLengthException:
                    print("Name is too long")

        self.logic_wrapper.add_destination(d)
        print(f"Successfully registered new destination at {d.city}")

    def print_destination_details(self, destination):
        print(f"""
===================================================================================
                        Destination Details
===================================================================================
                    
                    Country: {destination.country}
                    City: {destination.city}
                    Airport: {destination.airport}
                    Flytime: {destination.flytime}
                    Distance: {destination.distance}
                    Contact: {destination.contact}
                    Contact Number: {destination.contactNumber}
              
===================================================================================
                            [B]ack      [Q]uit
===================================================================================
        """)



    def display_add_voyage_UI(self):
        destination_menu = {
                    "1": "Nuuk",
                    "2": "Kulusuk",
                    "3": "Thorshavn",
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
                    departureFlight = Flight()
                    departureFlight.startingPoint = "Keflavik" # Starting point is always keflavik for now in A requirements
                    departureFlight.departureTime = departureDate
                    departureFlight.arrivalTime = arrivalDate
                    departureFlight.destination = destination.city
                    departureFlight.id = id
                    print("Successfully registered")
                    # User could cancel, so we dont write the flight to the csv file until he has registered the second flight as well.
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
                    arrivalFlight.destination = self.logic_wrapper.get_destination("Keflavik").city # Keflavik is always the arrival destination in A requirements, change in B requirements
                    arrivalFlight.id = id

                    # Add the departure flight and arrival flight to the voyage
                    voyage = Voyage()
                    voyage.departureFlight = arrivalFlight.id
                    voyage.arrivalFlight = arrivalFlight.id
                    voyage.crew = []
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
            id = input("please enter voyage ID: ")
            try:
                id = int(id)
                break
            except ValueError:
                print("Invalid ID, please enter a number.")
        get_voyage = self.logic_wrapper.get_voyage(id)
        if get_voyage != None:
            print(f"You picked voyage: {get_voyage}")
            while True:
                repeat_date = input("Please input the date and time for when you want to repeat this voyage (DD-MM-YYYY,HH:MM) (q to quit): ")
                validate, date = validate_voyage_date(repeat_date)
                if repeat_date == "q":
                    break
                elif validate_voyage_date(validate):
                    print("Invalid date format, try again")
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
            self.display_flight_manager_UI()
            seperator_line = '=' * 83
            command = input("Enter your command: ")
            command = command.lower()
            if command == "b":
                break
            elif command == "1":
                while True:
                    print("""
===================================================================================
                          
                    1. Create new voyage
                    2. Repeat an existing voyage

===================================================================================
                        [B]ack
===================================================================================
                    """)
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
                self.display_destination_database_UI()
            elif command == "3":
                pass
            else:
                print("Invalid input, try again")

