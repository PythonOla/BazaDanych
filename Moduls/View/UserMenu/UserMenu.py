from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from ..Menu.Menu import Menu
from ...Model.InOut.Input import Input
from ...Kontroler.Show.profile import User_profile_controller

class UserMenu(BoxLayout):
    def __init__(self, id, on_back, **kwargs):
        super(UserMenu, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.id = str(id)
        self.on_back = on_back
        self.name = Input().user_list.get_names_by_ids([int(id)])[0]
        self.back_here()
        
    def back_here(self, *args):
        self.clear_widgets()
        self.add_widget(Label(
            text = self.name,
            font_size = 50
        ))
        self.add_widget(Menu({
            "Zarządzaj Uzytkownikiem": lambda _: print("Zarządzanie"),
            "Obejrzyj profil": self.open_profile,
            "Obejrzyj aktywność": lambda _: print("Aktywność"),
            "Powrót": self.on_back
        }))

    def open_profile(self, *args):
        pr = User_profile_controller(self.id, self.back_here).show()
        self.clear_widgets()
        self.add_widget(pr)
        
