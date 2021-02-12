from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class KeyField(Label):
    def __init__(self, **kwargs):
        super(KeyField, self).__init__(**kwargs)
        self.size_hint = (0.25, 1)

class ValueField(Label):
    def __init__(self, **kwargs):
        super(ValueField, self).__init__(**kwargs)
        self.size_hint = (0.75, 3)

class KVList(GridLayout):
    def __init__(self, data, **kwargs):
        super(KVList, self).__init__(**kwargs)
        self.cols = 2
        self.orientation = 'lr-tb'
        for (key, value) in data.items():
            self.add_widget(KeyField(
                text = key
            ))
            print(key, value)
            self.add_widget(ValueField(
                text = value,        
            ))
        

