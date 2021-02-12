from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from ..Menu.Menu import Menu

class UserDataForm(GridLayout):
    def __init__(self, user_data = {}, **kwargs):
        super(UserDataForm, self).__init__(**kwargs)
        self.cols = 2
        self.orientation = "lr-tb"
        self.add_widget(Label(text = "Imię"))
        self.nameWidget = TextInput(text = user_data['name'] if 'name' in user_data else "")
        self.add_widget(self.nameWidget)
        self.add_widget(Label(text = "Nazwisko"))
        self.surnameWidget = TextInput(text = user_data['surname'] if 'surname' in user_data else "")
        self.add_widget(self.surnameWidget)
        self.add_widget(Label(text = "Data Urodzenia"))
        self.dateWidget = TextInput(text = user_data['birth_date'] if 'birth_date' in user_data else "")
        self.add_widget(self.dateWidget)
        self.add_widget(Label(text = "Aktywność"))
        self.activityWidget = TextInput(text = str(user_data['avg_daily_activity']) if 'avg_daily_activity' in user_data else "")
        self.add_widget(self.activityWidget)

    def get_data(self):
        return {
            'name': self.nameWidget.text,
            'surname': self.surnameWidget.text,
            'birth_date': self.dateWidget.text,
            'avg_daily_activity': self.activityWidget.text
        }

class Manage_users(BoxLayout):
    def __init__(self, on_back, on_save, on_delete, user_data, **kwargs):
        super(Manage_users, self).__init__(**kwargs)
        self.orientation = 'horizontal'
        self.form = UserDataForm(user_data = user_data)
        self.add_widget(self.form)
        menu_config = {
            "Powrót": on_back,
            "Zapisz": lambda _: on_save(self.form.get_data())
        }
        if 'id' in user_data:
            menu_config['Usuń'] = on_delete
        self.add_widget(Menu(menu_config))

    
        