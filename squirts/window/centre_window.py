"""Centre window.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com
"""
from tkinter import Tk
from tkinter.ttk import Label

root = Tk()
root.title('Centre window on screen')
root.eval('tk::PlaceWindow . Center')  # This is the line

msg_lbl = Label(root,
                text='This window should be in the '
                'centre of your screen.')
msg_lbl.grid()

root.mainloop()
