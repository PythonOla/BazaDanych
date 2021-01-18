from view import details_post #szczegóły

class Posts_details_controller:
    def __init__(self, post, author):
        self.data = {
            'author' : author,
            'text' : post.text,
            'number_of_likes' : len(post.likes),
            'comments' : post.get_comments(),
            'attachments' : post.attachments
        }

    def show(self):
        return details_post(self.data)