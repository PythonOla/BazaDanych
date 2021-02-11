from ...View.Profile.Profile import Profile
from ...Model.InOut.Input import Input

class User_profile_controller:
    def __init__(self, _id, *args):
        self.args = args
        user = Input().user_list.get_user_by_id(_id)
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
        return Profile(self.data, self.args[0])