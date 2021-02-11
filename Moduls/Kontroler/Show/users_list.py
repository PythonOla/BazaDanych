from ...Model.InOut.Input import Input
from ...View.Listing.listing import Listing
 

class User_list_controller:
    def __init__(self):
        self.data = Input().user_list.users
    
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
        return Listing(users, fields)
    