from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''

MDScreen:
    
    MDBoxLayout:
        orientation: "vertical"
        
        MDTopAppBar:
            title: "MDLabel at topAppBar"
            icon: "git"
            shadow_color: "brown"
            anchor_title: "left"
            elevation: 4
            

        MDLabel:
            text: "MDLabel"
            halign: "center"
            font_size: 70
            center_x: root.width / 4
            top: root.top - 50
        
        
        
       
'''


class Test(MDApp):
    title = 'Labels in KivyMD'
    def build(self):
        
        return Builder.load_string(KV)


Test().run()