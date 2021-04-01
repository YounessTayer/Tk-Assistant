"""Key bind reporter.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com
"""
from tkinter import messagebox, Tk

root = Tk()
root.title('Press any key')


def key_press(event):
    """When key event is detedted, report which key pressed."""
    print('key detected\n', event)
    messagebox.showinfo('key detected\n', event)


root.bind("<Key>", key_press)

root.mainloop()
