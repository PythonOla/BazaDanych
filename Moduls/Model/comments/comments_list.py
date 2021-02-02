from .comment import Comment

class Comments_list:
    def __init__(self, comments):
        self.comments = []
        for com in comments:
            self.comments.append(Comment(com))

    def get_comments_by_ids(self, ids):
        comments = []
        for com in self.comments:
            if com.id in ids:
                comments.append({
                    'likes' : com.how_many_likes(),
                    'text' : com.text,
                    'context' : com.get_context()
                    })
        return comments

    def get_comment_by_id(self, id_):
          return self.get_comments_by_ids(id_)[0] 

   