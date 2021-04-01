"""Combobox demo.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com
   """
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Combobox

root = tk.Tk()
root.title('Combobox demo')


# Callback
def clkd_btn():
    """Display selection."""
    sel_item = combo_bx.get()

    if sel_item == 'Select an item':
        return

    if sel_item == 'Quit combobox demo':
        root.withdraw()
        root.destroy()
        return

    tk.messagebox.showinfo('User choice',
                           'You Selected:\n\n'+str(sel_item))


# Frame.
combo_frame = tk.LabelFrame(root)
combo_frame.grid(padx=20, pady=8)

# Combobox.
combo_bx = Combobox(combo_frame)
combo_bx['values'] = ('Select an item',
                      'Art',
                      'Cats',
                      'Celeb',
                      'Dogs',
                      'Quit combobox demo')

combo_bx.current(0)
combo_bx.grid(padx=5, pady=5)

# Button.
clk_btn = tk.Button(combo_frame,
                    bg='gold',
                    text='Click Me',
                    command=clkd_btn)
clk_btn.grid(sticky=tk.W+tk.E, padx=5, pady=5)


root.mainloop()
