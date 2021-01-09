from user import User

class User_list:
    def __init__(self, users):
        self.users = []
        for usr in users:
            self.users.append(User(usr))
    
    #sortowanie :)