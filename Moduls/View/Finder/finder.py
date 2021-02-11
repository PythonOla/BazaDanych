from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from ..Menu.Menu import Menu
from kivy.uix.label import Label

class Finder(BoxLayout):
    def __init__(self, on_search, on_back, **kwargs):
        super(Finder, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(
            text = "Wyszukaj uzytkownika wg ID",
            font_size = 36
        ))
        self.txt_input = TextInput()
        self.add_widget(self.txt_input)
        self.add_widget(Menu({
            "Szukaj": lambda _: on_search(self.txt_input.text),
            "Powrót": on_back
        }))