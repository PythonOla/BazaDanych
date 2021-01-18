#na poźniej
from view import lista
 

class User_list_controller:
    def __init__(self, data):
        self.data  = data
    
    def show(self):
        return lista(self.data)

    #sortowanie