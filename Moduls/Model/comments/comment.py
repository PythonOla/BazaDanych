from ..InOut import Input 

class Comment:
    def __init__(self, data):
        self.id = data["id"]
        #id postu lub wczesniejszego komenatarza
        self.parent_id = data["parent_id"]
        #kto lajkuje i ile (długość listy)
        self.likes = data["likes"]
        self.is_first_comment = data["is_first_comment"]
        self.text = data["text"]

#getter -> uruchamia się podczas dostawania się do is first comment
    @property
    def is_first_comment(self):
        return self.__is_first_comment
    
#setter -> uruchamia się gdy chcemy zmienic wartosc is first comment
    @is_first_comment.setter
    def is_first_comment(self, is_first):
        self.__is_first_comment = is_first

    @property
    def is_reply_comment(self):
        return not self.__is_first_comment
    
    @is_reply_comment.setter
    def is_reply_comment(self, is_reply):
        self.__is_first_comment = not is_reply

    def __eq__(self, other):
        return self.id == other.id

    def __ne__(self, other):
        return self.id != other.id

    def get_context(self):
        base = Input()
        if self.is_first_comment:
            return base.posts_list.get_post_by_id(self.parent_id)
        #jeśli odpowiedź -> ściągamy kometarz do którego się odnosi
        else:
            return base.comments_list.get_comment_by_id(self.parent_id)

        