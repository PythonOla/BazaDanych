from post import Post

class Posts_list:
    def __init__(self, posts):
        self.posts = []
        for post in posts:
            self.posts.append(Post(post))