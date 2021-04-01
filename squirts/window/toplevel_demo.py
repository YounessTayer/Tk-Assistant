"""Toplevel Example
   Stand-alone example from Tk Assistant.
   Updated March 2021
   source:https://coderslegacy.com/python/list-of-tkinter-widgets/
   Edited by Steve Shambles.Ssee link its good.
   stevepython.wordpress.com
"""
import tkinter as tk
root = tk.Tk()


def new_window():
    """Create a toplevel window."""
    top_wndw = tk.Toplevel()
    top_wndw.title('Toplevel')

    new_label = tk.Label(top_wndw,
                         font=('verdant 40'),
                         bg='steelblue',
                         fg='gold',
                         text="A toplevel Window")
    new_label.grid()


my_btn = tk.Button(root,
                   font=('verdant 12'),
                   bg='khaki',
                   text='Click for Toplevel demo',
                   command=new_window)
my_btn.grid()


root.mainloop()
