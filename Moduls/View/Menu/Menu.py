from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class Menu(BoxLayout):
    def __init__(self, options, **kwargs):
        super(Menu, self).__init__(
            orientation = 'vertical',
            spacing = 30,
            **kwargs
        )
        for (label, callback) in options.items():
            self.add_widget(Button(
                text = label,
                on_press = callback
            ))       