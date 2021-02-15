#To bedziemy uruchamiac
from Moduls.View.Menu.Menu import Menu
from Moduls.View.Util.ListItem import ListItem
from Moduls.View.Listing.listing import Listing
from Moduls.View.UserMenu.UserMenu import UserMenu
from Moduls.Kontroler.Show.users_list import User_list_controller
from Moduls.Kontroler.User.user import User_controller
from Moduls.Kontroler.Show.user_search import User_search_controller


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
            "Znajdz uzytkownika": self.find_user_by_id,
            "Wyszukaj po nazwie": self.find_user_by_name,
            "Nowy uzytkownik": self.add_user
        }))

    def open_user_menu(self, id):
        self.clear_widgets()
        self.add_widget(UserMenu(id, self.createOptions))

    def find_user_by_id(self, *args):
        self.clear_widgets()
        us = User_search_controller()
        self.add_widget(us.show_id_search(self.open_user_menu, self.createOptions))
    
    def find_user_by_name(self, *args):
        self.clear_widgets()
        us = User_search_controller()
        self.add_widget(us.show_name_search(self.open_user_menu, self.createOptions))
    
    def list_users(self, *args):
        self.clear_widgets()
        l = User_list_controller(self.createOptions)
        self.add_widget(l.show())

    def add_user(self, *args):
        self.clear_widgets()
        usr = User_controller()
        self.add_widget(usr.show(self.createOptions))

        
class MainApp(App):
    def build(self):
        return Baza()
    
MainApp().run()