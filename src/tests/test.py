import random
import numpy 
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.event import EventDispatcher
from kivy.properties import StringProperty, NumericProperty

class GeneratingButton(Button):
    def generate(self):
        self.x = random.randint(0,100)
        self.y = random.randint(0,100)
        return int(self.x), int(self.y)
    def build(self):
        self.text = "Generate"
@staticmethod
def generate(*args) -> int:
    x = random.randint(0,100)
    y = random.randint(0,100)
    return x,y 


class SubmitButton(Button):
    @staticmethod
    def check_answer(num1: int, num2: int, submitted: int)-> bool:
        answer = num1+num2
        if submitted != answer:
            return False
        else:
            return True

class Question(Label):
    pass

class Answer(TextInput):
    pass


class TestLayout(BoxLayout):
    num1, num2 = generate()
    def build(self) -> BoxLayout:
        return self
    def update_label(self, *args):
        question = self.ids.question_label
        question.text=  f"{self.num1} + {self.num2}="
        
    number1 = NumericProperty(num1)
    number2 = NumericProperty(num2)
    def check_answer(self, num1: int, num2: int)-> bool:
        answer = int(self.ids.answer_text.text)
        sum = num1+num2
        if answer != sum:
            print("False") 
            print(num1, num2)
            return False
        else:
            print("True") 
            print(num1, num2)
            return True


def Testing():
    TestObject_Generation = GeneratingButton()
    Genned_First, Genned_Second = TestObject_Generation.generate()
    TestObject_Checking = SubmitButton()
    TestObject_Answer = int(input(f"{Genned_First}+{Genned_Second}="))
    if TestObject_Checking.check_answer(Genned_First, Genned_Second, TestObject_Answer):
        print('Correct!')
    else:
        print('Incorrect!')


class test(App):
    def build(self):
        return TestLayout()



if __name__ == "__main__":
    answer = int(input("What do u want to do? 1. Test Func 2. Test Graphics"))
    if answer == 1:
        Testing()
    else:
        test().run()
