

class Like:
    def __init__(self, data):
       self.id = data["id"]
       self.parent_id = data["parent_id"]
       self.comments_likes = data["comments_likes"]
       self.posts_likes = data["posts_likes"]

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return self.id != other.id