#na poźniej
from view import details_comment #szczegóły

class Comment_details_controller:
    def __init__(self, comment, author):
        
        self.data = {
            'author' : author,
            'text' : comment.text,
            'number_of_likes' : len(comment.likes),
            'context' : comment.get_context(),
        }

    def show(self):
        return details_comment(self.data)