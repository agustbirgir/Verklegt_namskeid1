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
            print("===================================================================================")
            print("                Destinations ")
            print("===================================================================================")
            for key, value in destination_menu.items():
                print(f"""{key}. {value}""")
            print(f"""
===================================================================================
                  [B]ack            [Q]uit
===================================================================================
            """)    
            command = input("Option: ")
            if command.lower() == "q":
                exit(0)
            if command.lower() == "b":
                break
            elif int(command) < 0 or int(command) > 5:
                print("Invalid input, try again")
            else:
                print(destination_menu[command])
                destination = self.logic_wrapper.get_destination(destination_menu[command])
                if destination != None:
                    print(f"""
===================================================================================
===================================================================================
                    Selected destination: 
                        country: {destination.country} 
                        city: {destination.city}
                        airport: {destination.airport}

===================================================================================
                        [B]ack        [Q]uit
===================================================================================

                    """)
                    print(f"Selected destination: country: {destination.country}, city: {destination.city}, airport: {destination.airport}")
                    break
                else:
                    print("Destination does not exist, try again")
        if command != "b":
            id = self.logic_wrapper.create_unique_id()
            while True:
                print()
                departure = input(f"Please pick the departure time from Keflavik to {destination.city} (YYYY-MM-DD HH:MM): ")
                validate, departureDate = validate_voyage_date(departure)
                if departure.lower() == "b":
                    break
                if departure.lower() == "q":
                    exit(0)
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
                    # User could cancel, so we dont write the flight to the csv file until he has registered the second flight as well.
                    break
        if departure != "q" and command != "q":
            #while True: B requirements
            #departure2 = input(f"Please pick the departure time from {destination.city} to Keflavik (DD-MM-YYYY,HH:MM) (q to quit): ")
            departure2 = arrivalDate.strftime('%Y-%m-%d %H:%M') # the A requirements has it so every voyage returns the same date as it leaves
            validate, departureDate2 = validate_voyage_date(departure2)
            #validate_if_after = validate_if_date_after(departure2, departure) # Doesnt quite work
            if validate == False:
                print("Wrong format for input, try again")
            #elif validate_if_after == False:
                #print("Arrival date must be set after the departure date, try again")
            elif validate == True:

                flytime2 = datetime.strptime(destination.flytime,'%H:%M')
                arrivalDate2 = self.logic_wrapper.calculate_arrival_time(departureDate2, flytime2)
                arrivalFlight = Flight()
                arrivalFlight.startingPoint = destination.city 
                arrivalFlight.departureTime = departureDate2
                arrivalFlight.arrivalTime = arrivalDate2
                arrivalFlight.destination = self.logic_wrapper.get_destination("Keflavik").city # Keflavik is always the arrival destination in A requirements, change in B requirements
                arrivalFlight.id = id

                # Add the departure flight and arrival flight to the voyage
                voyage = Voyage()
                voyage.departureFlight = departureFlight.id
                voyage.arrivalFlight = arrivalFlight.id
                voyage.crew = []
                voyage.id = id

                self.logic_wrapper.add_flight(departureFlight)
                self.logic_wrapper.add_flight(arrivalFlight)
                self.logic_wrapper.add_voyage(voyage)
                
                print(f"""
===================================================================================
                      Successfully registered voyage, ID: {id}
===================================================================================

            Departure from Keflavik to {destination.city}: {departureDate}
            Arrival date from Keflavik to {destination.city}: {arrivalDate}
            Departure from {destination.city} to Keflavik: {departureDate2}
            Arrival date from {destination.city} to Keflavik: {arrivalDate2}

===================================================================================

===================================================================================
                """)


    def List_voyage_specific_date(self):
        pass


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
                    2. List Voyage on a specifc date

===================================================================================
                        [B]ack          [Q]uit
===================================================================================
                    """)
                    command = input("Option: ")
                    if command.lower() == "b":
                        break
                    if command.lower() == "q":
                        exit(0)
                    elif command == "1":
                        self.display_add_voyage_UI()
                    elif command == "2":
                        self.List_voyage_specific_date()
                    else:
                        print("Invalid input, try again")
            elif command == "2":
                self.display_destination_database_UI()
            elif command == "3":
                pass
            else:
                print("Invalid input, try again")


    def display_voyage_search(self):
        while True:
            date = input("Search by date (DD-MM-YYYY) (b to go back): ")
            date = date.lower()
            if date == "back" or date == "b":
                break
            else:
                if validate_date(date):
                    print(self.logic_wrapper.get_voyages_of_day(date))
                else:
                    print("invalid date")