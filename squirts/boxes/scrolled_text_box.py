"""Scrolled text box.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com
   """
import tkinter as tk
from tkinter import scrolledtext

root = tk.Tk()
root.title('Tk Assistant Scolled Text Box example')
root.resizable(False, False)


# Callback.
def clear_txt():
    """Clear text from scr txt box window."""
    scr_txt_bx.delete(1.0, tk.END)


# Frame.
stb_frame = tk.LabelFrame(root, fg='blue', text='Scrolled text box')
stb_frame.grid(padx=10, pady=10)

# Scrolled text box widget.
scr_txt_bx = scrolledtext.ScrolledText(stb_frame,
                                       bg='khaki',
                                       width=40,
                                       height=10)
scr_txt_bx.grid(row=3, column=0)

scr_txt_bx.insert(tk.INSERT, 'This is a scrolled textbox.\n\nTry typing.')

# Clear button.
clr_btn = tk.Button(stb_frame, bg='limegreen',
                    text='Clear the text',
                    command=clear_txt)
clr_btn.grid(row=0, column=0, sticky=tk.S, pady=8)


root.mainloop()
