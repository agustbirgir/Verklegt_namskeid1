from UiLayer.input_validators import *

class EmployeeUpdater:
    def __init__(self, logic_wrapper):
        self.logic_wrapper = logic_wrapper

    def update_employee_details(self, ssn):
        employee = self.logic.find_employee_by_ssn(ssn)
        if not employee:
            print("Employee not found.")
            return

        # Update Profession
        if input(f"Current profession: {employee.profession}. Update profession? (y/n): ") == 'y':
            employee.profession = self.prompt_for_new_value("profession", None)  # Assuming no validation for profession

        # Update Home Address
        if input(f"Current home address: {employee.homeAddress}. Update home address? (y/n): ") == 'y':
            employee.homeAddress = self.prompt_for_new_value("home address", None)  # Assuming no validation for home address

        # Update GSM Number
        if input(f"Current GSM number: {employee.gsmNumber}. Update GSM number? (y/n): ") == 'y':
            employee.gsmNumber = self.prompt_for_new_value("GSM number", validate_phone)

        # Update Email
        if input(f"Current email: {employee.email}. Update email? (y/n): ") == 'y':
            employee.email = self.prompt_for_new_value("email", validate_email)

        # Update Home Phone
        if input(f"Current home phone: {employee.homePhone}. Update home phone? (y/n): ") == 'y':
            employee.homePhone = self.prompt_for_new_value("home phone", validate_phone)

        # Update Status
        if input(f"Current status: {employee.status}. Update status? (y/n): ") == 'y':
            new_status = self.prompt_for_new_value("status", lambda x: x.isdigit())
            employee.status = int(new_status)

        # Update Scheduled Date
        if input(f"Current scheduled date: {employee.scheduled}. Update scheduled date? (y/n): ") == 'y':
            employee.scheduled = self.prompt_for_new_value("scheduled date", validate_date)

        # Save the updated employee details
        self.logic.update_employee(employee)

    def prompt_for_new_value(self, field_name, validation_func):
        while True:
            new_value = input(f"Enter new {field_name}: ")
            if not validation_func or validation_func(new_value):
                return new_value
            print(f"Invalid {field_name}, please try again.")
