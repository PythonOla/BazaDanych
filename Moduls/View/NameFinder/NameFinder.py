from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from ..Menu.Menu import Menu
from kivy.uix.label import Label

class NameFinder(BoxLayout):
    def __init__(self, on_search, on_back, on_update, **kwargs):
        super(NameFinder, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.add_widget(Label(
            text = "Wyszukaj uzytkownika po nazwie",
            font_size = 36
        ))
        self.txt_input = TextInput()
        self.add_widget(self.txt_input)
        self.found_user = Label(
            text = "Tutaj pojawi się znaleziony uzytkownik",
            font_size = 36
        )
        self.add_widget(self.found_user)
        self.txt_input.bind(text = self.fuzzySearch)
        self.on_update = on_update
        self.on_search = on_search
        self.found = {
            'id': None
        }
        self.add_widget(Menu({
            "Przejdz do uzytkownika": self.open_user,
            "Powrót": on_back
        }))

    def fuzzySearch(self, instance, text):
        self.found = self.on_update(text)
        if self.found['id'] == None:
            self.found_user.text = "Brak uzytkownika"
        else:
            self.found_user.text = self.found['name_and_surname']

    def open_user(self, *args):
        if self.found['id'] == None:
            return
        else:
            self.on_search(self.found['id'])
            
