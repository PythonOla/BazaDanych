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

    def _update_self_in_database(self):
        base = Input()
        base.user_list.update_users_by_id(self.id, self)

    def post_created(self, id_):
        self.posts.append(id_)
        self._update_self_in_database()

    def comment_created(self, id_):
        self.comments.append(id_)
        self._update_self_in_database()

    def post_deleted(self, id_):
        self.posts = [post for post in self.posts if post.id != id_]
        self._update_self_in_database()

    def comment_deleted(self, id_):
        self.comments = [comment for comment in self.comments if comment.id != id_]
        self._update_self_in_database()

    def photo_added(self, url):
        self.photos.append(url)
        self._update_self_in_database()

    def photo_deleted(self, url):
        self.photos = [photo for photo in self.photos if photo != url]
        self._update_self_in_database()

    def liked(self, id_):
        self.likes.append(id_)
        self._update_self_in_database()

    def unliked(self, id_):
        self.likes = [like for like in self.likes if like != id_]
        self._update_self_in_database()
        