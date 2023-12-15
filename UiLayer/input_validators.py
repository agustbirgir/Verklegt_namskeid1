import re
from datetime import datetime
#from Models.Employee import Employee


class NameLengthException(Exception):
    pass

def validate_name(name):
    """
    Validates that the name is not over 50 characters long

    Args:
        name (string): Name to be validated

    Examples:
        >>> get_flight(aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa)
        pass
    """
    if len(name) >= 50:
        raise NameLengthException
    
def validate_id(id):
    """
    Validates that a string is a digit or not

    Args:
        id (string): string to be validated

    Returns:
        Returns True if string is digit, False otherwise

    Examples:
        >>> validate_id(12)
        True
        >>> validate_id(hello)
        False
    """
    return id.isdigit()
    
def validate_ssn(ssn):
    """
    Validates that string has the length of a SSN and is a digit

    Args:
        ssn (string): string to be validated

    Returns:
        Returns True if string is SSN, False otherwise

    Examples:
        >>> validate_id(1012032040)
        True
        >>> validate_id(123)
        False
    """
    return ssn.isdigit() and len(ssn) == 10

def validate_string(string):
    """
    Validates that the string is not a digit

    Args:
        string (string): string to be validated

    Returns:
        Returns True if string is digit, False otherwise

    Examples:
        >>> validate_string(12)
        True
        >>> validate_id(hello)
        False
    """
    return string.isdigit()

def validate_phone(phone_number):
    """
    Validates that a string is a valid phone number

    Args:
        phone_number (string): string to be validated

    Returns:
        Returns True if string is phone number, False otherwise

    Examples:
        >>> validate_id(1234567)
        True
        >>> validate_id(123)
        False
    """
    pattern = re.compile(r"^\d{7,15}$")
    return pattern.match(phone_number) is not None

def validate_email(email):
    """
    Validates that a string is a valid email

    Args:
        email (string): string to be validated

    Returns:
        Returns True if string is an email, False otherwise

    Examples:
        >>> validate_email(siggi@gmail.com)
        True
        >>> validate_id(gusti@gmail)
        False
    """
    return '@' in email and email.endswith('.com')

def validate_date(date):
    """
    Validates that a date is in a valid format

    Args:
        date (string): date to be validated

    Returns:
        Returns True if string is a date in the right format, False otherwise

    Examples:
        >>> validate_id(10-12-2003)
        True
        >>> validate_id(2003-12-10)
        False
    """
    try:
        datetime.strptime(date, '%d-%m-%Y')
        return True
    except ValueError:
        return False
    
def validate_date_2(date):
    """
    Validates that a date is in a valid format

    Args:
        date (string): date to be validated

    Returns:
        Returns True if string is a date in the right format, False otherwise

    Examples:
        >>> validate_id(2003-12-10)
        True
        >>> validate_id(10-12-2003)
        False
    """
    try:
        datetime.strptime(date, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    
def validate_time(time):
    """
    Validates that time is in a valid time format

    Args:
        time (string): time to be validated

    Returns:
        Returns True if string is in the right time format, False otherwise

    Examples:
        >>> validate_id(4:30)
        True
        >>> validate_id(430)
        False
    """
    try:
        datetime.strptime(time, '%H:%M')
        return True
    except ValueError:
        return False

def validate_voyage_date(date):
    """
    Validates that a date is in a valid format

    Args:
        date (string): date to be validated

    Returns:
        Returns True and the datetime object if string is a date in the right format, False otherwise

    Examples:
        >>> validate_id(2003-12-10 10:30)
        True
        >>> validate_id(10-12-2003 10:30)
        False
    """
    try:
        datetime_obj = datetime.strptime(date, '%Y-%m-%d %H:%M')
        return True, datetime_obj
    except ValueError:
        return False, None

def validate_if_not_number(str):
    """
    Validates that string is not a number

    Args:
        str (string): string to be validated

    Returns:
        Returns True if string is not number, False otherwise

    Examples:
        >>> validate_id(2003)
        True
        >>> validate_id(hello)
        False
    """
    return not str.isdigit()

def validate_voyage_crew(crew_list, employee_list):
    """
    Validates that a crew has 2 pilots, one of which is a head pilot, and one flight attendant, one of which is a head fligt attendant

    Args:
        crew_list (list of Employee): crew to be validated
        employee_list (list of Employee): all employees of NaN Air

    Returns:
        Returns True if crew meets requirements, False otherwiese

    Examples:
        >>> validate_id(['Siggi','Tommy Lee','Sigurjon'])
        True
        >>> validate_id(['Siggi])
        False
    """
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
    if pilot_count >= 2 and head_pilot_count >= 1 and attendant_count >= 1 and head_attendant_count >= 1:
        return True
    else:
        return False
        
def validate_if_registered_at_date(date1, date2):
    """
    Validates that a date is equal to another date

    Args:
        date1 (string): date to be validated
        date2 (string): date to be validated

    Returns:
        Returns True if the two dates are on the same day, False otherwise

    Examples:
        >>> validate_id("2003-12-10", "2003-12-10")
        True
        >>> validate_id("2003-12-10", "2003-12-11")
        False
    """
    date1 = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S').date()
    date2 = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S').date()

    return date1 == date2


def validate_pilot(employee, aircraft_name):
    """
    Validates that a pilot has a license for an aircraft

    Args:
        employee (string): pilot to be validated
        aircraft_name (string): name of aircraft to validate against

    Returns:
        Returns True if pilot has the license for the aircraft, False otherwise

    Examples:
        >>> validate_id("Siggi", "Airbus A330")
        False
        >>> validate_id("Siggi", "Boeing 737")
        True
    """
    if employee.profession == "Pilot" or employee.profession == "Head Pilot":
        if employee.aircraftLicense == aircraft_name:
            return True
        else:
            return False
    else:
        return True




def validate_if_registered_at_date_voyage(date1, date2):
    date1 = datetime.strptime(date1, '%Y-%m-%d %H:%M:%S').date()
    date2 = datetime.strptime(date2, '%Y-%m-%d %H:%M:%S').date()

    return date1 == date2