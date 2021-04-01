"""Color picker dialog.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com
"""
import tkinter as tk
from tkinter.colorchooser import askcolor

root = tk.Tk()
root.withdraw()  # Hide horrid window.

# Hex value of color returned in tuple askcolor.
get_colour = askcolor()
print('Colour picked: ', get_colour[1])


root.mainloop()
