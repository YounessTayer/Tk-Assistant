"""Simple Label.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com
"""
from tkinter import Label, Tk

root = Tk()
root.title('Simple label example')

txt_label = Label(root,
                  bg='plum',
                  font='helvetica 20',
                  text='helvetica 20 font on a simple label.')
txt_label.grid()


root.mainloop()
