from kivy.uix.boxlayout import BoxLayout
from ..Listing.listing import Listing
from kivy.uix.label import Label
from kivy.uix.button import Button

class UserList(BoxLayout):
    def __init__(self, listing_data, on_back, **kwargs):
        super(UserList, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.listing = Listing(listing_data['rows'], listing_data['fields'])
        self.add_widget(Label(text = 'Lista uzytkowników', font_size = 50))
        self.add_widget(self.listing)
        self.add_widget(Button(text = 'Powrót', on_press = on_back))