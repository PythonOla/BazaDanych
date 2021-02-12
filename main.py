#To bedziemy uruchamiac
from Moduls.View.Menu.Menu import Menu
from Moduls.View.Util.ListItem import ListItem
from Moduls.View.Listing.listing import Listing
from Moduls.View.Finder.finder import Finder
from Moduls.View.UserMenu.UserMenu import UserMenu
from Moduls.Kontroler.Show.users_list import User_list_controller


import kivy as kiwi
kiwi.require('2.0.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout


class Baza(BoxLayout):

    def __init__(self, **kwargs):
        super(Baza, self).__init__(**kwargs)
        self.createOptions()

    def createOptions(self, *args):
        self.clear_widgets()
        self.add_widget(Menu({
            "Przeglądaj uzytkowników": self.list_users,
            "Znajdz uzytkownika": self.find_user
        }))

    def open_user_menu(self, id):
        self.clear_widgets()
        self.add_widget(UserMenu(id, self.find_user))

    def find_user(self, *args):
        self.clear_widgets()
        self.add_widget(Finder(self.open_user_menu, self.createOptions))
    
    def list_users(self, *args):
        self.clear_widgets()
        l = User_list_controller(self.createOptions)
        self.add_widget(l.show())
        
class MainApp(App):
    def build(self):
        return Baza()
    
MainApp().run()