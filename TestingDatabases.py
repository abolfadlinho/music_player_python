from kivy.lang import Builder
from kivymd.app import MDApp
import sqlite3

kvdb = """
MDFloatLayout:
    BoxLayout:
        orientation: "vertical"
        size: root.width , root.height
        Label:
            id: input_label
            text_size: self.size
            halign: "center"
            valign: "middle"
            text: "Enter audio file name, artist and playlist"
            font_size: 25
        TextInput:
            id: input_filename
            multiline: False
            size_hint: (1, 0.2)
        TextInput:
            id: input_artist
            multiline: False
            size_hint: (1, 0.2)
        TextInput:
            id: input_playlist
            multiline: False
            size_hint: (1, 0.2)
        Button:
            size_hint: (1, 0.3)
            font_size: 32
            text: "Submit"
            on_press: app.submit()
        Button:
            size_hint: (1, 0.3)
            font_size: 32
            text: "Show Database"
            on_press: app.show()
"""


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "BlueGray"

        #Create or connect database
        connect =  sqlite3.connect("database.db")
        #Create a cursosr
        cursor = connect.cursor()
        #Create Main Table
        cursor.execute("""CREATE TABLE if not exists AllData(
            song_name TEXT PRIMARY KEY,
            artist TEXT NOT NULL,
            playlist TEXT DEFAULT singles
            )
        """)
        #Commit/save changes
        connect.commit()
        #Close connection
        connect.close()



        return Builder.load_string(kvdb)

    def submit(self):
        # Create or connect database
        connect = sqlite3.connect("database.db")
        # Create a cursosr
        cursor = connect.cursor()
        #Add a record
        cursor.execute("INSERT INTO AllData VALUES (:song_name) , (:artist), (:playlist)",
                       {
                           'first': self.root.ids.input_filename.text,
                           'second': self.root.ids.input_artist.text,
                           'third': self.root.ids.input_playlist.text

                       }
        )
        #Add message
        self.root.ids.input_label.text = f'{self.root.ids.input_filename.text} Added'
        #Clear Input Box
        self.root.ids.input_filename.text = ''
        # Commit/save changes
        connect.commit()
        # Close connection
        connect.close()

    def show(self):
        # Create or connect database
        connect = sqlite3.connect("database.db")
        # Create a cursosr
        cursor = connect.cursor()
        # Grab records from database
        cursor.execute("SELECT  * FROM AllData")
        records = cursor.fetchall()
        word = ""
        #Loop through records
        for record in records:
            word = f'{word}\n{record[0]}'
            self.root.ids.input_label.text = f'{word}'
        # Commit/save changes
        connect.commit()
        # Close connection
        connect.close()

MainApp().run()