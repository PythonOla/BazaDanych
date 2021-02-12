from . import like as l
from ..InOut import Output

class Like_list:
    def __init__(self, likes):
        self.likes = []
        for like in likes:
            self.likes.append(l.Like(like))
    
    def get_likes_by_ids(self, ids):
        likes = []
        for l in self.likes:
            if l.id in ids:
                likes.append({
                    'context' : l.get_context(),
                    'user_name' : l.get_name_from_user()
                    })
        return likes

    def _save_like_to_database(self):
        data_base = Output()
        data_base.update_likes(self.likes)

    def like_post_by_id(self, post_id):
        #id liczymy od 0, więc musimy zacząć max_id od -1
        max_id = -1
        for like in self.likes:
            if like.id > max_id:
                max_id = like.id

        new_id = max_id + 1
        data = {
            'id' : new_id,
            'parent_id' : post_id,
            'post_likes' : True,
            'comment_likes' : False
        }
        self.likes.append(l.Like(data))
        self._save_like_to_database()
        return new_id

    def like_comment_by_id(self, comment_id):
        max_id = -1
        for like in self.likes:
            if like.id > max_id:
                max_id = like.id

        new_id = max_id + 1
        data = {
            'id' : new_id,
            'parent_id' : comment_id,
            'post_likes' : False,
            'comment_likes' : True
        }
        self.likes.append(l.Like(data))
        self._save_like_to_database()
        return new_id

    def delete_like_by_id(self, id_):
        self.likes = [like for like in self.likes if like.id != id_]
        self._save_like_to_database()