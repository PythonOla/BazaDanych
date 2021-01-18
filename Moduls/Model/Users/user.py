

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
        #to do
        pass

    def get_comments(self):
        pass

    def get_posts(self):
        pass

    def get_friends(self):
        pass

     