from .post import Post
from ..InOut import Output

class Posts_list:
    def __init__(self, posts):
        self.posts = []
        for post in posts:
            self.posts.append(Post(post))

    def get_posts_by_ids(self, ids):
        posts = []
        for post in self.posts:
            if post.id in ids:
                posts.append({
                    'likes' : post.how_many_likes(),
                    'comments' : post.get_comments(),
                    'text' : post.text,
                    'attachments' : post.attachments
                    })
        return posts

    def get_post_by_id(self, id_):
        return self.get_posts_by_ids(id_)[0] 

    def _save_post_to_database(self):
        data_base = Output()
        data_base.update_posts(self.posts)

    def add_post(self, data):
        #id liczymy od 0, więc musimy zacząć max_id od -1
        max_id = -1
        for post in self.posts:
            if post.id > max_id:
                max_id = post.id

        new_id = max_id + 1
        data['id'] = new_id 
        data['likes'] = []
        data['comments'] = []
        self.posts.append(Post(data))
        self._save_post_to_database()
        return new_id

    def delete_post_by_id(self, id_):
        self.posts = [post for post in self.posts if post.id != id_]
        self._save_post_to_database()