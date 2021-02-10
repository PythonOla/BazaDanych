from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class Menu(Widget):
    def __init__(self, options):
        self.root = GridLayout(cols = 3)
        print(options)
        for (label, callback) in options:
            self.root.add_widget(Button(
                text = label,
                onTouchDown = callback
            ))