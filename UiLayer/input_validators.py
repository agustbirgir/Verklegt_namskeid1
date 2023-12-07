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

def validate_date(date_text):
    try:
        datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False