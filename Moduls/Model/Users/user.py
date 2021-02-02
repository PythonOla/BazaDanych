from ..InOut import Input

class User:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.surname = data["surname"]
        self.birth_date = data["birth_date"]
        self.friends = data["friends"]
        self.photos = data["photos"]
        self.likes = data["likes"]
        self.posts = data["posts"]
        self.comments = data["comments"]
        self.avg_daily_activity = data["avg_daily_activity"]
        self.joined_on = data["joined_on"]

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return self.id != other.id

    def get_likes(self):
        #verify
        base = Input()
        return base.likes_list.get_likes_by_ids(self.likes)

    def get_comments(self):
        base = Input()
        return base.comments_list.get_comments_by_ids(self.comments)

    def get_posts(self):
        base = Input()
        return base.posts_list.get_posts_by_ids(self.posts)

    def get_friends(self):
        #1. dostać się do bazy + TO DO ŚCIEZKA
        base = Input()
        return base.user_list.get_names_by_ids(self.friends)

     