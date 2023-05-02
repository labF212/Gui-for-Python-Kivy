from kivymd.app import MDApp
from kivymd.uix.boxlayout import BoxLayout
from kivymd.uix.label import MDLabel, MDIcon
from kivy.clock import Clock
import random

class TemperatureHumidityApp(MDApp):
    title = 'Medição de Variáveis'
    
    def build(self):
        self.theme_cls.primary_palette = "Brown"
        
        # Create a BoxLayout to hold the labels
        box_layout = BoxLayout(orientation='vertical', size_hint=(0.5, None))
        
        # Create a nested BoxLayout for each row
        temperature_row = BoxLayout(orientation='horizontal', size_hint=(1, None), height=25)
        humidity_row = BoxLayout(orientation='horizontal', size_hint=(1, None), height=25)
        
        # Create an Icon for the thermometer
        #https://pictogrammers.com/library/mdi/
        temperature_icon = MDIcon(icon='thermometer')
        
        # Create an Icon for the humidity
        humidity_icon = MDIcon(icon='water-percent',
            halign="center",
            size_hint = (0.5,1),
            pos_hint = {"center_x": 0.5, "center_y":0.5},
            font_size = 55
                               )
        
        # Create a Label for the temperature value
        self.temperature_label = MDLabel(text='Temperature{}°C'.format(random.randint(20,50)),
            halign="center",
            size_hint = (0.3,1),
            pos_hint = {"center_x": 0.5, "center_y":0.5},
            font_size = 22                                        
                                         )
        
        # Create a Label for the humidity value
        self.humidity_label = MDLabel(text='Humidity: {}%'.format(random.randint(20,80)),
            halign="center",
            size_hint = (0.3,1),
            pos_hint = {"center_x": 0.5, "center_y":0.5},
            font_size = 22                                        
                                         )
                                      
        
        # Add the Icons and Labels to their respective rows
        temperature_row.add_widget(temperature_icon)
        temperature_row.add_widget(self.temperature_label)
        humidity_row.add_widget(humidity_icon)
        humidity_row.add_widget(self.humidity_label)
        
        # Add the rows to the BoxLayout
        box_layout.add_widget(temperature_row)
        box_layout.add_widget(humidity_row)
        
        # Schedule a function to update the values every 1 second
        Clock.schedule_interval(self.update_values, 1)
        
        return box_layout
    
    def update_values(self, dt):
        # Update the temperature value
        self.temperature_label.text = '{}°C'.format(random.randint(20,50))
        
        # Update the humidity value
        self.humidity_label.text = 'Humidity: {}%'.format(random.randint(20,80))


if __name__ == '__main__':
    TemperatureHumidityApp().run()
