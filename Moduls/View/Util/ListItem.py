from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label

class ListItem(BoxLayout):
    def __init__(self, data, **kwargs):
        super(ListItem, self).__init__(**kwargs)
        for item in data:
           self.add_widget(Label(
               text = item
           ))

