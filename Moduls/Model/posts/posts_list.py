from .post import Post

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