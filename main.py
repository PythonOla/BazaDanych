#To bedziemy uruchamiac
from Moduls.View.Menu.Menu import Menu
from Moduls.View.Util.ListItem import ListItem
from Moduls.View.Listing.listing import Listing
from Moduls.Kontroler.Show.users_list import User_list_controller

import kivy as kiwi
kiwi.require('2.0.0')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

fields = ['a', 'b', 'c']
testData = [{
    'a': 'Ola',
    'b': 'Gryza',
    'c': 'Grzesia'
},
{
    'a': 'Ola',
    'b': 'Gryza',
    'c': 'Grzyba'
},
{
    'a': 'Decussata',
    'b': 'Tez',
    'c': 'Gryza'
}
]

class Baza(BoxLayout):

    def __init__(self, **kwargs):
        super(Baza, self).__init__(**kwargs)
        self.changeOptions1()

    def changeOptions1(self, *args):
        self.clear_widgets()
        self.add_widget(Menu({
            "Click": self.changeOptions2,
            "Not Click": self.nonClick
        }))

    def changeOptions2(self, *args):
        self.clear_widgets()
        self.add_widget(Menu({
            "Click me too": self.changeOptions1,
            "Don't click me either": self.nonClick 
        }))
    
    def nonClick(self, *args):
        self.clear_widgets()
        l = User_list_controller()
        self.add_widget(l.show())
class MainApp(App):
    def build(self):
        return Baza()
    
MainApp().run()