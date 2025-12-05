from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import random
import time
class RootWidget(BoxLayout):
    def do(self):
        a = 0
        total = 5
        user = self.ids.name
        while a <= 10:
            randnum = random.randrange(total)
            user.text = str(randnum)

            a+=1
class test3App(App):
    def build(self):
        return RootWidget()

if __name__ == "__main__":
    no=test3App()
    no.run()
