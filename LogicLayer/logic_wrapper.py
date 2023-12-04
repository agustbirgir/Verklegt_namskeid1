from LogicLayer.LogicLayerAPI import LogicLayerAPI
from DataLayer.data_wrapper import Data_Wrapper

class Logic_Wrapper:
    def __init__(self):
        self.data_wrapper = Data_Wrapper()
        self.LogicLayerAPI = LogicLayerAPI(self.data_wrapper)

    def create_employee(self, employee):
        return self.LogicLayerAPI.create_employee(employee)
    
    def get_all_employees(self):
        return self.LogicLayerAPI.get_all_employees()