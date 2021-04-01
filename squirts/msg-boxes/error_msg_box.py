"""Error message box.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com
"""
from tkinter import messagebox, Tk

root = Tk()
root.withdraw()

messagebox.showerror('Error',
                     'This is an error message box.')


root.mainloop()
