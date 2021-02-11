from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from ..KVList.KVList import KVList

class Profile(BoxLayout):
    def __init__(self, user_data, on_back, **kwargs):
        super(Profile, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(
            text = user_data['name'] + user_data['surname'],
            font_size = 50
        ))
        self.add_widget(KVList({
            "Data Urodzenia": user_data['birth_date'],
            "Znajomi": user_data['friends'] if len(user_data['friends']) < 5 else user_data['friends'][:5],
            "Zdjęcia": user_data['photos'],
            "Ostatnie posty": user_data['posts'] if len(user_data['posts'] < 5) else user_data['posts'][-4:],
            "Dołączył": user_data['joined_on']
        }))
        self.add_widget(Button(
            text = "Powrót",
            on_press = on_back
        ))