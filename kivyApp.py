from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from password import generate

class KivyApp(App):
    def build(self):
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.8, 0.9)
        self.window.pos_hint = {'center_x':0.5, 'center_y':0.5}
        Window.size = (360, 640)

        #Spazio vuoto
        self.window.add_widget(Label(
            text = 'Password Generator',
            font_size = '30sp',
            color = 'ebffff',
            bold = True
            ))

        #Pulsante
        self.button = Button(
            text = 'Generate',
            size_hint = (2,0.3),
            bold = True,
            background_color = '42c6ff',
            color = 'ebffff'
            )
        self.window.add_widget(self.button)
        self.button.bind(on_press=self.output)

        #Label
        self.label = Label(
            text = '',
            font_size = '30sp',
            color = 'ebffff'
            )
        self.window.add_widget(self.label)
        
        return self.window

    def output(self, instance):
        self.label.text = generate(16)


KivyApp().run()
    
