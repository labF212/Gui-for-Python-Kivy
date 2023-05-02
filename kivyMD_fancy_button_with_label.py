# https://github.com/kivy-garden/garden.knob/tree/master
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.garden.knob import Knob
from kivy.properties import StringProperty, NumericProperty


class KnobWithLabel(Knob):
    label_text = StringProperty("")
    voltage = NumericProperty(0)

    def __init__(self, **kwargs):
        super(KnobWithLabel, self).__init__(**kwargs)
        self.bind(value=self.update_label_text)
        self.update_label_text()

    def update_label_text(self, *args):
        voltage = round(self.value * 5 / 360, 2)
        self.voltage = voltage
        self.label_text = f"{voltage}V"


# LOAD KV UIX

KV = '''
<Main>:
    GridLayout:
        pos: root.pos
        size: root.size
        cols: 3
        spacing: 100
        padding: 50

        KnobWithLabel:
            min:0
            max:360
            size: 200, 200
            value: 0
            show_marker: True
            knobimg_source: "knob_metal.png"
            show_marker: False

<KnobWithLabel>:
    label_text: "0V"
    
    Label:
        text: root.label_text
        center: self.parent.center
        font_size: 20
        color: 0.1, 0.1, 0.1, 1
'''

Builder.load_string(KV)


class Main(GridLayout):
    pass


class MyApp(App):
    title = "Fancy Buttons"

    def build(self):
        root_widget = Main()
        return root_widget


if __name__ == '__main__':
    MyApp().run()
