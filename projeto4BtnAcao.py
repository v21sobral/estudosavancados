from kivy.app import App
from kivy.uix.button import Button


class MainApp(App):
    def build(self):
        
        button = Button(text='Clique aqui', size_hint=(.5, .5), pos_hint={'center_x': .5, 'center_y': .5})
        button.bind(on_press=self.on_button_press)
        
        return button
        
    def on_button_press(self, instance):
        print("Botão pressionado!")
        
if __name__ == '__main__':
    app = MainApp()
    app.run()