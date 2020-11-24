import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

# This corresponds to the my.kv file


class MyGrid(Widget):
    # empty until we read them in from kivy file
    name = ObjectProperty(None)
    email = ObjectProperty(None)
    # widget has default size <- specify in my.kv

    def btn(self):
        # print out message referenced in my.kv 
        print(f"My name is: {self.name.text} and my email: {self.email.text}")
        # now we need to clear the widgets
        self.name.text = ""
        self.email.text = ""


class MyApp(App):
    def build(self):
        return MyGrid()


if __name__ == "__main__":
    MyApp().run()
