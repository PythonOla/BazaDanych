from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from ..Menu.Menu import Menu
from ...Model.InOut.Input import Input

class UserMenu(BoxLayout):
    def __init__(self, id, on_back, **kwargs):
        super(UserMenu, self).__init__(**kwargs)
        self.orientation = 'vertical'
        name = Input().user_list.get_names_by_ids([int(id)])[0]
        self.add_widget(Label(
            text = name,
            font_size = 50
        ))
        self.add_widget(Menu({
            "Zarządzaj Uzytkownikiem": lambda _: print("Zarządzanie"),
            "Obejrzyj profil": lambda _: print("Profil"),
            "Obejrzyj aktywność": lambda _: print("Aktywność"),
            "Powrót": on_back
        }))