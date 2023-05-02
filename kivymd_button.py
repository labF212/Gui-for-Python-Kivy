from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel

KV = '''
BoxLayout:
    orientation: 'vertical'

    GridLayout:
        cols: 2
        padding: dp(20)
        spacing: dp(20)
        size_hint: 1, 0.6
        height: self.minimum_height

        MDLabel:
            text: 'Name'
            size_hint_y: None
            height: self.texture_size[1]

        MDTextField:
            id: name
            hint_text: 'Write your name'
            size_hint_y: None
            height: self.minimum_height

        MDLabel:
            text: 'Surname'
            size_hint_y: None
            height: self.texture_size[1]

        MDTextField:
            id: surname
            hint_text: 'Write your surname'
            size_hint_y: None
            height: self.minimum_height

        MDLabel:
            size_hint_y: None
            height: self.texture_size[1]

        GridLayout:
            cols: 2
            size_hint: 1, 0

        MDFillRoundFlatIconButton:
            icon: 'content-save'
            text: 'Save'
            on_press: app.save_data()

        MDFillRoundFlatIconButton:
            icon: 'eraser'
            text: 'Clear'
            on_press: app.clear_data()

    MDLabel:
        id: name_surname_label
        text: ''
        size_hint_y: None
        height: self.texture_size[1]
        halign: 'center'
        valign: 'center'
'''

class MyApp(MDApp):
    title = "Buttons"
    Window.size = (300, 400)

    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        self.root = Builder.load_string(KV)
        return self.root

    def save_data(self):
        name = self.root.ids.name.text
        surname = self.root.ids.surname.text
        name_surname_label = self.root.ids.name_surname_label
        name_surname_label.text = f"{name} {surname}"

    def clear_data(self):
        self.root.ids.name.text = ''
        self.root.ids.surname.text = ''
        name_surname_label = self.root.ids.name_surname_label
        name_surname_label.text = ''

MyApp().run()
