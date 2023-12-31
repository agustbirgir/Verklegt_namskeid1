from Models.Flight import Flight
from Models.Destination import Destination
from Models.Voyage import Voyage
from Models.Aircraft import Aircraft
from UiLayer.input_validators import *

class Flight_UI:
    def __init__(self, logic_connection):
        """
        Constructor that establishes a connection to the logic wrapper
        """
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

                1. Voyages
                2. Destination database
                3. Register new aircraft
                

===================================================================================
                    [B]ack                [Q]uit
===================================================================================
        """


    def display_flight_manager_UI(self):
        """
        Displays ascii art

        Example:
            >>> display_fligt_manager_UI()
            
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
                3. Register new aircraft
                

===================================================================================
                    [B]ack                [Q]uit
===================================================================================
        """
        print(self.asciiart)

    def display_destination_database_UI(self):
        """
        Displays the menu for listing all destinations or adding a new destination

        Example:
            >>> display_destination_database_UI()
            ===================================================================================
                  
                    1. List all destinations
                    2. Add new destination
                            
            ===================================================================================
                                    [B]ack
            ===================================================================================

        """
        
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

    def display_add_aircraft_UI(self):
        """
        Displays the menu for adding and adds a new aircraft to the database

        Example:
            >>> display_add_aircraft_UI()
            Enter the name of the aircraft:

        """
        a = Aircraft()
        while True:
            a.name = input("Enter the name of the aircraft: ")
            try:
                validate_name(a.name)
                break
            except NameLengthException:
                print("Name was too long")

        a.type = input("Enter the type: ")

        a.manufacturer = input("Enter the manufacturer: ")
        while validate_string(a.manufacturer):
            print("Input has to be string, try again")
            a.manufacturer = input("Enter the manufacturer: ")
        
        a.noOfPassengers = input("Enter the number of passengers: ")
        while not validate_string(a.noOfPassengers):
            print("Input has to be a number, try again")
            a.noOfPassengers = input("Enter the manufacturer: ")

        # Add aircraft
        self.logic_wrapper.add_aircraft(a)

    def display_destination_list(self):
        """
        Lists all destinations

        Example:
            >>> display_destination_list()
            Country      City          Airport              Flytime    Distance   Contact         Contact Number
            ----------------------------------------------------------------------------------------------------
            Iceland         Keflavik        Keflavik Airport     6:20       1000       helgi           87654321
            ----------------------------------------------------------------------------------------------------
            Greenland       Nuuk            Nuuk Airport         2:40       2000       john            12345678
            ----------------------------------------------------------------------------------------------------
            Greenland       Kulusuk         Kulusuk Airport      2:40       2500       uji             1234813
            ----------------------------------------------------------------------------------------------------
            Faroe Islands   Thorshavn       Vagar Airport        5:30       4500       joe             13579864
            ----------------------------------------------------------------------------------------------------
            Shetland Islands Tingwall        Tingwall Airport     4:55       3400       mark            5432167
            ----------------------------------------------------------------------------------------------------
            Svalbard        Longyearbyen    Svalbard Airport     4:20       6000       jarl            9324535
            ----------------------------------------------------------------------------------------------------

        """
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
        """
        Displays the menu for adding and adds a new destination to the database

        Example:
            >>> display_add_destination_UI()
            Enter the country:
        """
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
        """
        Lists all details of a specific destination

        Example:
            >>> print_destination_details()
            ===================================================================================
                        Destination Details
            ===================================================================================
                                
                                Country: Greenland
                                City: Kulusuk
                                Airport: Kulusuk Airport
                                Flytime: 4:30
                                Distance: 3000
                                Contact: Helga
                                Contact Number: 10563937
                        
            ===================================================================================
                                        [B]ack      [Q]uit
            ===================================================================================

        """
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
        """
        Displays the menu for adding a new voyage

        Example:
            >>> display_add_voyage_UI()
            ===================================================================================
                Destinations
            ===================================================================================
            1. Nuuk
            2. Kulusuk
            3. Thorshavn
            4. Tingwall
            5. Longyearbyen

            ===================================================================================
                            [B]ack            [Q]uit
            ===================================================================================

            Option:
        """
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
                  [B]ack            [Q]uit
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
                departure = input(f"Please pick the departure time from Keflavik to {destination.city} (YYYY-MM-DD HH:MM) (q to quit, b to break): ")
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
            departure2 = arrivalDate.strftime('%Y-%m-%d %H:%M') # the A requirements has it so every voyage returns the same date as it leaves
            #departure2 = self.logic_wrapper.calculate_arrival_time(datetime.strptime(str(arrivalDate), '%Y-%m-%d %H:%M'), datetime.strptime("3:00",'%H:%M')) # Add 3 hours between landing and departure
            validate, departureDate2 = validate_voyage_date(departure2)
            if validate == False:
                print("Wrong format for input, try again")
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
                voyage.aircraft = ''

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

    def display_repeat_voyage_UI(self):
        """
        Displays the menu for repeating a voyage

        Example:
            >>> display_repeat_voyage_UI()
            Please enter voyage ID:
        """
        while True:
            id = input("Please enter voyage ID: ")
            try:
                id = int(id)
                break
            except ValueError:
                print("Invalid ID, please enter a number.")
        get_voyage = self.logic_wrapper.get_voyage(id)
        if get_voyage != None:
            print(f"You picked voyage: {get_voyage.id}")
            while True:
                repeat_date = input("Please input the date and time for when you want to repeat this voyage (YYYY-MM-DD HH:MM) (q to quit): ")
                validate, departureDate = validate_voyage_date(repeat_date)
                if repeat_date == "q":
                    break
                elif validate == False:
                    print("Invalid date format, try again")
                elif validate_if_registered_at_date(repeat_date, self.logic_wrapper.get_flight(get_voyage.id).departureTime):
                    print("cant repeat voyage on same day as original voyage")
                elif validate == True:
                    new_id = self.logic_wrapper.create_unique_id() # Create a new id
                    voyage_flights = self.logic_wrapper.get_voyage_flights(id) # Get the flights of the selected voyage

                    # ----------- Register departure flight ------------
                    destination = self.logic_wrapper.get_destination(voyage_flights[0].destination)
                    flytime = datetime.strptime(destination.flytime,'%H:%M')
                    arrivalDate = self.logic_wrapper.calculate_arrival_time(departureDate, flytime)
                    print("Arrival date departure:", arrivalDate)
                    departureFlight = Flight()
                    departureFlight.startingPoint = "Keflavik" # Starting point is always keflavik for now in A requirements
                    departureFlight.departureTime = departureDate
                    departureFlight.arrivalTime = arrivalDate
                    departureFlight.destination = destination.city
                    departureFlight.id = new_id

                    # -------- Register arrival flight ------------
                    destination2 = "Keflavik"           # Destination always Keflavik in A requirements
                    departureDate2 = arrivalDate
                    destination2 = self.logic_wrapper.get_destination(voyage_flights[0].destination)
                    flytime2 = datetime.strptime(destination2.flytime,'%H:%M')
                    arrivalDate2 = self.logic_wrapper.calculate_arrival_time(departureDate2, flytime2)
                    arrivalFlight = Flight()
                    arrivalFlight.startingPoint = destination.city # Get the city of the departure flight
                    arrivalFlight.departureTime = departureDate2
                    arrivalFlight.arrivalTime = arrivalDate2
                    arrivalFlight.destination = "Keflavík" # Keflavik is always the arrival destination in A requirements, change in B requirements
                    arrivalFlight.id = new_id

                    # ----------- Add the departure flight and arrival flight to the new voyage -----------
                    new_voyage = Voyage()
                    new_voyage.departureFlight = departureFlight.id
                    new_voyage.arrivalFlight = arrivalFlight.id
                    new_voyage.crew = get_voyage.crew
                    new_voyage.id = new_id

                    crew_list = self.logic_wrapper.get_crew_of_voyage(get_voyage)
                    for name in crew_list:
                        employee = self.logic_wrapper.get_employee_by_name(name)
                        if employee is not None:
                            schedule = self.logic_wrapper.get_schedule_of_employee(employee)
                            voyage_date = str(departureDate).split(" ")[0] # Get only the date not the time
                            schedule.append(voyage_date)
                            employee.scheduled = schedule
                            self.logic_wrapper.update_employee(employee)
                        else:
                            print(f"Employee named {name} not found.")


                    self.logic_wrapper.add_flight(departureFlight)
                    self.logic_wrapper.add_flight(arrivalFlight)
                    self.logic_wrapper.add_voyage(new_voyage)
                    
                    print(f"""
