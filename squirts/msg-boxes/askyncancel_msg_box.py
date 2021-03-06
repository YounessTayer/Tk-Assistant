"""askyncancel msg box.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com
"""
from tkinter import messagebox, Tk

root = Tk()
root.withdraw()  # Remove annoying window.

ask_ync = messagebox.askyesnocancel('Question',
                                    'Click on any button.')

if ask_ync:
    print('You clicked on Yes')

if ask_ync is False:
    print('You clicked on No')

if ask_ync is None:
    print('You clicked on Cancel')


root.mainloop()
