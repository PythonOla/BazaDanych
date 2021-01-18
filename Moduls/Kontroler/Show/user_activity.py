#na poźniej
from view import details_activity #szczegóły

class User_activity_controller:
    def __init__(self, user):
        self.data = {
            'ids' : user.id,
            'likes' : user.get_likes(),
            'posts' : user.get_posts(),
            'comments' : user.get_comments(),
            'daily_avg' : user.avg_daily_activity,
            'joined_on' : user.joined_on
        }
    
    def show(self):
        return details_activity(self.data)