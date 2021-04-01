"""Change Window icon.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com
"""
from tkinter import Tk

root = Tk()
root.title('Changed icon')
root.config(bg='steelblue')

# Ensure the .ico file is in same dir
# as this source code is run from.

# Rename disk.ico to your own icon file.
root.iconbitmap('disk.ico')


root.mainloop()
