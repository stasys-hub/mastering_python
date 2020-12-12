import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line 


class Touch(Widget):

    # insert an rectangle -> conctructor
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        # use canvas to draw it and change colors to red
        with self.canvas:
            # draw a Line 
            Color(1, 0.3, 0.7, 0.6, mode='rgba')
            self.line = Line(points=(20, 30, 400, 500, 30, 300))
            Color(1, 0, 0, 0.5, mode='rgba')
            # specify psoition
            self.rect = Rectangle(pos=(0, 0), size=(50, 50))
            # create a second rectangle
            #Color(1, 1, 0, 0.3, mode='rgba')
            # specify psoition
            #self.rect = Rectangle(pos=(250, 250), size=(100, 50))
    btn = ObjectProperty(None)

    def on_touch_down(self, touch):
        print("Mouse down", touch)
        self.rect.pos = touch.pos

    def on_touch_move(self, touch):
        print("Mouse move", touch)
        self.rect.pos = touch.pos


class MyApp(App):
    def build(self):
        return Touch()


if __name__ == "__main__":
    MyApp().run()
