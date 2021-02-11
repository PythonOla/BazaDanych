from ...Model.InOut.Input import Input
from ...View.UserList.UserList import UserList
 

class User_list_controller:
    def __init__(self, *args):
        self.data = Input().user_list.users
        self.args = args
    
    def show(self):
        fields = ['Imię i Nazwisko', 'Data Urodzenia', 'Przyjaciół', 'Aktywność', 'Dołączył']
        users = []
        for user in self.data:
            users.append({
                'Imię i Nazwisko': user.name + " " + user.surname,
                'Data Urodzenia': user.birth_date,
                'Przyjaciół': str(len(user.friends)),
                'Aktywność': str(user.avg_daily_activity),
                'Dołączył': user.joined_on
            })
        return UserList({'rows': users, 'fields': fields}, self.args[0])
    