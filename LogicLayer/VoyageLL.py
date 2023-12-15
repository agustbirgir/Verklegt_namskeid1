from datetime import datetime, timedelta
from UiLayer.input_validators import *

class VoyageLL:
    def __init__(self, data_connection):
        self.data_wrapper = data_connection

    def add_voyage(self, voyage):
        """Create a new voyage"""
        self.data_wrapper.add_voyage(voyage)

    def get_voyage(self, id):
        """Return a specific voyage"""
        return self.data_wrapper.get_voyage(id)

    def get_all_voyages(self):
        """Return all voyages"""
        return self.data_wrapper.get_all_voyages()

    def voyage_add_employee(self, employeeList, id):
        """Add an employee to a voyage"""
        self.data_wrapper.voyage_add_employee(employeeList, id)

    def voyage_add_flight(self, flight, id):
        """Update a flight in a voyage"""
        self.data_wrapper.voyage_add_flight(flight, id)
    
    def get_crew_of_voyage(self, voyage):
        """Get the crew of a specific voyage"""
        crew_list = [item.strip("'") for item in voyage.crew[1:-1].split(", ")]
        return crew_list

    def get_week_dates(self, date):

        date = datetime.strptime(date, "%Y-%m-%d")

        start_date = date - timedelta(days=date.weekday())
        
        week_dates = [(start_date+timedelta(days=d)).date() for d in range(7)]

        return week_dates

    
    def get_voyages_of_day(self, date_looking):
        voyages = self.data_wrapper.get_all_voyages()
        ret_list = []
        for v in voyages:

            voyage_flight = self.data_wrapper.get_flight(v.id)
            date_of_voyage = voyage_flight.departureTime
            date_of_voyage = datetime.strptime(date_of_voyage, '%Y-%m-%d %H:%M:%S').date()

            if str(date_of_voyage) == str(date_looking):
                ret_list.append(v)

        return ret_list

    def unmanned_voyage_fetcher(self, command, input): #command is subroutine (list, search, next), input is for search only
        all_employees = self.data_wrapper.get_all_employees()
        voyages = self.data_wrapper.get_all_voyages() #can change if you dont want it all

        if command == "list":
            ret_list =[]
            for Voyage in voyages:
                crew_list = [item.strip("'") for item in Voyage.crew[1:-1].split(", ")]
                if validate_voyage_crew(crew_list, all_employees) == False: 
                    ret_list.append(Voyage)
            return ret_list
        
        elif command == "search": #this one feels redundant...
            for Voyage in voyages:
                if Voyage["id"] == input: #this should work in theory, but im judging why im searching for a empty one in the first place...
                    crew_list = [item.strip("'") for item in Voyage.crew[1:-1].split(", ")]
        
                    if validate_voyage_crew(crew_list, all_employees) == False: 
                        print("Voyage found and unmanned")
                        return(Voyage)
                    else:
                        print("Voyage found and manned")
                        return(Voyage)
                else:
                    return("Voyage not found")

        elif command == "next":
            latest_unmanned_voyage = "There is no unmanned voyage left" #this is to make sure that if i never get into the dates of any
            first_run = True                                            #i dont give the date of a manned voyage
            for Voyage in voyages:
                crew_list = [item.strip("'") for item in Voyage.crew[1:-1].split(", ")]

                flight_id = Voyage.departureFlight
                flight = self.get_flight_by_id(flight_id)

                if flight:
                    try:
                        date_of_voyage = datetime.strptime(flight.departureTime, '%Y-%m-%d %H:%M:%S')
                    except ValueError as e:
                        print(f"Error parsing departure time for flight {flight_id}: {e}")
                        continue
                #voyage_departure_str = Voyage.departureFlight  # Corrected this line
                #date_of_voyage = datetime.strptime(voyage_departure_str, '%Y-%m-%d %H:%M:%S') 
                #date_of_voyage = datetime.strptime(date_of_voyage, '%Y-%m-%d %H:%M:%S')

                if validate_voyage_crew(crew_list, all_employees) == False:

                    if first_run == True:
                        latest_date_of_voyage = date_of_voyage
                        latest_unmanned_voyage = Voyage
                        first_run = False

                    elif date_of_voyage > latest_date_of_voyage: #takes the shortest/nearest date available (does not account for the past)
                        latest_date_of_voyage = date_of_voyage
                        latest_unmanned_voyage = Voyage

            return latest_unmanned_voyage

        else:
            print("error in command prompt")