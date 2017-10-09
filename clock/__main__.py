from datetime import datetime

from kivy.app import App
from kivy.core.text import LabelBase
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.clock import Clock


LabelBase.register(name="Aller",
    fn_regular="Aller_Rg.ttf",
    fn_bold="Aller_Bd.ttf",
    fn_italic="Aller_It.ttf",
    fn_bolditalic="Aller_BdIt.ttf")


class ClockApp(App):
    def update_time(self, nap):
        self.root.ids.timeLabel.text = datetime.now().strftime('[b]%H[/b]:%M:%S')

    def on_start(self):
        Clock.schedule_interval(self.update_time, 1)

if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#101216')
    ClockApp().run()
