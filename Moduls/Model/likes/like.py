from ..InOut.Input import Input

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

    def get_context(self):
        base = Input()
        if self.posts_likes:
            return base.posts_list.get_post_by_id(self.parent_id)
        elif self.comments_likes:
            return base.comments_list.get_comment_by_id(self.parent_id)
        else:
            return None

    def get_name_from_user(self):
        base = Input()
        return base.user_list.get_names_by_condition(
            lambda usr: self.id in usr.likes
        )[0]
