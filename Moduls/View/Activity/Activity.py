from ..KVList.KVList import KVList
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class Activity(BoxLayout):
    def __init__(self, user_data, on_back, **kwargs):
        super(Activity, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(
            text = "Aktywność " + user_data['name'] + " " + user_data['surname'],
            font_size = 50
        ))
        print(user_data)
        self.add_widget(KVList({
            "Polubienia": str(len(user_data['likes'])),
            "Ostatnie Posty": self.posts_to_readable(
                user_data['posts'] if len(user_data['posts']) < 5 else user_data['posts'][:5]
            ),
            "Ostatenie Komentarze": self.posts_to_readable(
                user_data['comments'] if len(user_data['comments']) < 5 else user_data['comments'][:5]
            ),
            "Średnia Aktywność": str(user_data['daily_avg']),
        }, spacing = 20))
        self.add_widget(Button(
            text = "Powrót",
            on_press = on_back
        ))
    
    def posts_to_readable(self,posts):
        if len(posts) == 0:
            return "Brak"
        sep = "\n" + 20 * "-" + "\n"
        prepared = map(lambda post: str(post['text']) + "\nPolubień: " + str(post['likes']), posts)
        return sep + sep.join(prepared) + sep
