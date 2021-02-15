from .user import User
from ..InOut import Output
from datetime import date

class User_list:
    def __init__(self, users):
        self.users = []
        for usr in users:
            self.users.append(User(usr))

    def get_names_by_condition(self, condition):
        names = []
        for usr in self.users:
            if condition(usr):
                names.append(
                    usr.name + ' ' + usr.surname
                )
        return names

    def get_names_by_ids(self, ids):
        return self.get_names_by_condition(
            lambda usr: usr.id in ids
        )

    def get_user_by_id(self, _id):
        users = [user for user in self.users if int(user.id) == int(_id)]
        return users[0]

    def find_users_by_id(self, _id):
        try:
            converted_id = int(_id)
            users = [user for user in self.users if int(user.id) == int(_id)]
            return users
        except ValueError:
            return []

    def search_by_name(self, txt):
        # wszystkie osoby ktorych imie i nazwisko zawiera podany ciąg znaków
        users = [user for user in self.users if (user.name + " " + user.surname).lower().count(txt.lower()) > 0]
        return users


    def _save_usr_to_database(self):
        data_base = Output.Output()
        users_to_serialize = list(map(lambda user: user.get_serializable(), self.users))
        data_base.update_users(users_to_serialize)

    def add_user(self, data):
        #id liczymy od 0, więc musimy zacząć max_id od -1
        max_id = -1
        for user in self.users:
            if user.id > max_id:
                max_id = user.id

        new_id = max_id + 1
        data['id'] = new_id
        data['friends'] = []
        data['posts'] = []
        data['comments'] = []
        data['likes'] = []
        data['photos'] = []
        data['joined_on'] = date.today().strftime('%Y-%m-%d')
        self.users.append(User(data))
        self._save_usr_to_database()
        return new_id
     
    def delete_user_by_id(self, ids):
        self.users = [user for user in self.users if user.id != ids]
        self._save_usr_to_database()

    def update_users_by_id(self, ids, data):
        user = [user for user in self.users if user.id == ids][0]
        
        #zmiany profilu
        user.name = data['name'] if 'name' in data else user.name
        user.surname = data['surname'] if 'surname' in data else user.surname
        user.birth_date = data['birth_date'] if 'birth_date' in data else user.birth_date
        user.avg_daily_activity = data['avg_daily_activity'] if 'avg_daily_activity' in data else user.avg_daily_activity
        # id i joined_on nigdy nie zmieniamy

        #zmiany z działalności usera
        user.posts = data.posts if 'post' in data else user.posts
        

        self._save_usr_to_database()


    #sortowanie :)