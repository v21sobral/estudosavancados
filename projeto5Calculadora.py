from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

class MainApp(App):
    def build(self):
        self.operators = ['+', '-', '*', '/']
        self.last_was_operator = None
        self.last_button = None
        
        main_layout = BoxLayout(orientation='vertical')
        self.solution = TextInput(
            multiline=False, readonly=True, halign='right', font_size=55)
    
        main_layout.add_widget(self.solution)
        
        buttons = [
            ['C', '(', ')', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=', '=']  # Removido o botão duplicado
        ]
        
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(text=label, pos_hint={'center_x': 0.5, 'center_y': 0.5})
                
                # Conectar ao método correto baseado no botão
                if label == '=':
                    button.bind(on_press=self.on_solution)
                else:
                    button.bind(on_press=self.on_button_press)
                    
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)
            
        return main_layout
    
    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text
        
        if button_text == "C":
            self.solution.text = ""
        else:
            if current and (self.last_was_operator and button_text in self.operators):
                return
            elif current == "" and button_text in self.operators:
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
                
        self.last_button = button_text
        self.last_was_operator = button_text in self.operators
                
    def on_solution(self, instance):
        text = self.solution.text
        if text:
            try:
                solution = str(eval(self.solution.text))
                self.solution.text = solution
            except:
                self.solution.text = "Erro"

# Para executar a aplicação
if __name__ == '__main__':
    MainApp().run()