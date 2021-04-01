"""Checkbutton demo.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com
"""
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('Check Button demo')


# Callback.
def var_states():
    """Test and report which buttons user has ticked."""
    if VAR1.get() and VAR2.get():
        msg_box_txt = 'Both buttons were checked'

    if VAR1.get() and not VAR2.get():
        msg_box_txt = 'Python V2 was checked'

    if VAR2.get() and not VAR1.get():
        msg_box_txt = 'Python V3 was checked'

    if not VAR1.get() and not VAR2.get():
        msg_box_txt = 'Nothing was checked'

    messagebox.showinfo('Checkbutton result:',
                        msg_box_txt)


# Frame.
chkbtn_frame = tk.LabelFrame(root,
                             fg='green',
                             text='What Python do you use?')
chkbtn_frame.grid(padx=40, pady=20)

# Checkbuttons.
VAR1 = tk.IntVar()
pyv2_cb = tk.Checkbutton(chkbtn_frame,
                       text='Python V2',
                       variable=VAR1)
pyv2_cb.grid(row=0, sticky=tk.W, pady=10)

VAR2 = tk.IntVar()
pyv3_cb = tk.Checkbutton(chkbtn_frame,
                         text='Python V3',
                         variable=VAR2)
pyv3_cb.grid(row=1, sticky=tk.W)

# Button.
show_btn = tk.Button(chkbtn_frame,
                     text='Show Result',
                     bg='khaki',
                     command=var_states)
show_btn.grid (row=3, column=1)


root.mainloop()
