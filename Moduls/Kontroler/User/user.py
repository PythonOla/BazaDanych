from ...Model.InOut import Input
#na poźniej
from view import Manage_users #szczegóły

class Users_controller:
    def __init__(self):
        self.users_list = Input().user_list

    def add_user(self, dane):
        #to do methode in model
        self.users_list.add_user(dane)

    def delete_user(self, ids):
        #to do methode  in model
        self.users_list.delete_user_by_id(ids)

    def change_user_data(self, data, ids):
        #to do methode in model
        self.users_list.update_users_by_id(ids, data)

    def show(self):
        #to do
        return Manage_users(self.users_list)