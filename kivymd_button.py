from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivymd.uix.button import MDFillRoundFlatIconButton
from kivymd.uix.textfield import MDTextField
#from kivymd.app import MDApp

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
            hint_text: 'Write your name'
            size_hint_y: None
            height: self.minimum_height

        MDLabel:
            text: 'Surname'
            size_hint_y: None
            height: self.texture_size[1]

        MDTextField:
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
                

'''

class MyApp(MDApp):
    title="Botões"
    Window.size = (300, 300)
    
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Orange"
        return Builder.load_string(KV)

    def save_data(self):
        # Code to save data goes here
        pass
    
    def clear_data(self):
        # Code to save data goes here
        pass

MyApp().run()
