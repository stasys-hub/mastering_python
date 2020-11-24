import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class MYGridLayout(GridLayout):
    # Initialize infinite keywords
    def __init__(self, **kwargs):
        # Call Gridlayout constructor
        super(MYGridLayout, self).__init__(**kwargs)

        # set columns -> based on this kivy guesses the layout
        self.cols = 2

        # Add widgets
        self.add_widget(Label(text="Name: "))
        # Add Input Box
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)

        self.add_widget(Label(text="Adress: "))
        # Add Input Box
        self.adress = TextInput(multiline=False)
        self.add_widget(self.adress)

        self.add_widget(Label(text="Pizza: "))
        # Add Input Box
        self.pizza = TextInput(multiline=False)
        self.add_widget(self.pizza)

        # Add a submit button
        self.submit = Button(text="Submit stuff", font_size=32)
        # bind the button 
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)
    
    # we pass an instance of the class
    def press(self, instance):
        name = self.name.text
        pizza = self.pizza.text
        adress = self.adress.text

        # print(f"Your name is {name}, you live in {adress} and you like {pizza}")
        # print to terminal
        self.add_widget(Label(text=f"Your name is {name},you live in {adress} and you like {pizza}"))
        
        # replace everything with empty strings
        self.name.text = ""
        self.pizza.text = ""
        self.adress.text = ""

class MyApp(App):
    def build(self):
        return MYGridLayout()


if __name__ == '__main__':
    MyApp().run()
