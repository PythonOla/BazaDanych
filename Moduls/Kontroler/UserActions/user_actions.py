from ...Model.Users import User
from ...Model.InOut import Input 

class User_actions:
    def __init__(self, data):
        self.User = data

    def add_post(self, text = '', attachments = []):
        post_data = {
            'text' : text,
            'attachments' : attachments
        }
        data_base = Input()
        post_id = data_base.posts_list.add_post(post_data)
        self.User.post_created(post_id)

    def delete_post(self, id_):
        #to do
        data_base = Input()
        data_base.posts_list.delete_post_by_id(id_)
        self.User.post_deleted(id_)

    def add_coment_to_post(self):
        #to do
        pass

    def add_reply_coment(self):
        #to do 
        pass

    def delete_commen(self):
        #to do
        pass

    def add_photo(self):
        #to do
        pass

    def delete_photo(self):
        #to do 
        pass

    def like_to_post(self):
        #to do 
        pass

    def like_to_comment(self):
        #to do 
        pass

    def unlike(self):
        #to do 
        pass