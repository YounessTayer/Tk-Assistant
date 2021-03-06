"""User input dialog.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com
"""
from tkinter import simpledialog, Tk

root = Tk()
root.withdraw()

user_input = simpledialog.askstring(title='Test input dialog',
                                    prompt='What is your name?:')

print('Hello', user_input)


root.mainloop()
