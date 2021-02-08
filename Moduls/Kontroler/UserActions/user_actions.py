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
        data_base = Input()
        data_base.posts_list.delete_post_by_id(id_)
        self.User.post_deleted(id_)

    def add_comment_to_post(self, text, post_id):
        data_base = Input()
        comment_data = {
            'text' : text,
            'post_id' : post_id
        }
        comment_id = data_base.comments_list.add_comment_to_post(comment_data)
        self.User.comment_created(comment_id)

    def add_reply_coment(self, text, comment_id):
        data_base = Input()
        comment_data = {
            'text' : text,
            'comment_id' : comment_id
        }
        comment_id = data_base.comments_list.add_comment_to_comment(comment_data)
        self.User.comment_created(comment_id)

    def delete_comment(self, id_):
        data_base = Input()
        data_base.comments_list.delete_comment_by_id(id_)
        self.User.comment_deleted(id_)

    def add_photo(self, url):
        self.User.photo_added(url)

    def delete_photo(self, url):
        self.User.photo_deleted(url)

    def like_to_post(self, post_id):
        data_base = Input()
        like_id = data_base.likes_list.like_post_by_id(post_id)
        self.User.liked(like_id)

    def like_to_comment(self, comment_id):
        data_base = Input()
        like_id = data_base.likes_list.like_comment_by_id(comment_id)
        self.User.liked(like_id)

    def unlike(self, id_):
        data_base = Input()
        data_base.likes_list.delete_like_by_id(id_)
        self.User.unliked(id_)