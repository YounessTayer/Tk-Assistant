"""Listbox demo.
   Stand-alone example from Tk Assistant.
   Updated March 2021
   By Steve Shambles
   stevepython.wordpress.com
   """
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('Listbox demo by TK Assistant')
root.resizable(False, False)


# Callback.
def double_clicked(event):
    """Double clicked mouse on listbox item. Report which item."""
    ev_w = event.widget
    idx = int(ev_w.curselection()[0])
    value = ev_w.get(idx)
    messagebox.showinfo('Listbox demo',
                        'You double clicked on:\n\n' +
                        '"' + str(value) + '"')


# Frame.
lstbx_frame = tk.LabelFrame(root)
lstbx_frame.grid(padx=8, pady=8)

# Listbox.
lst_bx = tk.Listbox(
    master=lstbx_frame,
    selectmode='single',
    width=40,
    height=5,
    fg='white',
    bg='steelblue')

# Scrollbars.
scrbar_vert = tk.Scrollbar(lstbx_frame, orient='vertical')
scrbar_vert.pack(side=tk.RIGHT, fill=tk.Y)
lst_bx.configure(yscrollcommand=scrbar_vert.set)
scrbar_vert.configure(command=lst_bx.yview)

scrbar_horiz = tk.Scrollbar(lstbx_frame, orient='horizontal')
scrbar_horiz.pack(side=tk.BOTTOM, fill=tk.X)
lst_bx.configure(xscrollcommand=scrbar_horiz.set)
scrbar_horiz.configure(command=lst_bx.xview)

lst_bx.pack()

# Bind mouse dble click to listbox.
lst_bx.bind('<Double-1>', double_clicked)

lst_bx.insert('end', 'It hurt because it mattered. - John Green')
lst_bx.insert('end', 'Be so good they can’t ignore you.- Steve Martin')
lst_bx.insert('end', 'Everything you can imagine is real.- Pablo Picasso')
lst_bx.insert('end', 'No one can make you feel inferior without '
              'your consent. - Eleanor Roosevelt')
lst_bx.insert('end', 'You only live once, but if you do it right, '
                     'once is enough. - Mae West')
lst_bx.insert('end', 'Always forgive your enemies; nothing annoys them so'
              ' much. - Oscar Wilde')
lst_bx.insert('end', 'If you always tell the truth, you dont have to '
                     'remember anything. - Mark Twain')

# Pop up msg.
messagebox.showinfo('Listbox demo',
                    'Double click a selection.')


root.mainloop()
