from kivy.app import App
from kivy.core.text import LabelBase

LabelBase.register(name="Raleway",
    fn_regular="Raleway-Regular.ttf",
    fn_bold="Raleway-Bold.ttf",
    fn_italic="Raleway-Italic.ttf",
    fn_bolditalic="Raleway-BoldItalic.ttf")


class ClockApp(App):
    pass

if __name__ == '__main__':
    ClockApp().run()
