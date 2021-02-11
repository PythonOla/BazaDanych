from kivy.uix.boxlayout import BoxLayout
from ..Util.ListItem import ListItem

class Listing(BoxLayout):
    def __init__(self, data, fields, **kwargs):
        super(Listing, self).__init__(
            orientation = 'vertical',
            spacing = 5,
            **kwargs
        )
        self.add_widget(ListItem(fields))
        for data_item in data:
            data_fields = []
            for field in fields:
                data_fields.append(data_item[field])
            self.add_widget(
                ListItem(data_fields)
            )