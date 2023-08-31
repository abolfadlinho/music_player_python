import os
from kivy.core.audio import SoundLoader
from kivy.lang import Builder
import kivymd
from kivymd.app import MDApp
from kivy.core.window import Window
import kivy
import kivymd
import kivy
import zipfile
from tkinter import filedialog
import os
import random
from kivymd.uix.relativelayout import MDRelativeLayout
from kivy.core.audio import SoundLoader
from kivy.uix.widget import Widget
from kivy.uix.slider import Slider
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.button import MDTextButton, MDIconButton, MDFillRoundFlatButton, MDRoundFlatButton, MDFillRoundFlatIconButton
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.properties import StringProperty

Window.size = 400,600


kv = '''
<HomeWindow>:
    MDBoxLayout:
        md_bg_color: 0, 1, 0.36, 1
        orientation: 'vertical'
        MDRaisedButton:
            text: "play"
            font_size: 20
            md_bg_color: 0, 1, 0.35, 1
            text_color: 0,0,0.1,1
            size_hint: 1, 0.2
            pos_hint: {'x':0, 'y':0}            
            on_release: app.playaudio()
        MDRaisedButton:
            text: "stop"
            font_size: 20
            md_bg_color: 1, 1, 0.35, 1
            text_color: 0,0,0.1,1
            size_hint: 1, 0.2
            pos_hint: {'x':0, 'y':0.5}            
            on_release: app.stopaudio()


'''



class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.playing = False
        self.music_dir = 'C:/Users/Ahmed/PycharmProjects/pythonProject/Music Player/Music File'
        music_files = os.listdir(self.music_dir)

        self.song_list = [x for x in music_files if x.endswith('mp3')]

        self.song_count = len(self.song_list)
        return Builder.load_string(kv)
    def playaudio(self):
        self.song_title = self.song_list[random.randrange(0, self.song_count)]
        if not self.playing:
            self.sound = SoundLoader.load('{}/{}'.format(self.music_dir, self.song_title))
            self.playing = True
            self.sound.play()
        else:
            self.playing = False
            self.sound.stop()

    def stopaudio(self):
        self.sound.stop()


MyApp().run()