from comment import Comment

class Comments_list:
    def __init__(self, comments):
        self.comments = []
        for com in comments:
            self.comments.append(Comment(com))

