#To bedziemy uruchamiac
from Moduls.View.Menu.Menu import Menu

import kivy as kiwi
kiwi.require('2.0.0')

from kivy.app import App
from kivy.uix.widget import Widget

class Baza(Widget):

    def __init__(self):
        self.changeOptions1()

    def changeOptions1(self):
        self.root = Menu({
            "Click": self.changeOptions2,
            "Not Click": self.nonClick
        })

    def changeOptions2(self):
        self.root = Menu({
            "Click me too": self.changeOptions1,
            "Don't click me either": self.nonClick 
        })
    
    def nonClick(self):
        print('Told you not to click :*')

class MainApp(App):
    def build(self):
        return Baza()
    
MainApp().run()