from ...Model.InOut import Input
from ...View.Manage_Users.Manage_Users import Manage_users

class User_controller:
    def __init__(self):
        self.users_list = Input.Input().user_list

    def add_user(self, dane):
        self.users_list.add_user(dane)

    def delete_user(self, ids):
        self.users_list.delete_user_by_id(ids)

    def change_user_data(self, data, ids):
        self.users_list.update_users_by_id(ids, data)

    def show(self, on_back, id_ = None):
        if id_ == None:
            return Manage_users(on_back = on_back, on_save = self.add_user)
        else:
            save = lambda data: self.change_user_data(data, id_)
            delete = lambda : self.delete_user(id_)
            user = self.users_list.get_user_by_id(id_)
            user_data = {
                'name': user.name,
                'surname': user.surname,
                'birth_date': user.birth_date,
                'avg_daily_activity': user.avg_daily_activity
            }
            return Manage_users(on_back = on_back, on_save = save, on_delete = delete, user_data = user_data)