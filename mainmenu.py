#imports
import random
import sympy
import matplotlib as mpl
import appdirs
import tinydb
import subprocess
import sys
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.core.window import Window

class MainMenu(RelativeLayout):
    pass

class Title(Label):
    pass

class BeginSelection(Button):
    pass

class Quit(Button):
    pass

class MainMenuApp(App):
    def close_app(self):
        App.get_running_app().stop()
        Window.close()
        sys.exit()

MainMenuApp().run()
