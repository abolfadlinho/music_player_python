import kivymd
import kivy
import zipfile
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
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.config import Config
from kivy.properties import StringProperty

#Window.fullscreen = True
Window.size = 400, 600
Config.window_icon = "icon.ico"


kv = """
WindowManager:
    HomeWindow:
    AlbumsWindow:
    ArtistsWindow:
    PlaylistsWindow:
    AllDataWindow:
    FileChooserWindow:
<HomeWindow>:
    name:'home'
    MDFloatLayout:
        md_bg_color: 1, 0.49, 0.36, 1
        size: root.width, root.height
        MDLabel:
            text: "Title"
            font_size: 25
            halign: 'center'
            pos_hint: {"y": 0.45}
        MDFillRoundFlatIconButton:
            text: "Albums"
            icon: "album"
            font_size: 23
            md_bg_color: 1, 1, 0.35, 1
            pos_hint: {"y": 0.75}
            line_color: 0,0,0,1
            text_color: 0,0,0.1,1
            size_hint: 1, 0.08
            icon_color: 0,0,0.1,1
            on_release:
                app.root.current = "albums"
                root.manager.transition.direction = "left"
        MDFillRoundFlatIconButton:
            text: "Artists"
            icon: "account"
            font_size: 23
            md_bg_color: 1, 1, 0.35, 1
            pos_hint: {"y": 0.65}
            line_color: 0,0,0,1
            text_color: 0,0,0.1,1
            size_hint: 1, 0.08
            icon_color: 0,0,0.1,1
            on_release:
                app.root.current = "artists"
                root.manager.transition.direction = "left"
        MDFillRoundFlatIconButton:
            text: "Playlists"
            icon: "menu"
            font_size: 23
            md_bg_color: 1, 1, 0.35, 1
            pos_hint: {"y": 0.55}
            line_color: 0,0,0,1
            text_color: 0,0,0.1,1
            size_hint: 1, 0.08
            icon_color: 0,0,0.1,1
            on_release:
                app.root.current = "playlists"
                root.manager.transition.direction = "left"
        MDFillRoundFlatIconButton:
            text: "All Data"
            icon: "music"
            font_size: 23
            md_bg_color: 1, 1, 0.35, 1
            pos_hint: {"y": 0.45}
            line_color: 0,0,0,1
            text_color: 0,0,0.1,1
            size_hint: 1, 0.08
            icon_color: 0,0,0.1,1
            on_release:
                app.root.current = "alldata"
                root.manager.transition.direction = "left"
        MDLabel:
            id: currently_playing_song
            text: "Currently not Playing"
            halign: "center"
            pos_hint: {"y": -0.4}
            font_size: 14
        MDIconButton:
            icon : 'play'
            pos_hint: {"x": 0.45, "y": 0}
            size_hint: 0.1, 0.1
            md_bg_color: 0, 0.502, 0.65, 1
            line_color: 0,0,0,1
            on_release: app.playaudio()
        MDIconButton:
            icon : 'stop'
            pos_hint: {"x": 0.6, "y": 0}
            size_hint: 0.1, 0.05
            md_bg_color: 0, 0.502, 0.65, 1
            line_color: 0,0,0,1
            on_release: app.stopaudio()
        MDIconButton:
            icon : 'shuffle'
            pos_hint: {"x": 0.3, "y": 0}
            size_hint: 0.1, 0.05
            md_bg_color: 0, 0.502, 0.65, 1
            line_color: 0,0,0,1
            on_release: app.shuffleplay()
        MDIconButton:
            icon : 'skip-previous'
            pos_hint: {"x": 0.15, "y": 0}
            size_hint: 0.1, 0.05
            md_bg_color: 0, 0.502, 0.65, 1
            line_color: 0,0,0,1
        MDIconButton:
            icon : 'skip-next'
            pos_hint: {"x": 0.75, "y": 0}
            size_hint: 0.1, 0.05
            md_bg_color: 0, 0.502, 0.65, 1
            line_color: 0,0,0,1       
<AlbumsWindow>:
    name:"albums"
    ScrollView:
        do_scroll_x: False
        do_scroll_y: True
    MDFloatLayout:
        md_bg_color: 1, 0.49, 0.36, 1
        size: root.width, root.height
        MDLabel:
            text: "Albums"
            font_size: 20
            halign: 'center'
            pos_hint: {"y": 0.45}
        MDIconButton:
            icon : 'home'
            pos_hint: {"x": 0, "y": 0.91}
            size_hint: 0.1, 0.05
            on_release:
                app.root.current = "home"
                root.manager.transition.direction = "right"
        MDLabel:
            id: albums_currently_playing_song
            text: "Currently not Playing"
            halign: "center"
            pos_hint: {"y": -0.4}
            font_size: 14
        MDIconButton:
            icon : 'play'
            pos_hint: {"x": 0.45, "y": 0}
            size_hint: 0.1, 0.1
            md_bg_color: 0, 0.502, 0.65, 1
            line_color: 0,0,0,1
            on_release: app.playaudio()
        MDIconButton:
            icon : 'stop'
            pos_hint: {"x": 0.6, "y": 0}
            size_hint: 0.1, 0.05
            md_bg_color: 0, 0.502, 0.65, 1
            line_color: 0,0,0,1
            on_release: app.stopaudio()
        MDIconButton:
            icon : 'shuffle'
            pos_hint: {"x": 0.3, "y": 0}
            size_hint: 0.1, 0.05
            md_bg_color: 0, 0.502, 0.65, 1
            line_color: 0,0,0,1
            on_release: app.shuffleplay()
        MDIconButton:
            icon : 'skip-previous'
            pos_hint: {"x": 0.15, "y": 0}
            size_hint: 0.1, 0.05
            md_bg_color: 0, 0.502, 0.65, 1
            line_color: 0,0,0,1
        MDIconButton:
            icon : 'skip-next'
            pos_hint: {"x": 0.75, "y": 0}
            size_hint: 0.1, 0.05
            md_bg_color: 0, 0.502, 0.65, 1
            line_color: 0,0,0,1  
<ArtistsWindow>:
    name:"artists"
    ScrollView:
        do_scroll_x: False
        do_scroll_y: True
    MDFloatLayout:
        md_bg_color: 1, 0.49, 0.36, 1
        size: root.width, root.height

        MDLabel:
            text: "Artists"
            font_size: 20
            halign: 'center'
            pos_hint: {"y": 0.45}
        MDIconButton:
            icon : 'home'
            pos_hint: {"x": 0, "y": 0.91}
            size_hint: 0.1, 0.05
            on_release:
                app.root.current = "home"
                root.manager.transition.direction = "right"
        MDLabel:
            id: artists_currently_playing_song
            text: "Currently not Playing"
            halign: "center"
            pos_hint: {"y": -0.4}
            font_size: 14
        MDIconButton:
            icon : 'play'
            pos_hint: {"x": 0.45, "y": 0}
            size_hint: 0.1, 0.1
            md_bg_color: 0, 0.502, 0.65, 1
            line_color: 0,0,0,1
            on_release: app.playaudio()
        MDIconButton:
            icon : 'stop'
            pos_hint: {"x": 0.6, "y": 0}
            size_hint: 0.1, 0.05
            md_bg_color: 0, 0.502, 0.65, 1
            line_color: 0,0,0,1
            on_release: app.stopaudio()
        MDIconButton:
            icon : 'shuffle'
            pos_hint: {"x": 0.3, "y": 0}
            size_hint: 0.1, 0.05
            md_bg_color: 0, 0.502, 0.65, 1
            line_color: 0,0,0,1
            on_release: app.shuffleplay()
        MDIconButton:
            icon : 'skip-previous'
            pos_hint: {"x": 0.15, "y": 0}
            size_hint: 0.1, 0.05
            md_bg_color: 0, 0.502, 0.65, 1
            line_color: 0,0,0,1
        MDIconButton:
            icon : 'skip-next'
            pos_hint: {"x": 0.75, "y": 0}
            size_hint: 0.1, 0.05
            md_bg_color: 0, 0.502, 0.65, 1
            line_color: 0,0,0,1
<PlaylistsWindow>:
    name:"playlists"
    ScrollView:
        do_scroll_x: False
        do_scroll_y: True
    MDFloatLayout:
        md_bg_color: 1, 0.49, 0.36, 1
        size: root.width, root.height
        MDLabel:
            text: "Playlists"
            font_size: 20
            halign: 'center'
            pos_hint: {"y": 0.45}
        MDIconButton:
            icon : 'home'
            pos_hint: {"x": 0, "y": 0.91}
            size_hint: 0.1, 0.05
            on_release:
                app.root.current = "home"
                root.manager.transition.direction = "right"
        MDIconButton:
            icon : 'plus'
            pos_hint: {"x": 0.87, "y": 0.91}
            size_hint: 0.1, 0.05
            md_bg_color: 1, 1, 0.35, 1
            line_color: 0,0,0,1
        MDLabel:
            id: playlists_currently_playing_song
            text: "Currently not Playing"
            halign: "center"
            pos_hint: {"y": -0.4}
            font_size: 14
        MDIconButton:
            icon : 'play'
            pos_hint: {"x": 0.45, "y": 0}
            size_hint: 0.1, 0.1
            md_bg_color: 0, 0.502, 0.65, 1
            line_color: 0,0,0,1
            on_release: app.playaudio()
        MDIconButton:
            icon : 'stop'
            pos_hint: {"x": 0.6, "y": 0}
            size_hint: 0.1, 0.05
            md_bg_color: 0, 0.502, 0.65, 1
            line_color: 0,0,0,1
            on_release: app.stopaudio()
        MDIconButton:
            icon : 'shuffle'
            pos_hint: {"x": 0.3, "y": 0}
            size_hint: 0.1, 0.05
            md_bg_color: 0, 0.502, 0.65, 1
            line_color: 0,0,0,1
            on_release: app.shuffleplay()
        MDIconButton:
            icon : 'skip-previous'
            pos_hint: {"x": 0.15, "y": 0}
            size_hint: 0.1, 0.05
            md_bg_color: 0, 0.502, 0.65, 1
            line_color: 0,0,0,1
        MDIconButton:
            icon : 'skip-next'
            pos_hint: {"x": 0.75, "y": 0}
            size_hint: 0.1, 0.05
            md_bg_color: 0, 0.502, 0.65, 1
            line_color: 0,0,0,1
<AllDataWindow>:
    name:"alldata"
    ScrollView:
        do_scroll_x: False
        do_scroll_y: True
    MDFloatLayout:
        md_bg_color: 1, 0.49, 0.36, 1
        size: root.width, root.height
        MDIconButton:
            icon : 'plus'
            pos_hint: {"x": 0.87, "y": 0.91}
            size_hint: 0.1, 0.05
            md_bg_color: 1, 1, 0.35, 1
            line_color: 0,0,0,1
            on_release:
                app.root.current = "filechooserwindow"
                root.manager.transition.direction = "left"
        MDLabel:
            text: "All Data"
            font_size: 20
            halign: 'center'
            pos_hint: {"y": 0.45}
        MDIconButton:
            icon : 'home'
            pos_hint: {"x": 0, "y": 0.91}
            size_hint: 0.1, 0.05
            on_release:
                app.root.current = "home"
                root.manager.transition.direction = "right"
        MDLabel:
            id: alldata_currently_playing_song
            text: "Currently not Playing"
            halign: "center"
            pos_hint: {"y": -0.4}
            font_size: 14
        MDIconButton:
            icon : 'play'
            pos_hint: {"x": 0.45, "y": 0}
            size_hint: 0.1, 0.1
            md_bg_color: 0, 0.502, 0.65, 1
            line_color: 0,0,0,1
            on_release: app.playaudio()
        MDIconButton:
            icon : 'stop'
            pos_hint: {"x": 0.6, "y": 0}
            size_hint: 0.1, 0.05
            md_bg_color: 0, 0.502, 0.65, 1
            line_color: 0,0,0,1
            on_release: app.stopaudio()
        MDIconButton:
            icon : 'shuffle'
            pos_hint: {"x": 0.3, "y": 0}
            size_hint: 0.1, 0.05
            md_bg_color: 0, 0.502, 0.65, 1
            line_color: 0,0,0,1
            on_release: app.shuffleplay()
        MDIconButton:
            icon : 'skip-previous'
            pos_hint: {"x": 0.15, "y": 0}
            size_hint: 0.1, 0.05
            md_bg_color: 0, 0.502, 0.65, 1
            line_color: 0,0,0,1
        MDIconButton:
            icon : 'skip-next'
            pos_hint: {"x": 0.75, "y": 0}
            size_hint: 0.1, 0.05
            md_bg_color: 0, 0.502, 0.65, 1
            line_color: 0,0,0,1
<FileChooserWindow>:
    id: my_widget
    name: "filechooserwindow"
    ScrollView:
        do_scroll_x: False
        do_scroll_y: True
    MDBoxLayout:
        md_bg_color: 0, 0.502, 0.65, 1
        FileChooserListView:
            id: filechooser
            on_selection: my_widget.selected(filechooser.selection)
            MDRaisedButton:
                text: "Close"
                font_size: 18
                text_color: 1,1,1,1
                md_bg_color: 1, 0, 0, 1
                on_release:
                    app.root.current = "alldata"
                    root.manager.transition.direction = "right"
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


class FileChooserWindow(Screen):
    def selected(self, filename):
        try:
            self.ids.my_file.source = filename[0]
            print(filename[0])
        except:
            pass


class MusicPlayerApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "BlueGray"
        self.icon = 'icon.ico'
        self.theme_cls.primary_color
        self.theme_cls.theme_style = "Light"
        self.playing = False
        self.music_dir = 'C:/Users/Ahmed/PycharmProjects/pythonProject/Music Player/Music List'
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
        #self.root.ids.currently_playing_song.text = self.song_title

    def shuffleplay(self):
        self.song_title = self.song_list[random.randrange(0, self.song_count)]
        if not self.playing:
            self.sound = SoundLoader.load('{}/{}'.format(self.music_dir, self.song_title))
            self.playing = True
            self.sound.play()
        else:
            self.playing = False
            self.sound.stop()

    def stopaudio(self):
        self.playing = False
        self.sound.stop()

    def playprevious(self):
        print('previous')

    def playnext(self):
        print("next")

    def addfiles(self):
        with zipfile.ZipFile(self.filepath, 'r') as zip_ref:
            zip_ref.extractall('Music File')
        print("Done")


if __name__ == "__main__":
   MusicPlayerApp().run()