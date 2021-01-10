from like import Like

class Like_list:
    def __init__(self, likes):
        self.likes = []
        for like in likes:
            self.likes.append(Like(like))