"""Entry box demo.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com
   """
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('Entry box demo')


# Callback.
def ebox_display():
    """Display contents of entry box."""
    txt = ent_bx.get()
    tk.messagebox.showinfo('Information',
                           'Entry box contains the text:\n\n' + '"' +
                           str(txt) + '"')


# Frame.
entbox_frame = tk.LabelFrame(root)
entbox_frame.grid(padx=40, pady=8)

# Entrybox.
ent_bx = tk.Entry(entbox_frame,
                  bd=3,
                  bg='gold')
ent_bx.grid(sticky=tk.W+tk.E, padx=5, pady=5)
ent_bx.insert(0, 'Type text, press return')
ent_bx.focus()

# Bind key.
root.bind("<Return>", lambda x: ebox_display())


root.mainloop()
