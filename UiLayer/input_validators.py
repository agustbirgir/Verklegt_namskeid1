import re
from datetime import datetime

class NameLengthException(Exception):
    pass

def validate_name(name):
    """validate name"""
    if len(name) >= 50:
        raise NameLengthException
    
def validate_id(id):
    return id.isdigit()
    
def validate_ssn(ssn):
    return ssn.isdigit() and len(ssn) == 10

def validate_phone(phone_number):
    pattern = re.compile(r"^\d{7,15}$")
    return pattern.match(phone_number) is not None

def validate_email(email):
    return '@' in email and email.endswith('.com')

def validate_date(date):
    try:
        datetime.strptime(date, '%d-%m-%Y')
        return True
    except ValueError:
        return False
    
def validate_date_2(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    
def validate_time(time):
    try:
        datetime.strptime(time, '%H:%M')
        return True
    except ValueError:
        return False

def validate_voyage_date(date):
    try:
        datetime_obj = datetime.strptime(date, '%Y-%m-%d %H:%M')
        return True, datetime_obj
    except ValueError:
        return False, None

def validate_if_date_after(arrival, departure):
    return arrival > departure

def validate_if_not_number(str):
    return not str.isdigit()

def validate_voyage_crew(crew_list, employee_list):
    pilot_count = 0
    head_pilot_count = 0
    attendant_count = 0
    head_attendant_count = 0
    for employee in employee_list:
        for crew in crew_list:
            if employee.name == crew:
                if employee.profession == "Pilot":
                    pilot_count += 1
                elif employee.profession == "Head Pilot":
                    head_pilot_count += 1
                    pilot_count += 1
                elif employee.profession == "Attendant":
                    attendant_count += 1
                else:
                    head_attendant_count += 1
                    attendant_count += 1
    #print("pilot", pilot_count,"head pilot:",head_pilot_count,"attendant:",attendant_count,"head attendant:",head_pilot_count)
    if pilot_count >= 2 and head_pilot_count >= 1 and attendant_count >= 1 and head_attendant_count >= 1:
        return True
    else:
        return False
    
def validate_employee_for_voyage(name, selected_voyage_departure, v_crew, v, v_departure):
    if name in v_crew:
        print("departures")
        print(selected_voyage_departure)
        print(v_departure)
        if validate_if_registered_at_date(selected_voyage_departure, v_departure):
            return False
        else:
            return True
        

def validate_if_registered_at_date(date1, date2):
    date1 = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S').date()
    date2 = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S').date()

    return date1 == date2



#------not validators, but it wont work in the ui layer


def pull_next_unmanned_voyage(self):  #i will make a temp function for the pull, im not sure how to integrate it as of now, just bear with this abomination for now
    subroutine = "next"                                 #this should be able to pull in the next empty voyage
    input = 0                                           #so this should be used in the main function for crew assignment on while loops
    return self.logic_wrapper.unmanned_voyage_fetcher(subroutine, input) 