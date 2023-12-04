from DataLayer.DataLayerAPI import DataLayerAPI


class Data_Wrapper:
    def __init__(self):
        self.DataLayerAPI = DataLayerAPI()

    def get_all_employees(self):
        return self.DataLayerAPI.get_all_employees()

    def create_employee(self, employee):
        return self.DataLayerAPI.create_employee(employee)