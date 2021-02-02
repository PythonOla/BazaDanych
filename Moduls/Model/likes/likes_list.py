from like import Like

class Like_list:
    def __init__(self, likes):
        self.likes = []
        for like in likes:
            self.likes.append(Like(like))
    
    def get_likes_by_ids(self, ids):
        likes = []
        for l in self.likes:
            if l.id in ids:
                likes.append({
                    'context' : l.get_context(),
                    'user_name' : l.get_name_from_user()
                    })
        return likes