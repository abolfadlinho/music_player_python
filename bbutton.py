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
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.properties import StringProperty

#Window.fullscreen = True
Window.size = 400,600


kv = """
WindowManager:
    HomeWindow:
    AlbumsWindow:
    ArtistsWindow:
    PlaylistsWindow:
    AllDataWindow:
<HomeWindow>:
    name:'home'
    MDBoxLayout:
        adaptive_height: False
        md_bg_color: 1, 0.49, 0.36, 1
        orientation: 'vertical'
        size: root.width, root.height
        MDToolbar:
            md_bg_color: 0, 0.502, 0.65, 1
            title: "Title"
            anchor_title: 'center'
        MDBottomAppBar:
            md_bg_color: 0, 0.502, 0.65, 1
            MDToolbar:
                type_height: 'small'
                icon: 'play'
                icon_color: 0, 0.502, 0.65, 1
                type: 'bottom'
                mode: 'center'
                right_action_items: [['skip-next', lambda x: app.playnext() ]]
                left_action_items: [["skip-previous", lambda x: app.playprevious()]]
                on_action_button: app.playaudio()
        MDRaisedButton:
            text: "Albums"
            font_size: 20
            md_bg_color: 1, 1, 0.35, 1
            line_color: 0,0,0,1
            text_color: 0,0,0.1,1
            size_hint: 1, 0.2
            pos_hint: {'x':0, 'y':0}            
            on_release:
                app.root.current = "albums"
                root.manager.transition.direction = "left"
        MDRaisedButton:
            text: "Artists"
            font_size: 20
            text_color: 0,0,0.1,1
            md_bg_color: 1, 1, 0.35, 1
            line_color: 0,0,0,1
            size_hint: 1, 0.2
            on_release:
                app.root.current = "artists"
                root.manager.transition.direction = "left"
        MDRaisedButton:
            text: "Playlists"
            font_size: 20
            text_color: 0,0,0.1,1
            md_bg_color: 1, 1, 0.35, 1
            line_color: 0,0,0,1
            size_hint: 1, 0.2
            on_release:
                app.root.current = "playlists"
                root.manager.transition.direction = "left"
        MDRaisedButton:
            text: "All Data"
            font_size: 20
            text_color: 0,0,0.1,1
            line_color: 0,0,0,1
            md_bg_color: 1, 1, 0.35, 1
            size_hint: 1, 0.2
            on_release:
                app.root.current = "alldata"
                root.manager.transition.direction = "left"
        MDLabel:
            text: 'Ali Hany'
        MDRaisedButton:
            text: "Randomize"
            font_size: 16
            pos_hint: {"x": 0.4, "y": 0.15}
            size_hint: 0.1, 0.1
            md_bg_color: 1, 1, 0.35, 1
            text_color: 0,0,0.1,1
            line_color: 0,0,0,1          
<AlbumsWindow>:
    name:"albums"
    MDBoxLayout:
        md_bg_color: 1, 0.49, 0.36, 1
        orientation: 'vertical'
        size: root.width, root.height
        MDToolbar:
            md_bg_color: 0, 0.502, 0.65, 1
            title: "Albums"
            font_size: 32
            anchor_title: 'left'
            MDIconButton:
                icon : 'home'
                size_hint: 0.15, 1
                md_bg_color: 0, 0.502, 0.65, 1
                on_release:
                    app.root.current = "home"
                    root.manager.transition.direction = "right"
        MDBottomAppBar:
            md_bg_color: 0, 0.502, 0.65, 1
            MDToolbar:
                type_height: 'small'
                icon: 'play'
                icon_color: 0, 0.502, 0.65, 1
                type: 'bottom'
                mode: 'center'
                right_action_items: [['skip-next', lambda x: app.playnext() ]]
                left_action_items: [["skip-previous", lambda x: app.playprevious()]]
                on_action_button: app.playaudio()
        MDLabel:
            text: "Album list will be placed here"
        MDRaisedButton:
            text: "Randomize"
            font_size: 16
            pos_hint: {"x": 0.4, "y": 0.15}
            size_hint: 0.1, 0.05
            md_bg_color: 1, 1, 0.35, 1
            text_color: 0,0,0.1,1
            line_color: 0,0,0,1  
<ArtistsWindow>:
    name:"artists"
    MDBoxLayout:
        md_bg_color: 1, 0.49, 0.36, 1
        orientation: 'vertical'
        size: root.width, root.height
        MDToolbar:
            md_bg_color: 0, 0.502, 0.65, 1
            title: "   Artists"
            font_size: 32
            anchor_title: 'left'
            MDIconButton:
                icon : 'home'
                size_hint: 0.15, 1
                md_bg_color: 0, 0.502, 0.65, 1
                on_release:
                    app.root.current = "home"
                    root.manager.transition.direction = "right"
        MDBottomAppBar:
            md_bg_color: 0, 0.502, 0.65, 1
            MDToolbar:
                type_height: 'small'
                icon: 'play'
                icon_color: 0, 0.502, 0.65, 1
                type: 'bottom'
                mode: 'center'
                right_action_items: [['skip-next', lambda x: app.playnext() ]]
                left_action_items: [["skip-previous", lambda x: app.playprevious()]]
                on_action_button: app.playaudio()
        MDLabel:
            text: "Artists list will be placed here"
        MDRaisedButton:
            text: "Randomize"
            font_size: 16
            pos_hint: {"x": 0.4, "y": 0.15}
            size_hint: 0.1, 0.05
            md_bg_color: 1, 1, 0.35, 1
            text_color: 0,0,0.1,1
            line_color: 0,0,0,1
<PlaylistsWindow>:
    name:"playlists"
    MDBoxLayout:
        md_bg_color: 1, 0.49, 0.36, 1
        orientation: 'vertical'
        size: root.width, root.height
        MDToolbar:
            md_bg_color: 0, 0.502, 0.65, 1
            title: "   Playlists"
            font_size: 32
            anchor_title: 'left'
            MDIconButton:
                icon : 'home'
                size_hint: 0.15, 1
                md_bg_color: 0, 0.502, 0.65, 1
                on_release:
                    app.root.current = "home"
                    root.manager.transition.direction = "right"
        MDBottomAppBar:
            md_bg_color: 0, 0.502, 0.65, 1
            MDToolbar:
                type_height: 'small'
                icon: 'play'
                icon_color: 0, 0.502, 0.65, 1
                type: 'bottom'
                mode: 'center'
                right_action_items: [['skip-next', lambda x: app.playnext() ]]
                left_action_items: [["skip-previous", lambda x: app.playprevious()]]
                on_action_button: app.playaudio()
        MDLabel:
            text: "Playlists list will be placed here"
        MDRaisedButton:
            text: "Randomize"
            font_size: 16
            pos_hint: {"x": 0.4, "y": 0.15}
            size_hint: 0.1, 0.05
            md_bg_color: 1, 1, 0.35, 1
            text_color: 0,0,0.1,1
            line_color: 0,0,0,1
<AllDataWindow>:
    name:"alldata"
    MDBoxLayout:
        md_bg_color: 1, 0.49, 0.36, 1
        orientation: 'vertical'
        size: root.width, root.height
        MDToolbar:
            md_bg_color: 0, 0.502, 0.65, 1
            title: "   All Data"
            font_size: 40
            anchor_title: 'left'
            MDIconButton:
                icon : 'home'
                size_hint: 0.15, 1
                md_bg_color: 0, 0.502, 0.65, 1
                on_release:
                    app.root.current = "home"
                    root.manager.transition.direction = "right"
        MDBottomAppBar:
            md_bg_color: 0, 0.502, 0.65, 1
            MDToolbar:
                type_height: 'small'
                icon: 'play'
                icon_color: 0, 0.502, 0.65, 1
                type: 'bottom'
                mode: 'center'
                right_action_items: [['skip-next', lambda x: app.playnext() ]]
                left_action_items: [["skip-previous", lambda x: app.playprevious()]]
                on_action_button: app.playaudio()       
        MDIconButton:
            icon : 'youtube'
            pos_hint: {"x": 0.87, "y": 0.7}
            size_hint: 0.1, 0.05
            md_bg_color: 1, 1, 0.35, 1
            text_color: 0,0,0.1,1
            line_color: 0,0,0,1
        MDIconButton:
            icon : 'plus'
            pos_hint: {"x": 0.87, "y": 1.2}
            size_hint: 0.1, 0.05
            md_bg_color: 1, 1, 0.35, 1
            text_color: 0,0,0.1,1
            line_color: 0,0,0,1
        MDLabel:
            text: "All data will be placed here"
        MDLabel:
            text: ""
        MDRaisedButton:
            text: "Randomize"
            font_size: 16
            pos_hint: {"x": 0.4, "y": 0.15}
            size_hint: 0.1, 0.1
            md_bg_color: 1, 1, 0.35, 1
            text_color: 0,0,0.1,1
            line_color: 0,0,0,1
"""


class HomeWindow(Screen):
    pass


class AlbumsWindow(Screen):
    pass


class ArtistsWindow(Screen):
    pass


class PlaylistsWindow(Screen):
    pass


class AllDataWindow(Screen):
    pass


class WindowManager(ScreenManager):
    pass


class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.playing = False
        self.music_dir = 'C:/Users/Ahmed/PycharmProjects/pythonProject/Music Player/Music File'
        music_files = os.listdir(self.music_dir)

        self.song_list = [x for x in music_files if x.endswith('mp3')]

        self.song_count = len(self.song_list)
        self.song_title = StringProperty()
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

    def playprevious(self):
        print('previous')

    def playnext(self):
        print("next")

    def addfiles(self):
        self.filepath = filedialog.askopenfilename(initialdir='/', title='Select ZIP File',
                                              filetypes=(('executables', '*.zip'), ('all files', '*.*')))
        with zipfile.ZipFile(self.filepath, 'r') as zip_ref:
            zip_ref.extractall('Music File')
        print("Done")


MyApp().run()