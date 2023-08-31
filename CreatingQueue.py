from queue import Queue
import random
import sqlite3

#PlayingMusic = Queue()

#Create or connect database
connect =  sqlite3.connect("store_music.db")
#Create a cursosr
cursor = connect.cursor()
#Create Main Table
command1 = """CREATE TABLE IF NOT EXISTS
music(song_name TEXT PRIMARY KEY, artist TEXT, album TEXT)
"""
#command2 = "FROM music GROUP BY artist"
cursor.execute(command1)
#cursor.execute(command2)
#Commit/save changes
connect.commit()
#Close connection
connect.close()

def AddRecord():
    connect = sqlite3.connect("store_music.db")
    # Create a cursosr
    cursor = connect.cursor()
    # Add to database
    cursor.execute("INSERT INTO music VALUES ('Hustla', 'Wegz', 'Singles')")
    cursor.execute("INSERT INTO music VALUES ('CTRL', 'Pablo', 'Ghaba')")
    cursor.execute("INSERT INTO music VALUES ('KAAS', 'Pablo', 'Singles')")
    # Commit/save changes
    connect.commit()
    # Close connection
    connect.close()


def ShowRecords():
    connect = sqlite3.connect("store_music.db")
    # Create a cursosr
    cursor = connect.cursor()
    # Get Results
    cursor.execute("SELECT * FROM music")
    results = cursor.fetchall()
    print(results)
    # Commit/save changes
    connect.commit()
    # Close connection
    connect.close()


def UpdateRecord():
    cursor.execute("UPDATE music SET album = 'CTRL' WHERE song_name = 'CTRL'")


def DeleteRecord():
    cursor.execute("DELETE FROM music WHERE song_name = 'Hustla'")


AddRecord()
ShowRecords()
