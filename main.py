import kivy
import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen

class MainWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass

class FirsWindow(Screen):
    secret_word: ObjectProperty(None)
    results: ObjectProperty(None)
    guess: ObjectProperty(None)

    def on_enter(self, *args):
        # Open file with all names, and take random name for the guessing
        file_with_characters = open("SWOGH_Characters.txt", "r").read().splitlines()
        secret_word = random.choice(file_with_characters)
        # self.secret_word.text = secret_word
        self.SGC = secret_word
        self.word = secret_word.lower()
        # Making secret word by replacing letters fo *
        self.secret_name = "*" * len(self.word)
        print(self.secret_name)
        # Making loop for game till win or lose
        self.secret_word.text = self.secret_name
        self.tries = int(len(self.word)/2)
        self.results.text =("you have " + str(self.tries) + " tries")

    def qbtn(self):
        guess = self.guess.text
        # Find the guess in the word
        print(guess)
        i = 0
        if guess in self.word:
            while self.word.find(guess, i) != -1:
                i = self.word.find(guess, i)
                self.secret_name = self.secret_name[:i] + guess + self.secret_name[i + 1:]
                self.secret_word.text = self.secret_name
                i += 1
                print(self.secret_name)
        else:
            self.results.text = ("Ups, no this character, you still have " + str(self.tries) + " tries left")
            self.tries -= 1

        if self.word == self.secret_name:
            self.results.text = ("You Win")
            self.secret_word.text = self.SGC
        if self.tries == -1:
            self.results.text = ("You Lost")
            self.secret_word.text = self.SGC
        self.guess.text = ""


class SWCApp(App):
    def build(self):
        return WindowManager()

if __name__ == '__main__':
    SWCApp().run()
