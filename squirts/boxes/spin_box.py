"""Spinbox demo.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com
"""
import tkinter as tk
from tkinter import messagebox, TclError

root = tk.Tk()
root.title('Spinbox example')
root.resizable(False, False)


# Callback.
def spbox_val():
    """Display spinbox current value."""
    # If input is invalid, eg.non-numeric or blank, then return.
    try:
        spnbx_val = VAR.get()
    except TclError:
        messagebox.showerror('Input Error',
                            'Numbers only please!')
        return

    messagebox.showinfo('Spinbox',
                        'Spinbox value is '+str(spnbx_val))


# Frame.
spbx_frame = tk.LabelFrame(root,
                           fg='blue',
                           text='Choose number and click button')
spbx_frame.grid(padx=20, pady=20, ipadx=5, ipady=3)

VAR = tk.IntVar()
VAR.set(50)

# Spinbox widget.
spn_bx = tk.Spinbox(spbx_frame,
                    from_=0, to=100,
                    width=4,
                    textvariable=VAR)
spn_bx.grid(column=0, row=0, padx=10, pady=10)

# Button.
spbx_btn = tk.Button(spbx_frame,
                     bg='green2',
                     text='Spinbox value',
                     command=spbox_val)
spbx_btn.grid(row=0, column=1)


root.mainloop()