===================================================================================
                    Successfully registered voyage, ID: {id}
===================================================================================
                          
            Departure from Keflavik to {destination.city}: {departureDate}
            Arrival date from Keflavik to {destination.city}: {arrivalDate}
            Departure from {destination.city} to Keflavik: {departureDate2}
            Arrival date from {destination.city} to Keflavik: {arrivalDate2}

===================================================================================
                        [B]ack          [Q]uit  
===================================================================================

                        """)
                    print(f"\nSuccessfully registered voyage, ID: {new_id}")
                    print(f"\nDeparture from Keflavik to {destination.city}:", departureDate)
                    print(f"Arrival date from Keflavik to {destination.city}:", arrivalDate)
                    print(f"\nDeparture from {destination.city} to Keflavik:", departureDate2)
                    print(f"Arrival date from {destination.city} to Keflavik:", arrivalDate2)
                    print()
                    break
        else:
            print("Voyage not found")

    def display_get_voyage_on_date_UI(self):
        """
        Displays the menu for getting all voyages on a specific date

        Example:
            >>> display_get_voyage_on_a_date_UI()
            Please input the date to get all voyages (YYYY-MM-DD):
        """
        while True:
            date = input("Please input the date to get all voyages (YYYY-MM-DD) (b to go back): ")
            if date == "b":
                break
            elif not validate_date_2(date):
                print("Invalid date format, try again")
            else:
                header = "{:<6} {:<20} {:<20} {:<20}".format('ID', 'Departure Time', 'Destination', 'Is Manned')
                separator_line = '-' * 70

                print(separator_line)
                print(header)
                print(separator_line)
                
                employees = self.logic_wrapper.get_all_employees()

                result = self.logic_wrapper.get_voyages_of_day(date)
            
                for voyage in result:
                    flight = self.logic_wrapper.get_flight(voyage.id)
                    if flight:
                        is_manned = "true"
                        if validate_voyage_crew(self.logic_wrapper.get_crew_of_voyage(voyage), employees) == 1:
                            is_manned = "True"
                        else:
                            is_manned = "False"
                        print("{:<6} {:<20} {:<20} {:<20}".format(
                            flight.id, flight.departureTime, flight.destination, is_manned)
                        )
                        print(separator_line)
                print("""
