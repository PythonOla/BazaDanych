

class Post:
    def __init__(self, data):
        self.id = data["id"]
        #kto lajkuje i ile (długość listy)
        self.likes = data["likes"]
        self.comments = data["comments"]
        self.text = data["text"]
        self.attachments = data["attachments"]

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return self.id != other.id

    def get_comments(self):
        #verify
        base = Input()
        return base.comments_list.get_comments_by_ids(self.comments)

    def how_many_likes(self):
        return len(self.likes)