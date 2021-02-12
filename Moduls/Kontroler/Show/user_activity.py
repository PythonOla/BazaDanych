from ...View.Activity.Activity import Activity
from ...Model.InOut.Input import Input

class User_activity_controller:
    def __init__(self, id_, *args):
        self.args = args
        user = Input().user_list.get_user_by_id(id_)
        self.data = {
            'name' : user.name,
            'surname': user.surname,
            'likes' : user.get_likes(),
            'posts' : user.get_posts(),
            'comments' : user.get_comments(),
            'daily_avg' : user.avg_daily_activity,
            'joined_on' : user.joined_on
        }
    
    def show(self):
        return Activity(self.data, *self.args)