===================================================================================
                                [Q]uit  
===================================================================================
                """)
    
    def display_get_voyages_in_a_week_UI(self):
        """
        Displays the menu for getting all voyages in a specific week

        Example:
            >>> display_add_voyage_UI()
            Please input a date in the week to be checked (YYYY-MM-DD) (q to quit):
        """
        while True:
            date = input("Please input a date in the week to be checked (YYYY-MM-DD) (q to quit): ")
            if date == "q":
                break
            elif not validate_date_2(date):
                print("Invalid date format, try again")
            else:
                week = self.logic_wrapper.get_week_dates(date)
                header = "{:<6} {:<20} {:<20} {:<20}".format('ID', 'Departure Time', 'Destination', 'Is Manned')
                separator_line = '-' * 70

                print("===================================================================================")
                print(header)
                print(separator_line)

                employees = self.logic_wrapper.get_all_employees()

                for day in week:
                    result = self.logic_wrapper.get_voyages_of_day(day)

                    if not result:  # If there are no voyages on this day, print the date and separator
                        print(f"Date: {day}")
                        print(separator_line)
                    else:  # If there are voyages, print the date without the separator
                        print(f"Date: {day}")

                        for voyage in result:
                            flight = self.logic_wrapper.get_flight(voyage.id)
                            if flight:
                                is_manned = "true"
                                if validate_voyage_crew(self.logic_wrapper.get_crew_of_voyage(voyage), employees) == 1:
                                    is_manned = "True"
                                else:
                                    is_manned = "False"
                                                        
                                print("{:<6} {:<20} {:<20} {:<20}".format(
                                    flight.id, flight.departureTime, flight.destination, is_manned)
                                )
                        print(separator_line)  # Print the separator after listing all voyages of the day

                print("""===================================================================================
                        [Q]uit  
