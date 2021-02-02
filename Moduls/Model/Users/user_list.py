from .user import User

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

    #sortowanie :)