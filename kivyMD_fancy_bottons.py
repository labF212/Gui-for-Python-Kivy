
from kivy.app import App
from kivy.base import runTouchApp
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.garden.knob import Knob

# https://github.com/kivy-garden/garden.knob/tree/master

# LOAD KV UIX


KV = '''

<Main>:
    GridLayout:
        pos: root.pos
        size: root.size
        cols: 3
        spacing: 100
        padding: 50

        Knob:
            min:4
            max:5
            size: 200, 200
            value: 0
            show_marker: True
            knobimg_source: "knob_metal.png"
            show_marker: False

        Knob:
            size: 200, 200
            value: 0
            show_marker: True
            knobimg_source: "knob_metal.png"
            marker_img: "bline.png"
            markeroff_color: 0.3, 0.3, .3, 1

        Knob:
            size: 200, 200
            value: 0
            show_marker: True
            knobimg_source: ""
            knobimg_color: 0, 0, 0, 0
            marker_img: "bline.png"
            markeroff_color: 0, 0, 0, 0
            marker_inner_color: 0, 0, 0, 1

        Knob:
            size: 200, 200
            value: 0
            show_marker: True
            knobimg_source: "knob_metal.png"
            marker_img: "bline.png"
            markeroff_color: 0.0, 0.0, .0, 1
            knobimg_size: 0.7

        Knob:
            size: 200, 200
            step: 25
            value: 10
            show_marker: True
            knobimg_source: "knob_metal.png"
            marker_img: "bline2.png"
            markeroff_img: "bline2_off.png"
            markeroff_color: 0.3, 0.3, .3, 1
            marker_ahead: 6
            knobimg_size: 0.8
            marker_startangle: 6

        Knob:
            size: 200, 200
            value: 0
            knobimg_source: "knob_black.png"
            markeroff_color: 0.0, 0.0, .0, 1
            knobimg_size: 0.9
            marker_img: "bline3.png"
'''

Builder.load_string(KV)


class Main(GridLayout):
    pass


class MyApp(App):
    def build(self):
        root_widget = Main()
        return root_widget


if __name__ == '__main__':
    MyApp().run()
