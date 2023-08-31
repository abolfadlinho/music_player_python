import zipfile
from tkinter import filedialog


filepath =  filedialog.askopenfilename(initialdir='/', title='Select ZIP File',
                                         filetypes=(('executables', '*.zip'), ('all files', '*.*')))
with zipfile.ZipFile(filepath, 'r') as zip_ref:
    zip_ref.extractall('Music File')