===================================================================================""")


    def display_employee_voyages_in_a_week_UI(self):
        """
        Displays the menu for getting all voyages of a specific employee in a specific week

        Example:
            >>> display_employee_voyages_in_a_week_UI()
            Please input a date in the week to be checked (YYYY-MM-DD) (q to quit):
        """
        while True:
            date = input("Please input a date in the week to be checked (YYYY-MM-DD) (b to go back): ")
            if date.lower() == "q":
                exit(0)
            elif date.lower() == "b":
                break
            elif not validate_date_2(date):
                print("Invalid date format, try again")
            else:
                break
        if date.lower() != "b":
            while True:
                name = input("Please input the name of the employee to be checked (b to go back): ")
                if name.lower() == "b":
                    break
                elif validate_string(name):
                    print("Input has to be a string, try again")
                else:
                    week = self.logic_wrapper.get_week_dates(date)
                    voyages = self.logic_wrapper.get_all_voyages()

                    header = "{:<12} {:<20} {:<20}".format('Date', 'Employee Name', 'Voyage Destination')
                    separator = '-' * len(header)
                    print("\n" + header)
                    print(separator)

                    for day in week:
                        print(f"{day}:")
                        result = self.logic_wrapper.employee_schedule_checker(day, True)
                        if len(result) == 0:
                            print("    Employee not working")
                        else:
                            for elem in result:
                                if elem.name != name:
                                    break
                                
                                cleaned_name = elem.name.replace("<15", "").strip()
                                for v in voyages:
                                    
                                    v_crew = self.logic_wrapper.get_crew_of_voyage(v)
                                    if cleaned_name in v_crew:
                                        
                                        destination = self.logic_wrapper.get_flight(v.id).destination
                                        line = "            {:<20} {:<20}".format(cleaned_name, destination)
                                        print(line)
                                        break
                        print(separator)


    def input_prompt(self):
        """
        Displays the main menu for the flight manager

        Example:
            >>> input_prompt()
            ===================================================================================
                          
                    1. Create new voyage
                    2. Repeat an existing voyage
                    3. Get voyage on specific date
                    4. List voyages in a specific week
                    5. List an employees voyages in a week

            ===================================================================================
                                    [B]ack          [Q]uit
            ===================================================================================
            Enter an option:
        """
        while True:
            self.display_flight_manager_UI()
            command = input("Enter an option: ")
            command = command.lower()
            if command == "b":
                break
            elif command == "1":
                while True:
                    print("""
===================================================================================
                          
                    1. Create new voyage
                    2. Repeat an existing voyage
                    3. Get voyage on specific date
                    4. List voyages in a specific week
                    5. List an employees voyages in a week

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
                        self.display_repeat_voyage_UI()
                    elif command == "3":
                        self.display_get_voyage_on_date_UI()
                    elif command == "4":
                        self.display_get_voyages_in_a_week_UI()
                    elif command == "5":
                        self.display_employee_voyages_in_a_week_UI()
                    else:
                        print("Invalid input, try again")
            elif command == "2":
                self.display_destination_database_UI()
            elif command == "3":
                self.display_add_aircraft_UI()
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
       
