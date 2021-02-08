from .comment import Comment
from ..InOut import Output

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

    def _save_comment_to_database(self):
        data_base = Output()
        data_base.update_comments(self.comments)

    def add_comment_to_post(self, comment_data):
        #id liczymy od 0, więc musimy zacząć max_id od -1
        max_id = -1
        for com in self.comments:
            if com.id > max_id:
                max_id = com.id
        
        new_id = max_id + 1
        data = {
            'id' : new_id,
            'parent_id' : comment_data['post_id'],
            'text' : comment_data['text'],
            'is_first_comment' : True,
            'likes' : []
        }
        self.comments.append(Comment(data))
        self._save_comment_to_database()
        return new_id

    def add_comment_to_comment(self, comment_data):
        max_id = -1
        for com in self.comments:
            if com.id > max_id:
                max_id = com.id
        
        new_id = max_id + 1
        data = {
            'id' : new_id,
            'parent_id' : comment_data['comment_id'],
            'text' : comment_data['text'],
            'is_first_comment' : False,
            'likes' : []
        }
        self.comments.append(Comment(data))
        self._save_comment_to_database()
        return new_id

    def delete_comment_by_id(self, id_):
        self.comments = [comment for comment in self.comments if comment.id != id_]
        self._save_comment_to_database()