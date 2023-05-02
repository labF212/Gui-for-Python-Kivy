from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.clock import Clock
import random

class TemperatureHumidityApp(App):
    title = 'Medição de Variáveis'
    
    def build(self):
        # Create a BoxLayout to hold the labels
        box_layout = BoxLayout(orientation='vertical')
        
        # Create a Label for the temperature value
        self.temperature_label = Label(text='Temperature: {}°C'.format(random.randint(20,50)))
        
        # Create a Label for the humidity value
        self.humidity_label = Label(text='Humidity: {}%'.format(random.randint(20,80)))
        
        # Add the labels to the BoxLayout
        box_layout.add_widget(self.temperature_label)
        box_layout.add_widget(self.humidity_label)
        
        # Schedule a function to update the values every 1 second
        Clock.schedule_interval(self.update_values, 1)
        
        return box_layout
    
    def update_values(self, dt):
        # Update the temperature value
        self.temperature_label.text = 'Temperature: {}°C'.format(random.randint(20,50))
        
        # Update the humidity value
        self.humidity_label.text = 'Humidity: {}%'.format(random.randint(20,80))

if __name__ == '__main__':
    TemperatureHumidityApp().run()
