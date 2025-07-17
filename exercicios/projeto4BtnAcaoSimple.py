from kivy.app import App
from kivy.uix.button import Button


class projeto4BtnAcao(App):
    def build(self):
        
        return Button()
        
    def on_button_press(self):
        print("Botão pressionado!")
        
if __name__ == '__main__':
    app = projeto4BtnAcao()
    app.run()