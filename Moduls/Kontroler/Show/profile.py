#na poźniej
from view import details_profile #szczegóły

class User_profile_controller:
    def __init__(self, user):
        self.data = {
            'name' : user.name,
            'surname' : user.surname,
            'birth_date' : user.birth_date,
            'friends' : user.get_friends(),
            'photos' : user.photos,
            'posts' : user.get_posts(),
            'joined_on' : user.joined_on
        }
    
    def show(self):
        return details_profile(self.data)