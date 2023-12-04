class NameLengthException(Exception):
    pass

def validate_name(name):
    """validate name"""
    if len(name) >= 50:
        raise NameLengthException